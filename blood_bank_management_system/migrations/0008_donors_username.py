# Generated by Django 4.0 on 2021-12-27 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_bank_management_system', '0007_remove_donors_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='donors',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
