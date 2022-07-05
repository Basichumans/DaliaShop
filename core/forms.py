from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#create a form for the user to sign up
class SingUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=55, required=True, help_text='Jone.')
    last_name=forms.CharField(max_length=55, required=True, help_text='Jones.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    
    #override the default UserCreationForm
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )