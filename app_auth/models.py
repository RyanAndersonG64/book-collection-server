from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return self.user.username
    
class Author(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return (f'{self.first_name} {self.last_name}')
    
class Book(models.Model):
    title = models.TextField()
    published = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    reader = models.ManyToManyField(Profile)

    def __str__(self):
        return (f'{self.title} - {self.author}, published {self.published}')
