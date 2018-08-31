from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
#you can add more regex!
NAME_REGEX = re.compile(r'^[a-zA-Z\s]+$')
EMAIL_REGEX = re.compile(r'^[\w\s]+$')
PASSWORD_REGEX = re.compile('.*\s')

class UserManager(models.Manager):
    def validate_reg(self, input):
        errors = []
        name = input['name']
        username = input['username']
        pw = input['pw']
        pw_conf = input['pw_confirm']
        if not name or name.isspace():
            errors.append(("enter:name","name"))
        elif len(name) < 3 or not NAME_REGEX.match(name):
            errors.append(("name:invalid","name"))
        if not username or username.isspace():
            errors.append(("enter: username","username"))
        elif len(username) < 3 or not EMAIL_REGEX.match(username):
            errors.append(("username: invalid","username"))
        elif self.filter(username=username).exists():
            errors.append(("username: already exist","register"))
        if not pw or pw.isspace():
            errors.append(("password: none","pw"))
        elif PASSWORD_REGEX.match(pw) or len(pw) < 8:
            errors.append(("password: invalid","pw"))
        if not pw == pw_conf:
            errors.append(("password: doesn't match","confirm"))
        

        if errors:
            return (False, errors)
        else:
            hashed = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
            user = self.create(name=name, username=username, pw_hash=hashed)
            return (True, user)

    def validate_log(self, input):
        errors = []
        user = User.objects.filter(username=input['username'])
        if user.exists():
            hashed_pw = user[0].pw_hash.encode()
            input_pw = input['pw'].encode()
            if bcrypt.checkpw(input_pw, hashed_pw):
                return (True, user[0])
            else:
                errors.append(("password:incorrect","login_pw"))
        else:
            errors.append(("username: doesn't exist","login_user"))
        return (False, errors)

class User(models.Model):
    name = models.CharField(max_length=55)
    username = models.CharField(max_length=55)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self):
        return "<User object: {} {} {} {} {}>".format(self.name, self.username, self.password, self.created_at, self.updated_at)

    
