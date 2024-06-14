from django.shortcuts import render, redirect
from authors.forms import RegisterForm
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from authors.forms import RegisterForm, LoginForm
from django.urls import reverse



def register_view(request):

    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    return render(request, 'authors/pages/register.html', {
        'form': form
    })


def register_create(request):

    if not request.POST:
        raise Http404()
    
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Usuário Cadastrado com Sucesso!')

        del(request.session['register_form_data'])
    
    return redirect('authors:register')


def login_view(request):
    form = LoginForm()
    return render(request, 'authors/pages/login.html', {
        'form': form,
        'form_action': reverse('authors:login_success')
    })


def login_success(request):
    if not request.POST:
        raise Http404
    
    form = LoginForm(request.POST)
    login_url = reverse('authors:login')

    if form.is_valid():
        username = form.cleaned_data.get('username', '')
        authenticated_user = authenticate(
            username = username,
            password = form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, f'Bem Vindo {username}')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Login ou Senha Inválidos!')

    return redirect(login_url)