# Generated by Django 4.0.3 on 2023-11-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_qanda_video_qanda_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.CharField(default='English', max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('ongoing', 'ongoing'), ('Completed', 'Completed')], default='ongoing', max_length=200),
        ),
    ]
