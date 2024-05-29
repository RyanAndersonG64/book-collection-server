from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# def my_decorator(bob_the_function):
#     def wrapper():
#         print('Before function text')
#         bob_the_function()
#         print('After function text')
#     return wrapper

# @my_decorator         call decorators with @ before function
# def pizzerino():
#     print('no pizzerino')

# pizzerino()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return self.user.username