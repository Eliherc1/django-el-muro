from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validador_basico(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        SOLO_LETRAS = re.compile(r'^[a-zA-Z. ]+$')

        errors = {}

        if len(postData['name']) < 2:
            errors['firstname_len'] = "nombre debe tener al menos 2 caracteres de largo";

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "correo invalido"

        if not SOLO_LETRAS.match(postData['name']):
            errors['solo_letras'] = "solo letras en nombreporfavor"

        if len(postData['password']) < 4:
            errors['password'] = "contraseña debe tener al menos 8 caracteres";

        if postData['password'] != postData['password_confirm'] :
            errors['password_confirm'] = "contraseña y confirmar contraseña no son iguales. "

        
        return errors


class User(models.Model):
    CHOICES = (
        ("user", 'User'),
        ("admin", 'Admin')
    )

    name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255 , null=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=70)
    role = models.CharField(max_length=255, choices=CHOICES, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return f"{self.name} {self.last_name}"

    def __repr__(self):
        return f"{self.name} {self.last_name}"


class Message(models.Model):
    message = models.TextField()
    user_m= models.ForeignKey(User, related_name="users", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.message}"

    def __repr__(self):
        return f"{self.message}"


class Comment(models.Model):
    comment = models.TextField()
    user_c= models.ForeignKey(User, related_name="users2", on_delete = models.CASCADE)
    message= models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.comment}"

    def __repr__(self):
        return f"{self.comment}"