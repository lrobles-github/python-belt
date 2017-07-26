from __future__ import unicode_literals

from django.db import models
 
import re

import bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]*$')


class UserManager(models.Manager):

    def register(self, postData):

        first_name = postData['first_name']
        last_name = postData['last_name']
        email = postData['email']
        password = postData['password']
        password_confirm = postData['password_confirm']

        errors = {}

        # Validate names
        if len(first_name) < 2 or len(last_name) < 2:
            print 'Model says: a name is too short'
            errors['short_name'] = 'One of your names is too short. It must be at least 2 characters long.'
        # Validate email with Regex
        elif not EMAIL_REGEX.match(email):
            print 'Model says: email entered is not valid'
            errors['invalid_email'] = 'Your email is not a valid email address. Please try again.'
        # Check if email has been used
        elif User.objects.filter(email=email):
            print 'Model says: email already exists'
            errors['email_already_exists'] = 'This email already exists. Please try again with a different email address.'
        # Validate password
        elif len(password) < 8:
            print 'Model says: password is too short'
            errors['short_password'] = 'Your password is too short. It must be at least 8 characters long.'
        elif password != password_confirm:
            print 'Model says: passwords don\'t match'
            errors['password_no_match'] = 'Your passwords didn\'t match. Please try again.'
        else:
            p_hash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            User.objects.create(first_name=first_name, last_name=last_name, email=email, password=p_hash)

            print 'Model says: last object created:', User.objects.last()
            print 'Model says: here is what we have:', User.objects.all()

        return errors
        
    def login(self, loginData):

        email = loginData['login_email']
        password = loginData['login_password']
        errors = {}

        user = User.objects.filter(email=email)

        if user:
            print 'Model says: User exists! This is User', user
            hashed = bcrypt.hashpw(loginData['login_password'].encode(), user[0].password.encode())
			# if hashed  != results['user'][0].password:
            if user[0].password == hashed:
                # request.session['logged_in'] = True
                # request.session['user_id'] = User.objects.get(email=loginData('login_email'))
                return True
        else:
            print 'Model says: user doesn\'t exist'
            errors['no_matching_user'] = 'That user doesn\'t exist. Please use a valid email.'
            request.session['logged_in'] = False
            return False


class User(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.email

        
