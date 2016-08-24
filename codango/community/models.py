from django.contrib.auth.models import User
from django.db import models

from cloudinary.models import CloudinaryField
from multiselectfield import MultiSelectField

group_permissions = (
    ('INVITE_MEMBER', 'Send invites'),
    ('DELETE_MEMBER', 'Remove members'),
    ('BLOCK_MEMBER', 'Block members'),
    ('SUSPEND_MEMBER', 'Suspend members'),
)


class TimeStampMixin(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(TimeStampMixin):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_modified']


class Permission(TimeStampMixin):
    label = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.label

    class Meta:
        ordering = ['-date_modified']


class Community(TimeStampMixin):
    VISIBILITY_CHOICE = (
        ('None', 'None'),
        ('Partial', 'Partial'),
        ('Full', 'Full'),
    )

    name = models.CharField(max_length=100)
    logo = CloudinaryField(
        'logo', null=True, blank=True)
    description = models.TextField()
    private = models.BooleanField(default=False)
    visibility = models.CharField(
        choices=VISIBILITY_CHOICE, max_length=30, default='Partial')
    user = models.ForeignKey(User, related_name='communities')
    tags = models.ManyToManyField(Tag)
    default_group_permissions = MultiSelectField(
        choices=group_permissions, default='Block members')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_modified']


class CommunityMember(TimeStampMixin):
    STATUS_CHOICE = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    )
    community = models.ForeignKey(Community, related_name='members')
    user = models.ForeignKey(User, related_name='member')
    invitor = models.ForeignKey(User, related_name='invited_by')
    status = models.CharField(
        choices=STATUS_CHOICE, max_length=20, default='Pending')
    permission = MultiSelectField(
        choices=group_permissions, default='Block members')

    def __str__(self):
        return '{} ({})'.format(self.user.username, self.community.name)

    class Meta:
        ordering = ['-date_modified']


class CommunityBlacklist(TimeStampMixin):
    BLACKLIST_CHOICE = (
        ('Block', 'Block'),
        ('Suspend', 'Suspend'),
    )
    user = models.ForeignKey(User, related_name='community_blacklist')
    blacklister = models.ForeignKey(User, related_name='community_blacklister')
    blacklist_type = models.CharField(
        choices=BLACKLIST_CHOICE, max_length=20, default='Block')
    community = models.ForeignKey(Community)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-date_modified']
