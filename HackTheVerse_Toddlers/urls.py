"""HackTheVerse_Toddlers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from healthcare_workers import views as hcw_views
from patient import views as pat_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hcw_views.home_page, name='home_page'),
    path('login/', hcw_views.login_view, name='login'),
    path('logout/', hcw_views.logout_view, name='logout'),
    path('dashboard/', hcw_views.dashboard, name='dashboard'),
    path('patient/<int:patient_id>' , hcw_views.patient_details , name='patientdetails'),
    path('update_patient_details/', hcw_views.update_patient_details , name='update_patient_details'),
    path('fetchdata/', pat_views.run_consumer_thread, name='consumer-thread')
]
