# Generated by Django 5.0.2 on 2024-03-15 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookdetails',
            fields=[
                ('bookid', models.IntegerField(primary_key=True, serialize=False)),
                ('bookname', models.CharField(max_length=25)),
                ('author', models.CharField(max_length=20)),
                ('publishedyear', models.DateField()),
                ('price', models.IntegerField()),
                ('publishedcompany', models.CharField(max_length=20)),
            ],
        ),
    ]
