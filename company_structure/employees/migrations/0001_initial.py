# Generated by Django 5.0.9 on 2024-10-13 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('director', 'Директор'), ('hr', 'HR'), ('developer', 'Разработчик')], max_length=50, verbose_name='Должность')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(db_index=True, max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Фото')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='departments.department', verbose_name='Департамент')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ('surname',),
                'unique_together': {('name', 'surname', 'patronymic', 'birthday', 'department')},
            },
        ),
    ]
