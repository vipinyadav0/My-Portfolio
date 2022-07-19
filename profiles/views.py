from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    if request.method == 'POST':
        print(request.POST['message'])
        message = request.POST['message']
        subject = request.POST['subject']
        recepient = list(request.POST['email'])
        send_mail(subject, message, settings.EMAIL_HOST_USER, recepient, fail_silently=False)
        print("Mail Sent")
    return render(request, 'profiles/index.html')