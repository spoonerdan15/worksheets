# Generated by Django 4.0.6 on 2022-07-20 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('order', models.IntegerField()),
                ('price', models.IntegerField()),
                ('date', models.TextField()),
            ],
        ),
    ]
