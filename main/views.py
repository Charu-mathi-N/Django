from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import tutorial
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth import views as auth_views
from . import views
from django.db import models
from django.db.models import Model

# Create your views here.

def homepage(request):
	return render(request = request,
				template_name = "main/home.html",
				context = {"tutorial": tutorial.objects.all}
				)

def register(request):

	if request.method == "POST":
		Form = NewUserForm(request.POST)
		if Form.is_valid():
			user = Form.save()
			username = Form.cleaned_data.get('username')
			messages.success(request, f"Successfully Registered: {username}")
			login(request, user)
			return redirect("main:Homepage")
		else:
			for msg in Form.error_messages:
				messages.error(request, f"{msg}: {Form.error_messages[msg]}")
				return render(request = request,
						template_name = "main/register.html",
						context = {"form" : Form})

	Form = NewUserForm
	return render(request = request,
					template_name = "main/register.html",
					context = {"form" : Form})


def login_request(request):
	if request.method == "POST":
		Form = AuthenticationForm(request, data = request.POST)
		if Form.is_valid():
			username = Form.cleaned_data.get('username')
			password = Form.cleaned_data.get('password')
			user = authenticate(username = username, password = password)
			if user is not None:
				messages.success(request, f"Successfully Loggin: {username}")
				login(request, user)
				return redirect("main:Homepage")
			else:
				messages.error(request, "Invalid username or password")
		else:
				messages.error(request, "Invalid username or password")
	Form = AuthenticationForm()
	return render(request, "main/Login.html", {"form": Form})

def logout_request(request):
	logout(request)
	messages.info(request, "Logged out Successfully")
	return redirect("main:Homepage")


def Reset(request):

	if request.method == 'POST':
		Form = models.EmailField(request, data = request.POST)
		if Form.is_valid():
			email = Form.cleaned_data.get('email')
			if email is not None:
				messages.success(request, f"Sending reset link to: {email}")
				return render(request, "main/Reset.html", {'form': Form})
			else:
				messages.error(request, "Invalid email_id")
		else:
			messages.error(request, "Invalid email_id")
	return render(request, 'main/Reset.html')

