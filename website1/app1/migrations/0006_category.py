# Generated by Django 5.0.1 on 2024-05-20 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=255)),
                ('cat_image', models.FileField(null=True, upload_to='category')),
            ],
        ),
    ]
