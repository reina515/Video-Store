from django.db import models

# Create your models here.


class Video(models.Model):
    MovieID = models.IntegerField(primary_key=True)
    MovieTitle = models.CharField(max_length=100)
    Actor1Name = models.CharField(max_length=50)
    Actor2Name = models.CharField(max_length=50, blank=True)
    DirectorName = models.CharField(max_length=50)
    MovieGenre = models.CharField(max_length=30)
    ReleaseYear = models.IntegerField()


