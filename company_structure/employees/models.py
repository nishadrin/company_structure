from datetime import date

from django.db import models


class Employee(models.Model):
    """Модель сотрудника"""

    DAYS_IN_YEAR = 365
    POSITION_NAME = [
        ('director', 'Директор'),
        ('hr', 'HR'),
        ('developer', 'Разработчик')
    ]

    position = models.CharField(
        choices=POSITION_NAME,
        max_length=50,
        verbose_name='Должность',
    )
    name = models.CharField(max_length=50, verbose_name='Имя', )
    surname = models.CharField(
        max_length=50,
        verbose_name='Фамилия',
        db_index = True,
    )
    patronymic = models.CharField(max_length=50, verbose_name='Отчество', )
    birthday = models.DateField(verbose_name='Дата рождения', )
    salary = models.DecimalField(max_digits=10, decimal_places=2, )
    photo = models.ImageField(
        upload_to="media",
        null=True,
        blank=True,
        verbose_name='Фото',
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    department = models.ForeignKey(
        'departments.Department',
        verbose_name='Департамент',
        on_delete=models.CASCADE,
        related_name='employees'
    )

    class Meta:
        ordering = ('surname', )
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        unique_together = (
            'name',
            'surname',
            'patronymic',
            'birthday',
            'department',
        )

    def __str__(self):
        return f"{self.fio} {self.age}"

    @property
    def fio(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    @property
    def age(self):
        return str(int((date.today() - self.birthday).days / self.DAYS_IN_YEAR))
