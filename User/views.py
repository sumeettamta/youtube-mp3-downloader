from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from User import models
# Create your views here.
#from django.shortcuts import render_to_response
#from django.contrib.auth import authenticate, login

def login(request):
    c = {}
    c.update(csrf(request))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    #print c
=======
>>>>>>> 2ed739edfd5f81fb5d365d4737e03de3c220daeb
=======
>>>>>>> 2ed739edfd5f81fb5d365d4737e03de3c220daeb
=======
>>>>>>> 2ed739edfd5f81fb5d365d4737e03de3c220daeb
    return render_to_response('login.html',c)

def auth_view(request):
    username = request.POST.get('username','')
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    password = request.POST.get('pwd','')
    user = auth.authenticate(username=username,password=password)
=======
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)

>>>>>>> 2ed739edfd5f81fb5d365d4737e03de3c220daeb
=======
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)

>>>>>>> 2ed739edfd5f81fb5d365d4737e03de3c220daeb
=======
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)

>>>>>>> 2ed739edfd5f81fb5d365d4737e03de3c220daeb
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid/')
def loggedin(request):
    return render_to_response('loggedin.html',
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                                {'full_name': request.user.first_name})
=======
                                {'full_name': request.user.username})
>>>>>>> 2ed739edfd5f81fb5d365d4737e03de3c220daeb
=======
                                {'full_name': request.user.username})
>>>>>>> 2ed739edfd5f81fb5d365d4737e03de3c220daeb
=======
                                {'full_name': request.user.username})
>>>>>>> 2ed739edfd5f81fb5d365d4737e03de3c220daeb
def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    #print "yoyo"
    return HttpResponseRedirect('/accounts/login')
    #return render_to_response('logout.html')

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return  render_to_response('sucess.html')
    else:
        form = UserCreateForm()
    return render(request, "signup.html", {
        'form': form,
    })


class UserCreateForm(UserCreationForm):

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 2ed739edfd5f81fb5d365d4737e03de3c220daeb
=======
>>>>>>> 2ed739edfd5f81fb5d365d4737e03de3c220daeb
    def save(self):
        user = models.User()
        user.email="andjna2d"
        user.first_name="div"
        user.last_name="div"
        user.save()
        return user

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2ed739edfd5f81fb5d365d4737e03de3c220daeb
=======
>>>>>>> 2ed739edfd5f81fb5d365d4737e03de3c220daeb
=======
>>>>>>> 2ed739edfd5f81fb5d365d4737e03de3c220daeb
    class Meta:
        model = models.User
        fields = ('email','first_name','last_name','password1','password2')