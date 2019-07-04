from django.contrib import admin
from .models import  Employee
# Register your models here.

class EmployeeModelAdmin(admin.ModelAdmin):
	list_display = ['__str__','designation','manager']
	class Meta:
		model = Employee

admin.site.register(Employee,EmployeeModelAdmin)