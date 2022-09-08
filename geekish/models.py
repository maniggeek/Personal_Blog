from django.db import models
from django.urls import reverse
from autoslug import  AutoSlugField

# Create your models here.

#Create a STATUS of Post
STATUS = (
 (0,'draft'),
 (1,'publish')
)

#Creating a class name post with characteristic of a post
#we create a model from the data that we want to store
class Post(models.Model):
#This will store the images in date archives like MEDIA_ROOT/users/2020/04/12
#default png prevent from image error in test
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/',blank=True ,default='default.png')
#title
    title = models.CharField(max_length=200)
    url = models.URLField(blank=False,null=False)
    description = models.CharField(max_length=60,blank=True,null=False);
#create_on
    created_on = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title')

#status
    status = models.IntegerField(choices=STATUS,default=0)

#meta class for ordering

    def Meta(self):
        ordering_on = ['-created_on']
#return title with __str__
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"slug":self.title})


class Paragraph(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='paragraphs')
    header = models.CharField(max_length=200,blank=True,null=False)
    content = models.TextField()

    def __str__(self):
        return self.header
