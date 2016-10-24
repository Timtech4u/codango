from cloudinary.forms import CloudinaryFileField
from django.forms import ModelForm

from .models import Community


class CommunityForm(ModelForm):

    class Meta:
        model = Community
        exclude = ['creator', 'tags']

    logo = CloudinaryFileField(
        required=False,
        options={
            'resource_type': 'raw',
            'use_filename': True,
            'allowed_formats': ['png', 'jpg', 'jpeg'],
            'crop': 'limit',
            'width': 100,
            'height': 100,
            'eager': [{'crop': 'limit', 'width': 100, 'height': 100}],
        })

    def __init__(self, *args, **kwargs):
        super(CommunityForm, self).__init__(*args, **kwargs)
        self.fields[
            'name'].widget.attrs['placeholder'] = 'Community Name (Not more than 50 characters)'
        self.fields[
            'description'].widget.attrs['placeholder'] = 'Describe your community (Not more than 1000 characters)'
        self.fields['visibility'].widget.attrs['disabled'] = True
