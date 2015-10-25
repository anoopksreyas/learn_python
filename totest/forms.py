from django import forms
from models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'occupation', 'hobbies', 'husband_name', 'country', 'state',
                  'city', 'number_of_kids')
