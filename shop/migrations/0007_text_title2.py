# Generated by Django 2.0.5 on 2018-08-19 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_price2'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='title2',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
