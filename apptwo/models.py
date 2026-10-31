from django.db import models
from django.contrib.auth.models import User


PROGRAM_CHOICES = [
    ('playgroup', 'Play Group'),
    ('prekg', 'Pre-KG'),
    ('lkg', 'LKG'),
    ('ukg', 'UKG'),
    ('daycare', 'Day Care'),
]


class Enquiry(models.Model):
    """A quick 'Step 01' enquiry submitted from the Admissions page —
    lightweight, no login required."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    program = models.CharField(max_length=20, choices=PROGRAM_CHOICES, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Enquiries'

    def __str__(self):
        return f"{self.name} — {self.get_program_display() or 'No program'}"


class AdmissionApplication(models.Model):
    """The full application submitted from the Admissions page.
    Linked to a parent account when the parent is logged in, but the
    field is nullable so it still works if they apply before registering."""

    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('reviewed', 'Reviewed'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL, related_name='admission_applications'
    )

    child_name = models.CharField(max_length=100)
    child_dob = models.DateField(verbose_name="Child's Date of Birth")
    program = models.CharField(max_length=20, choices=PROGRAM_CHOICES)

    parent_name = models.CharField(max_length=100)
    parent_email = models.EmailField()
    parent_phone = models.CharField(max_length=15)
    address = models.TextField(blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.child_name} ({self.get_program_display()}) — {self.get_status_display()}"


class ContactMessage(models.Model):
    """Submitted from the general Contact page form."""
    parent_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    program = models.CharField(max_length=20, choices=PROGRAM_CHOICES, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.parent_name} — {self.created_at:%d %b %Y}"


def resume_upload_path(instance, filename):
    """Keep resumes organised as media/resumes/<applicant-name>/<filename>"""
    safe_name = "".join(c for c in instance.name if c.isalnum() or c in (' ', '_', '-')).strip().replace(' ', '_')
    return f"resumes/{safe_name}/{filename}"


class CareerApplication(models.Model):
    """Submitted from the Careers section on the Contact page.
    Stored in its own table, separate from general contact enquiries."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=100, blank=True, verbose_name="Role Interested In")
    resume = models.FileField(upload_to=resume_upload_path)
    cover_note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_reviewed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.position or 'General'} ({self.created_at:%d %b %Y})"