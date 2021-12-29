# Generated by Django 4.0 on 2021-12-27 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_bank_management_system', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.RemoveField(
            model_name='donors',
            name='password',
        ),
        migrations.AddField(
            model_name='donors',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='donors',
            name='blood_group',
            field=models.CharField(choices=[('o_positive', 'O+'), ('a_positive', 'A+'), ('o_negative', 'O-'), ('b_positive', 'B+'), ('a_negative', 'A-'), ('ab_positive', 'AB+'), ('b_negative', 'B-'), ('ab_negative', 'AB-')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='donors',
            name='email',
            field=models.CharField(max_length=120, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='donors',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Prefer not to say')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='donors',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='donors',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]