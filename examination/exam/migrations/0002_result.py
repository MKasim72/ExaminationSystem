# Generated by Django 3.0.5 on 2024-08-20 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.StudentProfile')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.addSubject')),
            ],
        ),
    ]