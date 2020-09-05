# Generated by Django 3.0.8 on 2020-09-05 11:37

from django.db import migrations, models
import django.db.models.deletion
import restAPI.models


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0005_category_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='restAPI.Category'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_active',
            field=models.CharField(choices=[('active', 'active'), ('completed', 'completed'), ('preparation', 'preparation')], default='active', max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('deliver', 'deliver'), ('pickup', 'pickup')], default='deliver', max_length=200),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=restAPI.models.foldername)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='restAPI.Product')),
            ],
        ),
    ]
