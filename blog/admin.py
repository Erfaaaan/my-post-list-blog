from django.contrib import admin
from .models import Post,account,comment

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'publish' , 'created', 'author')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author' ,)
    date_hierarchy = 'publish'
    ordering = ('status','publish')
    list_editable = ('status',)
    list_display_links = ('slug',)

@admin.register(account)
class accountAdmin(admin.ModelAdmin):
    list_display = ('phone','user','sex','address','age')

@admin.register(comment)
class commentAdmin(admin.ModelAdmin):
    list_display = ('name','body','post','created','active')
    list_filter = ('active','created','updated')
    list_editable = ('active',)