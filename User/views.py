from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from User import models
from django.contrib.auth.decorators import login_required
# Create your views here.
#from django.shortcuts import render_to_response
#from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login(request):
    if 'm_id' in request.session:
        return HttpResponseRedirect('/accounts/loggedin')
    c = {}
    c.update(csrf(request))

    return render_to_response('login.html',c)

def auth_view(request):
    username = request.POST.get('username','')

    password = request.POST.get('pwd','')
    user = auth.authenticate(username=username,password=password)

    print user
    if user is not None:
            request.session['m_id'] = user.id
        #if user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/home')
    else:
        return HttpResponseRedirect('/accounts/invalid/')


#@login_required
#@login_required(login_url ='/accounts/login/'):
def loggedin(request):
    # return render_to_response('home.html', {'full_name': request.user.first_name})
    if 'm_id' in request.session:
        return render_to_response('loggedin.html', {'full_name': request.user.first_name})
    else:
        #rquest.session['m_id'] = None
        return HttpResponseRedirect('/accounts/login/')


def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    #print "yoyo"
    #del request.session['m_id']
    return HttpResponseRedirect('/accounts/login')
    #return render_to_response('logout.html')
"""def logout(request):
    try:
        del request.session['member_id']
    except KeyError:login
        pass
    return HttpResponse("You're logged out.")"""
#@login_required
def register(request):
    # if 'm_id' in request.session:
    if 'm_id' in request.session:
        return HttpResponse("alredy signed in")
    else:
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


   # def save(self):
    #    user = models.User()

     #   user.save()
      #  return user


    class Meta:
        model = models.User
        fields = ('email','first_name','last_name','password1','password2')