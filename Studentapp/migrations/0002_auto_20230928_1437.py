# Generated by Django 3.2 on 2023-09-28 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Studentapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('last', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('adress', models.CharField(default=True, max_length=255)),
                ('zipcode', models.CharField(max_length=8)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]