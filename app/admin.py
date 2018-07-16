from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import User_Profile, Post, Comment
# Register your models here.

class User_in_line(admin.StackedInline):
    model = User_Profile
    can_delete = False
    verbose_name_plural = "Informations"


class UserAdmin(UserAdmin):
    inlines = (User_in_line,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Post)
admin.site.register(Comment)
