"""
URL configuration for hospitalmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/",views.SignUpView.as_view(),name="signup"),
    path("login/",views.SignInView.as_view(),name="signin"),
    path("logout/",views.sign_out_view,name="signout"),
    path("index/",views.IndexView.as_view(),name="index"),
    path("appointment/",views.AppointmentView.as_view(),name="appointment"),
    path("appointment/list/",views.AppointmentListView.as_view(),name="appointment-list"),
    path("Hospitalmanagement/",views.HomeView.as_view(),name="hospitalmanagement"),
    path("doctor/add/",views.DoctorCreateView.as_view(),name="doctor-add"),
    path("doctor/list/",views.DoctorListView.as_view(),name="doctor-list"),
    path("doctor/detail/<int:pk>/",views.DoctorDetailView.as_view(),name="doctor-detail"),
    path("doctor/edit/<int:pk>/",views.DoctorEditView.as_view(),name="doctor-edit"),
    path("doctor/<int:pk>/remove/",views.doctor_delete_view,name="doctor-delete"),
    path("department/",views.DepartmentCreateView.as_view(),name="department"),
    path("department/list/",views.DepartmentListView.as_view(),name="department-list"),
    path("department/edit/<int:pk>/",views.DepartmentEditView.as_view(),name="department-edit"),
    path("department/<int:pk>/remove/",views.DepartmentDeleteView.as_view(),name="department-delete"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

