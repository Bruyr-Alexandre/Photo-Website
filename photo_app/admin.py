from django.contrib import admin
from .models import User, Photo

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name')

@admin.register(Photo)
class Photo(admin.ModelAdmin):
    list_display = ('creator', 'id')
    search_fields = ('id')