from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from videos.models import Video

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request, 'registration/edit_done.html')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'registration/edit.html', {'user_form': user_form, 'profile_form': profile_form})

class ProfileListView(ListView):
    model = Profile
    context_object_name = 'profile_list'
    template_name = 'account/list.html'
    queryset = Profile.objects.all()

def profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    videos = Video.objects.filter(author_name=profile)
    return render(request, 'account/detail.html', {'profile': profile, 'videos': videos})