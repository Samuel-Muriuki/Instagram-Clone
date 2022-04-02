from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.
def homepage(request):
    return render(request, "home.html")

def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registartion successful")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information")
    form = NewUserForm()
    return render (request=request, template_name="ig/register.html", context={"register_form":form})