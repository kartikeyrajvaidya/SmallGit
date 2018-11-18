# Generated by Django 2.1.2 on 2018-11-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('search_category', models.CharField(max_length=200)),
                ('search_query', models.CharField(max_length=200)),
            ],
        ),
    ]
