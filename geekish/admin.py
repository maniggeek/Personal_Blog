from django.contrib import admin

# Register your models here.
#import model from models
from .models import Post
from .models import Paragraph


class ParagraphInline(admin.StackedInline):
    model = Paragraph
    can_delete= False

#creating a class PostAdmin that subclass of admin.ModelAdmin
class PostAdmin(admin.ModelAdmin):
#create list_display and list list_filter
    list_display = ('status','title',)
    list_filter = ('status',)
    inlines = [ParagraphInline]





admin.site.register(Post,PostAdmin)
admin.site.register(Paragraph)
