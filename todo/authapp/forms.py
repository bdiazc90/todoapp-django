from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # first_name = forms.CharField(label="Nombre")

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email",  "password1", "password2")
        labels = {
            'username': ('Nombre de usuario'),
            'first_name': ('Nombre'),
        }

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        # aumentar el email
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user