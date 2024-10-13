from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination

from ..models import Employee
from .serializers import EmployeeSerializer
from .filters import EmployeeFilter


class EmployeePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    pagination_class = EmployeePagination
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = EmployeeFilter
