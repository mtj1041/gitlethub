from django import forms

class UserForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100)

class UploadFileForm(forms.Form):
   docfile = forms.FileField(
        label='Select a file'
    )