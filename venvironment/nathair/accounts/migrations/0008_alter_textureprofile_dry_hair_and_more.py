# Generated by Django 4.2.2 on 2023-11-20 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_textureprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textureprofile',
            name='dry_hair',
            field=models.ImageField(blank=True, null=True, upload_to='dry_hair_pics'),
        ),
        migrations.AlterField(
            model_name='textureprofile',
            name='dry_hair_prod',
            field=models.ImageField(blank=True, null=True, upload_to='dry_hair_product_pics'),
        ),
        migrations.AlterField(
            model_name='textureprofile',
            name='wet_hair',
            field=models.ImageField(blank=True, null=True, upload_to='wet_hair_pics'),
        ),
        migrations.AlterField(
            model_name='textureprofile',
            name='wet_hair_prod',
            field=models.ImageField(blank=True, null=True, upload_to='wet_hair_product_pics'),
        ),
    ]
