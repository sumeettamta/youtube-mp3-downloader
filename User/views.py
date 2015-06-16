from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from User import models

def login(request):
    c = {}
    c.update(csrf(request))
    if 'm_id' in request.session:
        return HttpResponseRedirect('/home')
    else:
        return render(request, 'login.html', c)

def auth_view(request):
    if 'm_id' in request.session:
        return HttpResponseRedirect('/home')

    username = request.POST.get('username', '')
    password = request.POST.get('pwd', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
            request.session['m_id'] = user.id
            auth.login(request, user)
            return HttpResponseRedirect('/home')
    else:
        return render(request, 'login.html', {'error': True})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login')

def register(request):
    if 'm_id' in request.session:
        return HttpResponseRedirect('/home')
    else:
        if request.method == 'POST':
            form = UserCreateForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                new_user.save()
                return HttpResponseRedirect('/accounts/login')
            else:
                return render(request, "signup.html", {'error': True, 'form': form})
        else:
            form = UserCreateForm()
            return render(request, "signup.html", {'form': form})


class UserCreateForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2', 'user_type', 'gender')