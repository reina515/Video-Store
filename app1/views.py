from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video
from .forms import VideoForm


def index(request):
    return render(request, 'index.html')

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})


def video_create(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'video_form.html', {'form': form})


def video_update(request, pk):
    try:
        video = Video.objects.get(pk=pk)
    except Video.DoesNotExist:
        return HttpResponse("Video not found.", status=404)

    if request.method == "POST":
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm(instance=video)
    return render(request, 'video_form.html', {'form': form})


def video_delete(request, pk):
    try:
        video = Video.objects.get(pk=pk)
    except Video.DoesNotExist:
        return HttpResponse("Video not found.", status=404)

    if request.method == "POST":
        video.delete()
        return redirect('video_list')
    return render(request, 'video_confirm_delete.html', {'video': video})

