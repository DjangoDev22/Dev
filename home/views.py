from django.shortcuts import render, redirect
from posts.models import Posts
import datetime

from newsletter.models import Subscripers, MailMessages
from newsletter.forms import SubscriptionForm, MailMessagesForm

from django.conf import settings
from django.core.mail import send_mail
from django_pandas.io import read_frame

# Create your views here.
def home(request):
    # newsletter Form
    if request.method == 'POST':
        sub_form = SubscriptionForm(request.POST)
        if sub_form.is_valid():
            if Subscripers.objects.filter(email=sub_form.cleaned_data['email']).exists():
                return redirect('home')
            sub_form.save()
    else:
        sub_form = SubscriptionForm()


    # using datetime module and timedelta Method ...
    # timedelta >> diffrence between 2 times or 2 dates .


    # latest posts
    three_days_ago = datetime.date.today() - datetime.timedelta(days=3)
    latest_posts = Posts.objects.filter(created_at__gte=three_days_ago).order_by('-created_at')[:4]

    # Trending posts
    week_ago = datetime.date.today() - datetime.timedelta(days=7)
    trending_posts = Posts.objects.filter(created_at__gte=week_ago).order_by('-created_at')[:4]

    context = {
        'sub_form': sub_form,
        'latest_posts': latest_posts,
        'trending_posts': trending_posts,
    }

    return render(request, 'home/home.html', context)

def latest_posts(request):
    from_three_days = datetime.date.today() - datetime.timedelta(days=3)
    trending_posts = Posts.objects.filter(created_at__lte=three_days_ago).order_by('-created_at')[:4]

    context = {
        'latest_posts': latest_posts,
    }

    return render(request, 'home/latest_posts.html', context)

def trending_posts(request):
    week_ago = datetime.date.today() - datetime.timedelta(days=7)
    trending_posts = Posts.objects.filter(created_at__gte=week_ago).order_by('-created_at')[:4]

    context = {
        'trending_posts': trending_posts,
    }

    return render(request, 'home/trending_posts.html', context)


def send_mails(request):
    # send multiple emails
    qs = Subscripers.objects.all()
    df = read_frame(qs, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    print(mail_list)
    if request.method == 'POST':
        form = MailMessagesForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=form.cleaned_data.get('title'),
                message=form.cleaned_data.get('message'),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=mail_list,
                fail_silently=False
            )
            return redirect('home')

    else:
        form = MailMessagesForm()

    context={
        'form': form,
    }

    return render(request, 'home/send_mails.html', context)
