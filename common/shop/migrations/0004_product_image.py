# Generated by Django 4.2.6 on 2023-12-02 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/default_img.jpg', upload_to='images/'),
        ),
    ]