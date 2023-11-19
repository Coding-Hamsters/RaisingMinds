from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('email','username','date_joined','is_active','is_staff','is_superuser')
    search_fields = ('email','username',)
    readonly_fields = ('date_joined',)
    list_filter = ('date_joined',)
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes':('wide'),
            'fields':('email','username','password1','password2'),
        }),
    )
    


    ordering = ('date_joined',)
admin.site.register(User,CustomUserAdmin)
