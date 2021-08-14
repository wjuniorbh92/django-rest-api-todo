from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'author')

# Register your models here.

admin.site.register(Todo, TodoAdmin)