from django.db import models

class Photo(models.Model):
    id = models.IntegerField(max_length=255)
    place = models.CharField(max_length=255)
    date = models.DateField()
    creator = models.ForeignKey('User', related_name="photo", on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class User(models.Model):
    name = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name