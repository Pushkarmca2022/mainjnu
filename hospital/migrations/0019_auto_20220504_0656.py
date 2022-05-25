# Generated by Django 3.2 on 2022-05-04 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientdischargedetails',
            name='OtherCharge',
        ),
        migrations.RemoveField(
            model_name='patientdischargedetails',
            name='doctorFee',
        ),
        migrations.RemoveField(
            model_name='patientdischargedetails',
            name='medicineCost',
        ),
        migrations.RemoveField(
            model_name='patientdischargedetails',
            name='roomCharge',
        ),
        migrations.RemoveField(
            model_name='patientdischargedetails',
            name='total',
        ),
        migrations.AddField(
            model_name='patientdischargedetails',
            name='Medicine',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
