from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.conf import settings

from .models import Video
from account.models import Profile
from .forms import VideoForm

import redis

r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB,)

class VideoListView(ListView):
    model = Video
    ordering = ['-pub_date']
    context_object_name = 'video_list'
    template_name = 'videos/list.html'
    queryset = Video.objects.all()

def detail(request, video_id):
    try:
        video = Video.objects.get(id=video_id)
    except Video.DoesNotExist:
        raise Http404('Видео не найдено')

    total_views = r.incr(f'video:{video.id}:views'.format(video_id))
    latest_comment_list = video.comment_set.order_by('-id')[:5]
    #profile = get_object_or_404(Profile, user=request.user)

    return render(request, 'videos/detail.html', {'video': video,
                                                  'latest_comment_list': latest_comment_list, 
                                                  #'profile': profile,
                                                  'total_views': total_views,})

@login_required
def create_comment(request, video_id):
    try:
        v = Video.objects.get(id=video_id)
    except:
        raise Http404("Видео не найдено")

    profile = get_object_or_404(Profile, user=request.user)

    v.comment_set.create(author_name=profile, text=request.POST['text'])

    return HttpResponseRedirect(Video.get_absolute_url(self=v))

@login_required
def like(request, video_id):
    video = Video.objects.get(id=video_id)
    profile = get_object_or_404(Profile, user=request.user)
    if profile in video.like.all():
        video.like.remove(profile)
        status = 'unliked'
    else:
        video.like.add(profile)
        status = 'liked'
    return HttpResponseRedirect(Video.get_absolute_url(self=video))

@login_required
def dislike(request, video_id):
    video = Video.objects.get(id=video_id)
    profile = get_object_or_404(Profile, user=request.user)
    if profile in video.dislike.all():
        video.dislike.remove(profile)
        status = 'undisliked'
    else:
        video.dislike.add(profile)
        status = 'disliked'
    return HttpResponseRedirect(Video.get_absolute_url(self=video))


@login_required
def create_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.author_name = request.user.profile
            video.save()
            return render(request, 'videos/create_video_done.html', {'video': video})
    else:
        form = VideoForm()
    return render(request, 'videos/create_video.html', {'form': form})

