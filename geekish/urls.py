from django.urls import path

from .views import HomePageView
from .views import PostDetailView
from .views import AboutPageView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('post/<slug:slug>',PostDetailView.as_view(),name='post_detail'),
]
