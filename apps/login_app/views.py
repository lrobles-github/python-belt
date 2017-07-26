from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *


def index(request):
    print 'In home page...'
    request.session['logged_in'] = False

    return render(request, 'index.html')


def registration(request):
    print 'View says: Creating registration...'
    errors = User.objects.register(request.POST)
    
    try:
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags='tag')
                print 'View says:', error
                return redirect('/')
    except TypeError:
        print 'View says: TypeError'

    context = { 'success':True } 

    return render(request, 'index.html', context)


def login(request):
    print 'View says: logging in...'
    user_logged_in = User.objects.login(request.POST)
    
    if user_logged_in:
        user = User.objects.get(email=request.POST['login_email'])
        request.session['logged_in'] = True
        request.session['user_id'] = user.id
        request.session['display_name'] = user.first_name
        
        context = { 
            'display_name':user.first_name, 
            'user_logged_in': True
        }
        return redirect('/travels')
    else:
        context = { 'login_failed':'You have entered invalid credentials.'}
        return render(request, 'index.html', context)


def logout(request):
    print 'View says: logging out...'
    user_logged_in = False
    request.session.flush()
    return redirect('/')
	