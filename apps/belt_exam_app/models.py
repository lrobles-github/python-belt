from __future__ import unicode_literals

from django.db import models

from ..login_app.models import User


class TripManager(models.Manager):
    
    def validateData(self, postData):
        if postData:
            if len(postData['destination']) <= 0:
                return False
            elif len(postData['plan']) <= 0:
                return False
            elif postData['start'] > postData['end']:
                return False
            else:
                return True 

    def addTrip(self, postData, user_id):
        
        if Trip.objects.validateData(postData):
            self.create(destination=postData['destination'], start=postData['start'], end=postData['end'],plan=postData['plan'],user=User.objects.get(id=user_id))
            return self.all()
        else:
            return False

    def addGuest(self, trip_id, user_id):

        trip = self.get(id=trip_id)
        guest = User.objects.get(id=user_id)
        trip.guest.add(guest)
        trip.save()
        return self.all()


class Trip(models.Model):
    destination = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()
    plan = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='user_trips')
    guest = models.ManyToManyField(User, related_name='trip_guests')
    objects = TripManager()
    
    def __str__(self):
        return self.id + ' - ' + self.destination + '(Trip)'



