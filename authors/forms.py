from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):

    first_name = forms.CharField(
        required= True,
        label= 'Nome',
        widget= forms.TextInput(attrs={
            'placeholder': 'Insira seu None',
        }),
        
    )

    last_name = forms.CharField(
        required= True,
        label= 'Sobrenome',
        widget= forms.TextInput(attrs={
            'placeholder': 'Insira seu Sobrenone'
        }),
    )

    username = forms.CharField(
        required= True,
        label= 'Nome de Usuário',
        widget= forms.TextInput(attrs={
            'placeholder': 'Username'
        }),
    )

    email = forms.CharField(
        required= True,
        label= 'E-mail',
        widget= forms.TextInput(attrs={
            'placeholder': 'Insira seu E-mail'
        }),
    )

    password = forms.CharField(
        required=True,
        widget= forms.PasswordInput(attrs={
            'placeholder': 'Digite sua Senha'
        }),
        label= 'Senha',
        min_length = 8
    )

    confirme_password = forms.CharField(
        required=True,
        widget= forms.PasswordInput(attrs={
            'placeholder': 'Confirme sua Senha'
        }),
        label= 'Confirmação de Senha',
        min_length = 8
    )

    # Validações

    def clean(self):
        clean_data = super().clean()

        password = clean_data.get('password')
        confirme_password = clean_data.get('confirme_password')
        
        if password != confirme_password:
            password_error = ValidationError(
                'A senha deve ser igual a sua confirmação!',
                code='invalid'
            )
            raise ValidationError({
                'password': password_error,
                'confirme_password' : [
                    password_error
                ]
            })