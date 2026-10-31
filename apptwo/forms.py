from django import forms
from .models import Enquiry, AdmissionApplication, ContactMessage, CareerApplication

ALLOWED_RESUME_EXTENSIONS = ['.pdf', '.doc', '.docx']
MAX_RESUME_SIZE_MB = 5


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'email', 'phone', 'program', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+91 00000 00000'}),
            'message': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Anything specific you want to ask?'}),
        }


class AdmissionApplicationForm(forms.ModelForm):
    class Meta:
        model = AdmissionApplication
        fields = [
            'child_name', 'child_dob', 'program',
            'parent_name', 'parent_email', 'parent_phone', 'address',
        ]
        widgets = {
            'child_name': forms.TextInput(attrs={'placeholder': "Child's full name"}),
            'child_dob': forms.DateInput(attrs={'type': 'date'}),
            'parent_name': forms.TextInput(attrs={'placeholder': 'Parent / Guardian name'}),
            'parent_email': forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
            'parent_phone': forms.TextInput(attrs={'placeholder': '+91 00000 00000'}),
            'address': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Home address'}),
        }


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['parent_name', 'phone', 'email', 'program', 'message']
        widgets = {
            'parent_name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'phone': forms.TextInput(attrs={'placeholder': '+91 00000 00000'}),
            'email': forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': "Tell us a little about what you're looking for..."}),
        }


class CareerApplicationForm(forms.ModelForm):
    class Meta:
        model = CareerApplication
        fields = ['name', 'email', 'phone', 'position', 'resume', 'cover_note']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+91 00000 00000'}),
            'position': forms.TextInput(attrs={'placeholder': 'e.g. Pre-KG Teacher, Admin Staff'}),
            'cover_note': forms.Textarea(attrs={'rows': 3, 'placeholder': 'A few lines about yourself (optional)'}),
        }

    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume:
            ext = '.' + resume.name.rsplit('.', 1)[-1].lower() if '.' in resume.name else ''
            if ext not in ALLOWED_RESUME_EXTENSIONS:
                raise forms.ValidationError('Please upload a PDF or Word document (.pdf, .doc, .docx).')
            if resume.size > MAX_RESUME_SIZE_MB * 1024 * 1024:
                raise forms.ValidationError(f'File is too large — please keep it under {MAX_RESUME_SIZE_MB}MB.')
        return resume