from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    contact_form=ContactForm()

    if request.method=="POST":
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get('name', '')
            email=request.POST.get('email', '')
            content=request.POST.get('content', '')

            email_from=settings.EMAIL_HOST_USER

            recipient_list=["pbellido0401@gmail.com"]

            send_mail(name, content, email_from, recipient_list )
            #Suponemos que todo a ido bien redireccionamos
            return redirect(reverse('contact')+"?ok=1")

    return render(request, "contact/contact.html", {'form':contact_form})