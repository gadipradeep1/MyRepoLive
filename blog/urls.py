from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView


urlpatterns = [
    path('', PostListView.as_view() ,name='blog-home'), #default post_list.html, but template_name is given in model
    path('user/<str:username>', UserPostListView.as_view() ,name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view() ,name='post-detail'), # default post_detail.html
    path('post/new/', PostCreateView.as_view() ,name='post-create'), #calls post_form.html
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'), #calls post_form.html
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'), #post_confirm_delete.html
    path('about/', views.about,name='blog_about'),
]