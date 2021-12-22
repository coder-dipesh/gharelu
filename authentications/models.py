from django.db import models
from passlib.hash import pbkdf2_sha256

class UserSignUp(models.Model):
    username = models.CharField(max_length=20,null=True)
    email = models.EmailField()
    password1 = models.CharField(max_length=25,null=True)

    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password1)