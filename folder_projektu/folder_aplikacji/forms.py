from django import forms
from .models import Opinion

class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['name', 'content']


from django import forms
from .models import UserImage

class UserImageForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = ['title', 'image']

