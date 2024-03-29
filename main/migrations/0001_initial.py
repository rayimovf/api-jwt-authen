# Generated by Django 5.0 on 2024-01-27 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=5)),
                ('information', models.TextField()),
            ],
        ),
    ]
