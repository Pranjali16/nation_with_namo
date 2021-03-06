# Generated by Django 2.2.16 on 2020-09-16 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgateway_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='card_type',
            field=models.CharField(choices=[('creditcard', 'creditcard'), ('debitcard', 'debitcard')], default='creditcard', max_length=255),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('success', 'success'), ('failed', 'failed'), ('in-progress', 'In-Progress')], default='success', max_length=1),
        ),
    ]
