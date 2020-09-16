# Generated by Django 2.2.16 on 2020-09-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.CharField(default='', max_length=255)),
                ('currency', models.CharField(default='', max_length=255)),
                ('card_type', models.CharField(choices=[('cc', 'creditcard'), ('dc', 'debitcard')], default='cc', max_length=255)),
                ('authorization_code', models.CharField(default='', max_length=255)),
                ('card_number', models.CharField(default='', max_length=1)),
                ('expiration_month', models.CharField(default='', max_length=255)),
                ('expiration_year', models.CharField(default='', max_length=255)),
                ('cvv', models.CharField(default='', max_length=255)),
                ('status', models.CharField(choices=[('s', 'success'), ('f', 'failed'), ('p', 'In-Progress')], default='s', max_length=1)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]