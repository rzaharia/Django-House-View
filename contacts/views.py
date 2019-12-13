from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check user has made inqury already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already made the inquiry!")
                return redirect('/listings/' + listing_id)

        current_contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone,
                                  message=message, user_id=user_id)
        current_contact.save()
        # Send email
        subject = 'Thank you for registering to our site'
        message = ' it  means a world to us '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['zahariarauul@gmail.com']
        values = [settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD]
        # send_mail(subject, message, email_from, recipient_list)

        # send_mail('Property listing Inquiry',
        #           'There has been in inquiry for ' + listing + '. Sign into admin panel for more info.',
        #           settings.EMAIL_HOST, ['zahariarauul@gmail.com'], fail_silently=False)
        messages.success(request, 'Your request has been submitted!')
        return redirect('/listings/' + listing_id)
    return redirect('/listings/')
