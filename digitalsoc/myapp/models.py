from django.db import models

# Create your models here.

class User(models.Model):
    email= models.EmailField(unique=True,max_length=30)
    password= models.CharField(max_length=20)
    role= models.CharField(max_length=20)
    isActive= models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email + " | " + self.role


class Chairman(models.Model):
    userid= models.ForeignKey(User, on_delete= models.CASCADE)
    firstname= models.CharField(max_length=20)
    lastname= models.CharField(max_length=20)
    contact= models.CharField(max_length=11)
    blockno= models.CharField(max_length=3)
    houseno= models.CharField(max_length=4)

    def __str__(self):
        return self.firstname + self.lastname + " | " + self.blockno
