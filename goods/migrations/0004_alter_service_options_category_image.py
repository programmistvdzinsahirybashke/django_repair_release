# Generated by Django 5.1.2 on 2024-10-15 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_category_options_alter_category_category_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Услугу', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Изображение'),
        ),
    ]