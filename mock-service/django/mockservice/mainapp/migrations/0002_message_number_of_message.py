# Generated by Django 4.1.1 on 2022-10-02 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='number_of_message',
            field=models.IntegerField(default=1),
        ),
    ]