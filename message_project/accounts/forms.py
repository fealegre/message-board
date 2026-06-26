from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Usuario"
        self.fields["password1"].label = "Contraseña"
        self.fields["password2"].label = "Confirmar contraseña"
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Usuario"
        self.fields["password"].label = "Contraseña"
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
