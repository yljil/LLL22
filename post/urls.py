from post import views
from django.urls import path
urlpatterns = [
    path("index/", views.IndexView.as_view()),
    path("post/<int:num>/", views.IndexView.as_view(), name="page_view"),
    path("posts/<int:postid>/",views.DetailView.as_view()),
    path("category/<int:cid>/",views.getPostByCid,name='category'),
    path("archive/<int:year>/<int:month>/",views.getPostByCreated),
    path("archive/",views.getPostByCreated),

]