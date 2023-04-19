from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import ComplainForm
from django.core.mail import send_mail
from blog.models import Post
from .models import Contact
from datetime import datetime
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
# Create your views here.


def home(request):
    allPosts = Post.objects.filter(status=1).order_by('-created_on')[0:6]

    context ={
        'allPosts': allPosts,
    }
    return render(request, 'pages/home.html',context)

def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        feedback= Contact(name=name, email=email, phone=phone,  subject=subject, message=message, create_date= datetime.today())
        feedback.save()
        data = {
            'name':name,
            'email':email,
            'phone':phone,
            'subject':subject,
            'message':message,
        }
        message = '''
        Name:\t{}\n
        Phone:\t{}\n
        Email:\t{}\n
        Subject:\t{}\n
        Message:\t{}\n
        '''.format(data['name'], data['phone'],  data['email'],  data['subject'], data['message'],)
        send_mail('You got a mail!', message, '', ['<dharmendrayadav076@gmail.com>'])
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')
        
    return render(request, 'pages/contact.html')