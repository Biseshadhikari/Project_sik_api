# Generated by Django 3.2.21 on 2023-09-26 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_lesson_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonvideo',
            name='Course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.course'),
        ),
    ]
