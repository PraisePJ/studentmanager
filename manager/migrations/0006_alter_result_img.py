# Generated by Django 4.1.4 on 2023-09-03 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_alter_project_body_alter_project_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='img',
            field=models.ImageField(null=True, upload_to='images/results'),
        ),
    ]