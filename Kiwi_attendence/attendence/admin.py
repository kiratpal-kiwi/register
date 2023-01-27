from django.contrib import admin

from attendence.models import RegisterUser


# Register your models here.
@admin.register(RegisterUser)
class RegisterUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'Emp_id', 'FullName', 'Email', 'Password')
