# Generated by Django 4.1.1 on 2022-09-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.TextField(),
        ),
    ]
