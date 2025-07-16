from rest_framework import serializers
from .models import Unit, Employee



class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'employee_id', 'name', 'section', 'email', 'phone', 'created_at', 'unit']

        depth = 0
    def to_representation(self, instance):
        request = self.context.get("request")
        # Adjust depth dynamically
        depth = 0 if request and request.method == "POST" else 0
        serializer = self.__class__(instance, context=self.context)  # Create a new instance
        serializer.Meta.depth = depth
        return super(EmployeeSerializer, serializer).to_representation(instance)


class UnitSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)  # 👈 related_name='employees' in model

    class Meta:
        model = Unit
        fields = ['id', 'name', 'unit_id','employees']

        depth = 0

    def to_representation(self, instance):
        request = self.context.get("request")
        # Adjust depth dynamica11lly
        depth = 0 if request and request.method == "POST" else 0
        serializer = self.__class__(instance, context=self.context)  # Create a new instance
        serializer.Meta.depth = depth
        return super(UnitSerializer, serializer).to_representation(instance)



