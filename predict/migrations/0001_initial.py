# Generated by Django 3.1 on 2020-08-08 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sepal_length', models.FloatField()),
                ('sepal_width', models.FloatField()),
                ('petal_length', models.FloatField()),
                ('petal_width', models.FloatField()),
                ('classification', models.CharField(max_length=30)),
            ],
        ),
    ]
