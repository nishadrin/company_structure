from django_filters import rest_framework as filters

from ..models import Employee


class EmployeeFilter(filters.FilterSet):
    surname = filters.CharFilter(field_name='surname', lookup_expr='icontains')
    department_id = filters.NumberFilter(field_name='department_id')

    class Meta:
        model = Employee
        fields = ['surname', 'department_id']
