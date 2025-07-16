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
    list_display = ('name', 'employee_id', 'unit', 'section', 'email', 'created_at')
    list_filter = ('unit', 'created_at')
    search_fields = ('name', 'email', 'phone')
