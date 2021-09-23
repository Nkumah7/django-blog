from django.urls import path

from . import views


urlpatterns = [
    # path("", views.starting_page, name="starting-page"), # Function based view for Starting Page
    path("", views.StartingPageView.as_view(), name="starting-page"), # Class based view for Starting Page
    # path("posts/", views.posts, name="posts-page"), # Function based view for All Posts Page
    path("posts/", views.AllPostsView.as_view(), name="posts-page"), # Class based view for All Posts Page
    # path("posts/<slug:slug>", views.post_detail,
    #      name="post-detail-page"), #/posts/my-first-post # Function based view for Single Post Page
    path("posts/<slug:slug>", views.SinglePostView.as_view(),
         name="post-detail-page"), #/posts/my-first-post # Class based view for Single Post Page
]