from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Post, Profile

# Create your views here.

@login_required(login_url='login/')
def homepage(request):
    posts = Post.all_posts()
    json_posts = []
    for post in posts:

        # import pdb; pdb.set_trace()
        pic = Profile.objects.filter(user=post.user.id).first()
        if pic:
            pic = pic.profile_pic.url
        else:
            pic =''
        obj = dict(
            image=post.image.url,
            author=post.user.username,
            avatar=pic,
            name=post.title,
            caption=post.caption

        )
        json_posts.append(obj)
    return render(request, 'home.html', {"posts": json_posts})

def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registartion successful")
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information")
    form = NewUserForm()
    return render (request=request, template_name="ig/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="ig/login.html", context={"login_form": form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("homepage")