# Generated by Django 3.0.4 on 2020-03-31 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionbank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_description',
            field=models.TextField(max_length=10000, verbose_name="Question's Description"),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_number',
            field=models.FloatField(unique=True, verbose_name="Question's Number"),
        ),
    ]
