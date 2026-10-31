from django.contrib import admin
from .models import Enquiry, AdmissionApplication, ContactMessage, CareerApplication


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'program', 'created_at')
    list_filter = ('program', 'created_at')
    search_fields = ('name', 'email', 'phone')


@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):
    list_display = ('child_name', 'program', 'parent_name', 'parent_phone', 'status', 'created_at')
    list_filter = ('program', 'status', 'created_at')
    search_fields = ('child_name', 'parent_name', 'parent_email', 'parent_phone')
    list_editable = ('status',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('parent_name', 'phone', 'email', 'program', 'is_read', 'created_at')
    list_filter = ('is_read', 'program', 'created_at')
    search_fields = ('parent_name', 'email', 'phone')
    list_editable = ('is_read',)


@admin.register(CareerApplication)
class CareerApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'phone', 'email', 'resume_link', 'is_reviewed', 'created_at')
    list_filter = ('is_reviewed', 'created_at')
    search_fields = ('name', 'email', 'phone', 'position')
    list_editable = ('is_reviewed',)

    def resume_link(self, obj):
        from django.utils.html import format_html
        if obj.resume:
            return format_html('<a href="{}" target="_blank">Download</a>', obj.resume.url)
        return '—'
    resume_link.short_description = 'Resume'