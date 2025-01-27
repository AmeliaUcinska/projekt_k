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


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']  # Tylko email, bo username jest nieedytowalne
