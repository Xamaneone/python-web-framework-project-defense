from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from python_web_framework_project_defense.profiles.forms import ProfileForm
from python_web_framework_project_defense.profiles.models import Profile


@login_required
def profile_edit(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'edit_profile.html', context)
