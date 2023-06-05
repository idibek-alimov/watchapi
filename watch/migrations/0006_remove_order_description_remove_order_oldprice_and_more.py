# Generated by Django 4.0.10 on 2023-05-12 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0005_remove_product_description_remove_product_img_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='description',
        ),
        migrations.RemoveField(
            model_name='order',
            name='oldPrice',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='hello', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default='hello', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='product',
            name='oldPrice',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
    ]