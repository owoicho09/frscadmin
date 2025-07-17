from django.contrib import admin

# Register your models here.


# core/admin.py
from .models import Unit, Employee

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_id')
    search_fields = ('name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'employee_id', 'unit', 'command', 'email', 'created_at')
    list_filter = ('unit', 'created_at')
    search_fields = ('first_name', 'email', 'phone')
