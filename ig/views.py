from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Post, Profile, Comment, Like
from .forms import ProfileUpdateForm, UserUpdateForm, NewPostForm, CommentForm

# Create your views here.

@login_required(login_url='login/')
def homepage(request):
    posts = Post.all_posts()
    json_posts = []
    profiles = Profile.objects.all()
    current_user = request.user

    comments = Comment.objects.all()
    likes = Like.objects.all()
    for post in posts:                                                            
        num_likes = 0
        for like in likes:
            if post.id == like.post.id:
                num_likes +=1
        post.likes = num_likes
        post.save()
        pic = Profile.objects.filter(username=post.user.id).first()
        if pic:
            pic = pic.picture.url
        else:
            pic = ''
        obj = dict(
            image=post.image.url,
            author=post.user.username,
            avatar=pic,
            name=post.title,
            caption=post.caption

        )
        json_posts.append(obj)
        
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = int(request.POST.get("idpost"))
            post = Post.objects.get(id = post_id)
            comment = form.save(commit=False)
            comment.username = request.user
            comment.post = post
            comment.save()
        return redirect('homepage')

    else:
        form = CommentForm()

    
    likes = Like.objects.all()
    
    return render(request, 'home.html', {"posts": json_posts, "likes":likes, "comments":comments, "profiles":profiles,"current_user":current_user,})

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
	return redirect("login")

@login_required
def profile(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user)

        if  profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('homepage')

    else:
        
        profile_form = ProfileUpdateForm(instance=request.user)
        user_form = UserUpdateForm(instance=request.user)

        context = {
            'user_form':user_form,
            'profile_form': profile_form

        }

    return render(request, 'ig/profile.html', context)

def post(request):
    current_user = request.user
   
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
           
            image.save()
            
        return redirect('homepage')

    else:
        form = NewPostForm()
    return render(request, 'ig/post.html', {"form": form})

@login_required
def edit_profile(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('homepage')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user)

        context = {
            'user_form': user_form,
            'profile_form': profile_form

        }

    return render(request, 'ig/edit_profile.html', context)