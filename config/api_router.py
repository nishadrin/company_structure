from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from company_structure.users.api.views import UserViewSet
from company_structure.employees.api.views import EmployeeViewSet
from company_structure.departments.api.views import DepartmentViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("employees", EmployeeViewSet)
router.register("departments", DepartmentViewSet)


app_name = "api"
urlpatterns = router.urls
