# Generated by Django 3.0.8 on 2020-10-13 12:50

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import restAPI.models


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0004_auto_20200925_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='level',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='lft',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='rght',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to=restAPI.models.foldername),
        ),
        migrations.AlterField(
            model_name='review',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='restAPI.Review'),
        ),
    ]
