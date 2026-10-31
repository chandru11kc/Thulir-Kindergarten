from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import EnquiryForm, AdmissionApplicationForm, ContactMessageForm, CareerApplicationForm

# Create your views here.


def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created. You can login now!')
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def logout(request):
    return render(request, 'logout.html')


def infrastructure(request):
    return render(request, 'infrastructure.html')


def programs(request):
    return render(request, 'programs.html')


def gallery(request):
    return render(request, 'gallery.html')


def admissions(request):
    """Handles two separate forms on the same page:
    - the short 'Enquiry' form (Step 01)
    - the full 'Admission Application' form
    Distinguished by a hidden <input name="form_type"> in each <form>.
    """
    enquiry_form = EnquiryForm()
    application_form = AdmissionApplicationForm()

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'enquiry':
            enquiry_form = EnquiryForm(request.POST)
            if enquiry_form.is_valid():
                enquiry_form.save()
                messages.success(request, "Thanks! We've received your enquiry and will reach out shortly.")
                return redirect('admissions')

        elif form_type == 'application':
            application_form = AdmissionApplicationForm(request.POST)
            if application_form.is_valid():
                application = application_form.save(commit=False)
                if request.user.is_authenticated:
                    application.user = request.user
                application.save()
                messages.success(request, "Application submitted! Our admissions team will contact you soon.")
                return redirect('admissions')

    context = {
        'enquiry_form': enquiry_form,
        'application_form': application_form,
    }
    return render(request, 'admissions.html', context)


def contact(request):
    """Handles two separate forms on the same page:
    - the general 'Contact' enquiry form
    - the 'Career Application' form (with resume upload)
    Distinguished by a hidden <input name="form_type"> in each <form>.
    """
    form = ContactMessageForm()
    career_form = CareerApplicationForm()

    if request.method == 'POST':
        form_type = request.POST.get('form_type', 'contact')

        if form_type == 'career':
            career_form = CareerApplicationForm(request.POST, request.FILES)
            if career_form.is_valid():
                career_form.save()
                messages.success(request, "Application received! We'll review it and get back to you if there's a fit.")
                return redirect('contact')
        else:
            form = ContactMessageForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Message sent! We'll get back to you within a day.")
                return redirect('contact')

    context = {'form': form, 'career_form': career_form}
    return render(request, 'contact.html', context)