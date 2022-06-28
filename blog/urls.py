from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),
    path('postlist/', views.postlist, name='postlist'),
    path('postlist/<slug:tag_slug>/', views.postlist, name='postlist_tag'),
    # path('postlist/', views.PostListView.as_view(), name='postlist'),
    path('postdetail/<slug:slug>/<int:pk>',views.postdetail,name='post_detail'),
    path('accountform/', views.useraccount, name='accountform'),
    path('contactus/', views.contactus, name='contactus'),
    path('share/<int:post_id>', views.share, name='share'),

]