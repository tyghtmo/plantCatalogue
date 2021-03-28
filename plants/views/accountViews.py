from django.shortcuts import render, redirect
from django.conf import settings
from plants.forms import accountForms
from django.contrib.auth import login, logout
from django.contrib import messages

#region Profile
def logoutUser(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

def profile(request):
    # <request> Django state
    # <return> profile.html if user is authenticated otherwise sends to login.html

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    
    return render(request, 'account/profile.html')

def register(request):
    # <request> Django state
    # <return> register.html if user is not authenticated otherwise sends to profile.html
	if request.method == "POST":
		form = accountForms.NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("profile")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = accountForms.NewUserForm
	return render (request=request, template_name="registration/register.html", context={"register_form":form})
#endregion