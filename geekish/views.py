from django.shortcuts import render
#import ListView to List the Posts
from django.views.generic import ListView
#import DetailView to see more detail

from django.views.generic import DetailView
from django.views.generic import TemplateView
#import reverse_lazy from urls
from django.urls import reverse_lazy

from django.views import View
from .models import Post


from django.urls import reverse



#we have a class that List the Posts is subclass of List View
class HomePageView(ListView):
# queryset = order Post objects in filter of status1 based on negative Cdate
    queryset = Post.objects.filter(status='1').order_by('-created_on')
#our model
    model = Post
#template name
    template_name = 'home.html'
#context_object_name
    context_object_name = 'all_posts'

    paginate_by = 4

class AboutPageView(TemplateView):
    template_name = 'about.html'


class PostDetailView(DetailView):
    
    model = Post
    context_object_name = "post"
    template_name = "post_detail.html"
