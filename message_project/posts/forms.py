from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]
        labels = {
            "title": "Título",
            "body": "Contenido",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingresa el título del post"}),
            "body": forms.Textarea(attrs={"class": "form-control", "rows": 6, "placeholder": "Escribe el contenido de tu post aquí..."}),
        }
