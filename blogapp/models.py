from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    usuario=models.CharField(max_length=50)
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField(max_length=50)

    def __str__(self) -> str:
        return self.nombre+''+self.apellido


class Avatar(models.Model):
    imagen=models.ImageField(upload_to='avatar')
    user=models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"