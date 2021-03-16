from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User

# def home(request):
# 	return render(request,'blog/home.html',{'blog_post':Post.objects.all()})

class PostListView(ListView):
	model=Post
	template_name='blog/home.html'  # <app_name>/<model>_<listType>.html
	context_object_name='blog_post'
	ordering=['-date_posted']
	paginate_by=2

class UserPostListView(ListView):
	model=Post
	template_name='blog/user_posts.html'  
	context_object_name='blog_post'
	paginate_by=2	

	def get_queryset(self):
		user=get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
	model=Post
	fields=['title','content'] #default template page for both create and update is "post_form.html"
	# success_url='/' This will redirect to Home page, if this is not provided it will search for
	# get_absolute_url in Post model

	def form_valid(self,form):
		form.instance.author=self.request.user  #this will provide the authorid without having to explicitly providing by user
		return super().form_valid(form)	

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model=Post
	fields=['title','content'] #default template page for both create and update is "post_form.html"
	# success_url='/' This will redirect to Home page, if this is not provided it will search for
	# get_absolute_url in Post model

	def form_valid(self,form):
		form.instance.author=self.request.user  #this will provide the authorid without having to explicitly providing by user
		return super().form_valid(form)			

	def test_func(self):
		if self.request.user == self.get_object().author:  #if present user is the same user of the post. Only he can update his posts
			return True
		else: return False	

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):	
	model=Post
	success_url='/'

	def test_func(self):
		if self.request.user == self.get_object().author:  #if present user is the same user of the post. Only he can update his posts
			return True
		else: return False	

def about(request):
	return render(request,'blog/about.html',{'title': 'about kikitara'})
