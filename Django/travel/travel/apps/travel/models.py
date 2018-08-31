from __future__ import unicode_literals
from django.db import models
#.. here!
from ..login_register.models import User
from datetime import datetime

class TravelManager(models.Manager):
    def validate_travel(self, input, user):
        errors = []
        loc = input['destination']
        plan = input['plan']
        date_from = input['date_from']
        date_to = input['date_to']
        if not loc or loc.isspace():
            errors.append("Input:Destination")
        if not plan or plan.isspace():
            errors.append("input: plan")
        if not date_from:
            errors.append("select: travel date from")
        if not date_to:
            errors.append("select: travel date to")
        
        
        #-----for future dates------------------------------------------------
        if date_from and date_to:
            today = datetime.now().strftime('%Y-%m-%d')
        if date_from < today:
                errors.append("future notnow")
        if date_from > date_to:
                errors.append('dates dont match')
        
        if errors:
            return (False, errors)
        trip = self.create(destination=loc, plan=plan, date_from=date_from, date_to=date_to, user=user)
        trip.users.add(user)
        return (True, "trip added!")


class Travel(models.Model):
    destination = models.CharField(max_length=55)
    plan = models.TextField()
    date_from = models.DateField()
    date_to = models.DateField()
    #to connect-----------manymany and forign
    users = models.ManyToManyField(User, related_name='travels')
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TravelManager()
    def __repr__(self):
        return self.destination

    
