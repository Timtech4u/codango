import os
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from resources.models import NotificationQueue
from django.utils import timezone
from pyfirebase import Firebase
from resources.tasks import send_notification
from celery.task.control import revoke


def is_user_logged_in(user_id):
    """
    Returns True for logged-in user
    We're using Firebase for this
    """
    firebase = Firebase('https://project-8667655276128018284.firebaseio.com/')

    # Create a Firebase reference
    ref = firebase.ref('presence')
    users = ref.get()
    return True if users.get(str(user_id), None) is not None else False

def schedule_notification(author, resource_link, username,
                          request, notification_type):
    """
    Creates a task to be queued
    The notification contains operations on a resource (like, dislike, comment)
    """
    task_id = 'task_' + str(author.id)

    # Create/ Update notification as long as the author is logged out
    if not is_user_logged_in(author.id):
        queue_exists = NotificationQueue.objects.filter(user=author)
        if not queue_exists:
            data = {
                'author': author,
                'resource_link': request.build_absolute_uri(
                    resource_link),
                'settings_link': request.build_absolute_uri(
                    '/user/' + author.username + '/settings'
                )
            }
            # Create task on celery
            send_notification.apply_async(
                kwargs=data,
                countdown=int(os.getenv('CELERY_NOTIFICATION_TIMEOUT')) or 600,
                task_id=task_id
            )


        exists = NotificationQueue.objects.filter(
            user=author, notification_type=notification_type).first()
        if exists:
            exists.count += 1
            exists.save()
        else:
            queue = NotificationQueue(
                user=author,
                notification_type=notification_type,
                count=0,
                first_interaction=username
            )
            queue.save()

    # Delete the notifications as soon as the author is logged in
    else:
        exists = NotificationQueue.objects.filter(user=author)
        if exists:
            exists.delete()
