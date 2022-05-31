from django.shortcuts import render
from landing.models import GetMeNotified
# Create your views here.

def notification(request):
    if request.method == "POST":
        email_notification = GetMeNotified()
        email_notification.user_email = request.POST.get("user_email")
        email_notification.save()
    return render(request, 'landing/demo.html')