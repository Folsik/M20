from .models import Profile
from django.forms import ModelForm

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = 'avatar', 'username', 'first_name', 'last_name', 'bio'
