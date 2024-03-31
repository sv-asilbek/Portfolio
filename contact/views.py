from urllib import request

from django.contrib import messages
from django.shortcuts import render, redirect
from .form import ContactForm


def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        print(form.data)
        messages.success(request, 'successfully send your message')
        return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'contact.html', context)
