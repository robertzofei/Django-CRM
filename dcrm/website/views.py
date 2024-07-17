
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def home(request):
	# check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# authenticate
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login (request, user)
			messages.success(request, "You Have Been Victoriously Logged In!")
			return redirect('home')
		else:
			messages.success(request, "Incorrect Username or Password, Please Try Again...")
			return redirect('home')
	else:
		return render(request, 'home.html', {})



def logout_user(request):
	logout(request)
	messages.success(request, "You have Been Strongly Logged out.")
	return redirect('home')

def register_user(request):
	return render(request, 'register.html', {})