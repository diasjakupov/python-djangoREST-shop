# Generated by Django 3.0.8 on 2020-08-30 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0003_auto_20200827_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardproduct',
            name='total_price',
            field=models.FloatField(default=0, max_length=4, null=True),
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='restAPI.Category'),
        ),
    ]