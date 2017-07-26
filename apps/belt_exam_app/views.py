from django.shortcuts import render, redirect

from .models import *

def index(request):
    if request.session['logged_in'] == True:

        context = {
            'user_trips':Trip.objects.filter(user_id=request.session['user_id']),
            'guest_trips':Trip.objects.filter(guest=request.session['user_id']),
            'other_users_trips':Trip.objects.exclude(user_id=request.session['user_id']).exclude(guest=request.session['user_id'])
        }

        return render(request, 'belt_exam_app/index.html', context)
    else:
         return redirect('/') 


def show_destination(request, id):
    
    if request.session['logged_in'] == True:
        print '###### add destination page'
        context = {
            'trip': Trip.objects.get(id=id)
        }
        return render(request, 'belt_exam_app/show.html', context) 
    else:
         return redirect('/') 


def add_destination_page(request):

    if request.session['logged_in'] == True:
        print '###### add destination page'
        return render(request, 'belt_exam_app/add.html')
    else:
        return redirect('/')



def process_destination(request):
    if request.session['logged_in'] == True:
        print '###### processing destination'
        Trip.objects.addTrip(request.POST, request.session['user_id'])
        return redirect('/travels')
    else:
        return redirect('/')


def process_join(request, id):
    if request.session['logged_in'] == True:
        print '###### processing join'
        Trip.objects.addGuest(id, request.session['user_id'])
        return redirect('/travels')
    else:
        return redirect('/')