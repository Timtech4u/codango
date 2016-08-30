from django.db import models


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
        ('none', 'None'),
        ('partial', 'Partial'),
        ('full', 'Full'),
    )

    name = models.CharField(max_length=100)
    logo = CloudinaryField(
        'logo', null=True, blank=True)
    description = models.TextField()
    private = models.BooleanField(default=False)
    visibility = models.CharField(
        choices=VISIBILITY_CHOICE, max_length=30, default='Partial')
    creator = models.ForeignKey(User, related_name='communities')
    tags = models.ManyToManyField(Tag)
    default_group_permissions = MultiSelectField(
        choices=group_permissions, default='Block members')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_modified']


class CommunityMember(TimeStampMixin):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined'),
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
        ('block', 'Block'),
        ('suspend', 'Suspend'),
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

