# Generated by Django 2.2.6 on 2022-12-16 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_procurement', '0002_auto_20221216_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contractor',
            field=models.ManyToManyField(related_name='contract', to='public_procurement.TheContractor'),
        ),
    ]
