from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView,ListView,DetailView,UpdateView,CreateView
from myapp.forms import RegistrationForm,LoginForm,PasswordResetForm,DoctorCreateForm,DoctorChangeForm,AppointmentForm,DepartmentForm,DepartmentEditForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from myapp.models import Doctor,Appointment,Department
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"you must login to perform this action !!!")
            return redirect("signin")
        return fn(request,*args,**kwargs)
    return wrapper


class SignUpView(CreateView):
    model=User
    template_name="register.html"
    form_class=RegistrationForm
    success_url=reverse_lazy("signin")
    def form_valid(self,form):
        messages.success(self.request,"account created !!!")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,"failed to create account")
        return super().form_invalid(form)
    
class SignInView(View):
    model=User
    template_name="login.html"
    form_class=LoginForm

    def get(self,request,*args,**kwargs):
        form=self.form_class
        return render(request,self.template_name,{"form":form})
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login success")
                return redirect("index")
            messages.error(request,"invalid credentials")
            return render(request,self.template_name,{"form":form})   

@method_decorator(signin_required,name="dispatch")       
class IndexView(TemplateView):
    template_name="index.html"

@method_decorator(signin_required,name="dispatch")       
class HomeView(TemplateView):
    template_name="home.html"

@method_decorator(signin_required,name="dispatch")       
class AppointmentView(CreateView):
    template_name="appointment.html"
    model=User
    form_class=AppointmentForm  
    success_url=reverse_lazy("appointment-list")
    def form_valid(self,form):
        messages.success(self.request,"successful")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,"failed to make appointment")
        return super().form_invalid(form)
    
@method_decorator(signin_required,name="dispatch")           
class AppointmentListView(ListView):
    model=Appointment
    template_name="appointment-list.html"
    context_object_name="appointments" 

    
@method_decorator(signin_required,name="dispatch")           
class DoctorCreateView(CreateView):
    model=Doctor
    template_name="doctor-create.html"
    form_class=DoctorCreateForm
    success_url=reverse_lazy("doctor-list")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"doctor has been created")
        return super().form_valid(form)
   
@method_decorator(signin_required,name="dispatch")           
class DoctorListView(ListView):
    model=Doctor
    template_name="doctor-list.html"
    context_object_name="doctors"   

@method_decorator(signin_required,name="dispatch")       
class DoctorDetailView(DetailView):
    model=Doctor
    template_name="doctor-detail.html"
    context_object_name="doctor"

@method_decorator(signin_required,name="dispatch")       
class DoctorEditView(UpdateView):
    model=Doctor
    form_class=DoctorChangeForm
    template_name="doctor-edit.html"
    success_url=reverse_lazy("doctor-list")

    def form_valid(self, form):
        messages.success(self.request,"changed")
        return super().form_valid(form)
    
@method_decorator(signin_required,name="dispatch")       
class DepartmentCreateView(CreateView):
    model=Department
    template_name="department-create.html"
    form_class=DepartmentForm

    success_url=reverse_lazy("department-list")
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"department has been created")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"failed to create department")
        return super().form_invalid(form)
    
@method_decorator(signin_required,name="dispatch")           
class DepartmentListView(ListView):
    model=Department
    template_name="department-list.html"
    context_object_name="departments" 

@method_decorator(signin_required,name="dispatch")       
class DepartmentEditView(UpdateView):
    model=Department
    form_class=DepartmentEditForm
    template_name="department-edit.html"
    success_url=reverse_lazy("department-list")

    def form_valid(self, form):
        messages.success(self.request,"changed")
        return super().form_valid(form)     

@method_decorator(signin_required,name="dispatch")       
class DepartmentDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Department.objects.get(id=id).delete()
        return redirect("department-list")

@method_decorator(signin_required,name="dispatch")           
def doctor_delete_view(request,*args,**kwargs):
    id=kwargs.get("pk")
    obj=Doctor.objects.get(id=id)
    if obj.user == request.user:
        Doctor.objects.get(id=id).delete()
        messages.success(request,"doctor removed")
        return redirect("doctor-list")
    else:
        messages.error(request,"you donot have the permission to perform this action")
        return redirect("signin")
    

def sign_out_view(request,*args,**kwargs):
    logout(request)
    messages.success(request,"logged out")
    return redirect("signin")

    
    