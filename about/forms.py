from django import forms


class TeachersRegistration(forms.Form):
    first_name = forms.CharField(
        label='Enter Your First Name', label_suffix=' ')
    last_name = forms.CharField(label='Enter Your Last Name', label_suffix=' ')
    email = forms.EmailField(initial='user@gmail.com', disabled=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
    file = forms.FileField(widget=forms.FileInput, required=False)
