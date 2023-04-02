from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



invalids = ['!', "[", "]", "{", "}", " ", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "="]

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"type": "text", "id": "username"}))
    password = forms.CharField(max_length=None, widget=forms.PasswordInput(attrs={"type": "password", "id": "password"}))
    confirm_password = forms.CharField(max_length=None,  widget=forms.PasswordInput(attrs={"type": "password", "id": "confirm-password"}))


    

    def clean(self):
        cleaned_data = self.cleaned_data
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")
        if not confirm == password:
            self.add_error("confirm_password", "password did not match")
        for char in username:
            if char in invalids:
                self.add_error("username", "invalid username")
                # raise forms.ValidationError("Fix the error or errors to submit")
        return cleaned_data
    

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({"class": "first_name", "required": False})
        self.fields["last_name"].widget.attrs.update({"class": "last_name", "required": False})
        self.fields["email"].widget.attrs.update({"class": "email", "required": False})