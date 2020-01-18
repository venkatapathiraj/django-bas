# Generated by Django 2.2.8 on 2019-12-11 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0005_cart_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='slug',
        ),
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]