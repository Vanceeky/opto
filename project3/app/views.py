from asyncio.proactor_events import _ProactorSocketTransport
from telnetlib import STATUS
from tkinter.messagebox import NO
from django.apps import AppConfig
from django.shortcuts import render, redirect
from django.http import HttpResponse
import app

from app.models import Appointment, Patient


from .forms import AppointmentForm, CreateUserForm, PatientForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only

from .filters import AppointmentFilter
from django.forms import inlineformset_factory

# Create your views here.

def sign_in(request):
    return render(request, 'app/sign-in.html')

def index(request):
    return HttpResponse(" Index.html ")

@unauthenticated_user
def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')


            messages.success(request, "Account was created for " + username)
            return redirect('signin')


    context = {
        'form': form
    }

    return render(request, 'app/register.html', context)


@unauthenticated_user
def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return  redirect('dashboard')

        else:
            messages.info(request, "Username or password is incorrect")
        

    context = {

    }

    return render(request, 'app/sign-in.html', context)


def logout_user(request):
    logout(request)
    return redirect('signin')


@login_required(login_url='login')
@admin_only
def dashboard(request):

    appointments = Appointment.objects.all()
    patients = Patient.objects.all()

    total_appointments = appointments.count()
    total_patients = patients.count()

    pending = appointments.filter(status = 'Pending')
    confirmed = appointments.filter(status = 'Confirmed')
    cancelled = appointments.filter(status = 'Cancelled')
    completed = appointments.filter(status = 'Completed')

    pending_count = appointments.filter(status = 'Pending').count()
    confirmed_count = appointments.filter(status = 'Confirmed').count()
    cancelled_count = appointments.filter(status = 'Cancelled').count()
    completed_count = appointments.filter(status = 'Completed').count()

    context = {
        'patient': patients,
        'appointment': appointments,

        'total_appointments': total_appointments,
        'total_patients': total_patients,

        'pending': pending,
        'confirmed': confirmed,
        'cancelled': cancelled,
        'completed': completed,

        'pending_count': pending_count,
        'confirmed_count': confirmed_count,
        'cancelled_count': cancelled_count,
        'completed_count': completed_count,
    }

    return render(request, 'app/dashboard.html', context)

def patient(request, pk_test):
    
    
    patient = Patient.objects.get(id = pk_test)
    appointment = request.user.patient.appointment_set.all()
    #appointment = request.user.patient
    #appointment = Appointment.objects.get(id=pk_test)
    form = AppointmentForm(instance=appointment)


    context = {
        'patient': patient,
        'appointment': appointment,
        'form': form
    }


    return render(request, 'app/qwe.html', context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def User_page(request):
    return render(request, 'app/home.html')


def send_request(request):


    appointment = request.user.patient.appointment_set.all()


    if appointment is None:

        firstname = request.user.first_name
        lastname = request.user.last_name
        email = request.user.email


        patient = Patient.objects.create(
            user = request.user,
            first_name = firstname,
            last_name = lastname,
            email = email,
        )

        patient.save()

        appointment = Appointment.objects.create(
            patient = patient
        )

        appointment.save()

        return redirect('my_appointment')
    
    else:
        messages.info(request, " You already sent a request")
        return HttpResponse (" You already sent a request")


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def my_appointment(request):

    appointment = request.user.patient.appointment_set.all()
        
        #status = appointment.status

    context = {
        'appointment': appointment,
            
    }
    return render(request, 'app/my_appointment.html', context)





