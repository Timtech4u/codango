import factory

from comments import models


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Comment
