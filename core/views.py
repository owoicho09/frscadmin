from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import APIException
import logging
from .models import Unit,Employee
from .serializers import UnitSerializer,EmployeeSerializer
from rest_framework.generics import RetrieveAPIView




logger = logging.getLogger(__name__)



# ✅ Create Unit (POST /api/units/)
class UnitCreateView(generics.CreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"UnitCreateView.create Exception: {str(e)}")
            return Response({"error": "Unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UnitListView(generics.ListAPIView):
    serializer_class = UnitSerializer

    def get_queryset(self):
        try:
            return Unit.objects.all()
        except Unit.DoesNotExist:
            raise APIException("No Unit found.")
        except Exception as e:
            logger.error(f"UnitListView.get_queryset Exception: {str(e)}")
            raise APIException("Database error occurred while fetching units.")

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except APIException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(f"UnitListView.list Exception: {str(e)}")
            return Response({"error": "Unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class EmployeeListByUnitView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        unit_id = self.kwargs.get('unit_id')
        try:
            unit = Unit.objects.get(id=unit_id)
            return Employee.objects.filter(unit=unit)
        except Employee.DoesNotExist:
            raise APIException("No employees found for this unit.")
        except Exception as e:
            logger.error(f"EmployeeListByUnitView.get_queryset Exception: {str(e)}")
            raise APIException("Database error occurred while fetching employees.")

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except APIException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(f"EmployeeListByUnitView.list Exception: {str(e)}")
            return Response({"error": "Unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





class EmployeeDetailView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'employee_id'

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"EmployeeDetailView.retrieve Exception: {str(e)}")
            return Response({"error": "Unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EmployeeFormView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"EmployeeFormView.create Exception: {str(e)}")
            return Response(
                {"error": "Failed to create employee."},
                status=status.HTTP_400_BAD_REQUEST
            )
