from django.contrib import admin
from .models import AddOn, Community, Tag

# Register your models here.
admin.site.register((AddOn, Community, Tag))
