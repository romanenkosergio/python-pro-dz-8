# Generated by Django 4.2.1 on 2023-05-04 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('students', models.ManyToManyField(related_name='groups', to='students.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher')),
            ],
        ),
    ]
