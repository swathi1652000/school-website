"""Schoolwebsiteproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home'),
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(),, name='home'),
Including another URLconf
    1. Import the include(), function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'),),
"""
from django.contrib import admin
from django.urls import path
from Schoolwebsite.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Maharishi_Vidya_Mandir/',Maharishi_Vidya_Mandir),
    path('aboutus/',aboutus, name='aboutus'),
    path('bhavans/',bhavans, name='bhavans'),
    path('ac/', ac, name='ac'),
    path('ac2/', ac2, name='ac2'),
    path('activities/', activities, name='activities'),
    path('admission/',admission, name='admission'),
    path('Admissionform/',Admissionform, name='Admissionform'),
    path('busses/',busses, name='busses'),
    path('CCA/',CCA, name='CCA'),
    path('cca2/',cca2, name='cca2'),
    path('Classrooms/',Classrooms, name='Classrooms'),
    path('cocurricularactivities/',cocurricularactivities, name='cocurricularactivities'),
    path('contactus/', contactus, name='contactus'),
    path('dicom/', dicom, name='dicom'),
    path('educomp/', educomp, name='Educomp'),
    path('f1/',f1, name='f1'),
    path('form1/',form1, name='form1'),
    path('form5/',form5, name='form5'),
    path('forms/',forms, name='forms'),
    path('hostel/',hostel, name='hostel'),
    path('imagemap/',imagemap, name='imagemap'),
    path('infrastructure/',infrastructure, name='infrastructure'),
    path('labs/',labs, name='labs'),
    path('library/',library, name='library'),
    path('ncc/',ncc, name='ncc'),
    path('orgchart/',orgchart, name='orgchart'),
    path('osla/',osla, name='osla'),
    path('photogallery/',photogallery, name='photogallery'),
    path('RESULTS/',RESULTS, name='RESULTS'),
    path('rulesandregulations/',rulesandregulations, name='rulesandregulations'),
    path('specialfeatures/',specialfeatures, name='specialfeatures'),
    path('sports/',sports, name='sports'),
    path('XSEED/',XSEED, name='XSEED'),
    path('Highform/',Highform, name='Highform'),
    
]