from django.forms import ModelForm
from django import forms
from .models import Video

# Create the form class.
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['MovieID','MovieTitle', 'Actor1Name', 'Actor2Name', 'DirectorName', 'MovieGenre', 'ReleaseYear']
