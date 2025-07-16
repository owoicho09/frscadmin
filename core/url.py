from django.urls import path
from .views import (
    UnitCreateView,
    UnitListView,
    EmployeeFormView,
    EmployeeListByUnitView,
    EmployeeDetailView,

)

urlpatterns = [
    path('units/create/', UnitCreateView.as_view()),
    path('units/', UnitListView.as_view()),
    path('employees/', EmployeeFormView.as_view()),
    path('units/<str:unit_id>/employees/', EmployeeListByUnitView.as_view()),
    path('employees/<str:employee_id>/', EmployeeDetailView.as_view()),
]
