import os
from userprofile import frequency_updates

from celery.task import task
from account.emails import SendGrid
from resources.models import Resource, NotificationQueue
from django.template import loader
from django.db.models import Count
from codango.settings.base import CODANGO_EMAIL
from django.template import Context, loader


@task
def send_recent_posts(frequency):
    recipients = frequency_updates.updates(frequency)

    # Top 5 posts on Codango
    popular_posts = Resource.objects.annotate(
        num_comments=Count('comments')).annotate(
        num_votes=Count('votes')).order_by(
        '-num_comments', '-num_votes')[:5]

    # URL to Codango
    codango_url = os.getenv('CODANGO_HOME')

    # Compose the email
    message = SendGrid.compose(
        sender='Codango <{}>'.format(CODANGO_EMAIL),
        recipient=None,
        subject="Top Posts on Codango",
        recipients=recipients,
        text=None,
        html=loader.get_template(
            'emails/popular-post-updates.html'
        ).render(Context({
            'popular_posts': popular_posts,
            'codango_url': codango_url
        }))
    )

    # send email
    response = SendGrid.send(message)
    return response


@task(name='send_notice')
def send_notification(author, resource_link, settings_link):

    # Create a new task
    queues = NotificationQueue.objects.filter(user=author)
    if not queues:
        return

    message = ''
    for queue in queues:
        content = queue.first_interaction
        if queue.notification_type == 'likes':
            if queue.count > 0:
                content += ' and ' + str(queue.count) + ' other person(s)'
            content += ' liked your resource.'
        elif queue.notification_type == 'unlikes':
            if queue.count > 0:
                content += ' and ' + str(queue.count) + ' other person(s)'
            content += ' down voted your resource.'
        elif queue.notification_type == 'comment':
            if queue.count > 0:
                content += ' and ' + str(queue.count) + ' other person(s)'
            content += ' commented on your resource.'
        message += content

    resource_email_context = {
        "subject": 'Guess what ' + author.username + '!',
        "content": message,
        "resource_link": resource_link,
        "settings_link": settings_link
    }

    message = SendGrid.compose(
        'Codango <{}>'.format(CODANGO_EMAIL),
        author.email,
        'Codango: Notification',
        None,
        loader.get_template('emails/notification.txt'
                            ).render(resource_email_context),
        loader.get_template('emails/notification.html'
                            ).render(resource_email_context),
    )

    SendGrid.send(message)
    queues.delete()
