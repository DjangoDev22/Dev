from django.conf import settings
from django.core.mail import send_mail

from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Posts
# from django.views.generic import ListView

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from users.forms import (
    UserSignupForm,
    UserLoginForm,
    ContactForm,
    UserForm,
    ProfileForm
)

# Create your views here.
def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return redirect('user_signup')
            elif form.cleaned_data['password'] != form.cleaned_data['password_confirmation']:
                return redirect('user_signup')
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()
                return redirect('user_login')

    else:
        form = UserSignupForm()

    context={
        'form': form,
    }

    return render(request, 'users/signup.html', context)

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                return redirect('user_login')

    else:
        form = UserLoginForm()

    context={
        'form': form,
    }

    return render(request, 'users/login.html', context)

def user_logout(request):
    logout(request)
    return redirect("user_login")

def user_profile(request, pk):
    user_profile= get_object_or_404(Profile, pk= pk)
    # user_profile = Profile.objects.get(user=user)
    user= user_profile.user
    user_articles = Posts.objects.filter(author=user)

    user= user_profile.user
    user_favourites = Posts.objects.filter(favourites=user)
    context={
        'user_profile': user_profile,
        'user_articles': user_articles,
        'user_favourites': user_favourites,
    }

    return render(request, 'users/user_profile.html', context)

def add_profile(request):
    if request.method == 'POST':
        u_form = UserForm(request.POST)
        p_form = ProfileForm(request.POST, request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()

            myform = p_form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect('user_profile')
    else:
        u_form = UserForm()
        p_form = ProfileForm()

    context={
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/add_profile.html', context)

def edit_profile(request, pk):
    profile= get_object_or_404(Profile, pk= pk)
    # profile = Profile.objects.get(user=request.user)
    user = request.user
    if request.method == 'POST':
        u_form = UserForm(request.POST, instance=user)
        p_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()

            my_p_form = p_form.save(commit=False)
            my_p_form.user = request.user
            my_p_form.save()
            return redirect('user_profile')
    else:
        u_form = UserForm(instance=user)
        p_form = ProfileForm(instance=profile)

    context={
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/edit_profile.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=form.cleaned_data.get('subject'),
                message=form.cleaned_data.get('message'),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[form.cleaned_data.get('email')],
                fail_silently=False
            )
            return redirect('home')

    else:
        form = ContactForm()

    context={
        'form': form,
    }

    return render(request, 'users/e-mail.html', context)
