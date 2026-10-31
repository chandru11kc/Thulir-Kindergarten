"""
URL configuration for projecttwo project.
"""
from django.contrib import admin
from django.urls import path
from apptwo import views
from django.contrib.auth import views as auth_views

# --- ADD THESE TWO IMPORTS ---
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name='home'),
    path("base/", views.base, name='base'),
    path("about/", views.about, name='about'),
    path("register/", views.register, name='register'),
    path("login/", auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('infrastructure/', views.infrastructure, name='infrastructure'),
    path('programs/', views.programs, name='programs'),
    path('gallery/', views.gallery, name='gallery'),
    path('admissions/', views.admissions, name='admissions'),
    path('contact/', views.contact, name='contact'),
]

# --- ADD THIS BLOCK AT THE VERY BOTTOM, OUTSIDE the urlpatterns list ---
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)