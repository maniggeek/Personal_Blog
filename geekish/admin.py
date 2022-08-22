from django.contrib import admin

# Register your models here.
#import model from models
from .models import Post


#creating a class PostAdmin that subclass of admin.ModelAdmin
class PostAdmin(admin.ModelAdmin):
#create list_display and list list_filter
    list_display = ('status','title',
    'paragraph_1','paragraph_2','paragraph_3','paragraph_4',
    'p_topic_1','p_topic_2','p_topic_3','p_topic_4',
    'image','description','created_on',)
    list_filter = ('status',)


admin.site.register(Post,PostAdmin)
