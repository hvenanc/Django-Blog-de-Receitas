from django.forms import Form, ModelForm
from django.contrib.auth.models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        ]
