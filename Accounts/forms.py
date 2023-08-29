from django import forms
from Accounts.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'password1')
		widgets = {
			'first_name': forms.TextInput(attrs={
				'class': 'form-control form-control-lg',
          		'placeholder': 'First Name'
      		}),
      		'last_name': forms.TextInput(attrs={
          		'class': 'form-control form-control-lg',
          		'placeholder': 'Last name'
      		}),
      		'username': forms.TextInput(attrs={
        	  	'class': 'form-control form-control-lg',
        	  	'placeholder': 'Username'
      		}),
      		'email': forms.EmailInput(attrs={
        	  	'class': 'form-control form-control-lg',
			  	'autocomplete' : 'username',
        	  	'placeholder': 'Email'
      		}),
      		'password': forms.TextInput(attrs={
        	  	'class': 'form-control form-control-lg',
        	  	'placeholder': 'Password'
      		}),
    	}

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
	
