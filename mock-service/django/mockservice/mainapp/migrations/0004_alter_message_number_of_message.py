# Generated by Django 4.1.1 on 2022-10-02 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_message_number_of_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='number_of_message',
            field=models.IntegerField(editable=False),
        ),
    ]
