# Generated by Django 5.1.1 on 2024-09-22 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_rename_attributevalue_productattributevalue_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='productattributevalue',
            name='attribute',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_attributes', to='product.attribute'),
        ),
        migrations.AddField(
            model_name='productattributevalue',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_attributes', to='product.product'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default=None, upload_to='product'),
        ),
        migrations.AlterField(
            model_name='productattributevalue',
            name='value',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_attributes', to='product.value'),
        ),
        migrations.DeleteModel(
            name='ProductAttribute',
        ),
    ]
