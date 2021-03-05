
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


from .models.user import User
from .models.profile import Profile

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
