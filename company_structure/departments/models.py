from django.db import models


class Department(models.Model):
    """Модель департамента"""

    name = models.CharField(max_length=50, verbose_name='Название', )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    class Meta:
        ordering = ('name', )
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'

    def __str__(self):
        return self.name

    def employee_count(self):
        return self.employees.count()

    def total_salary(self):
        return sum(employee.salary for employee in self.employees.all())
