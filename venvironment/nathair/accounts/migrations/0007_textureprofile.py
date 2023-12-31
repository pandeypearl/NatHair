# Generated by Django 4.2.2 on 2023-11-20 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0006_alter_hairprofile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextureProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wet_hair', models.ImageField(upload_to='wet_hair_pics')),
                ('dry_hair', models.ImageField(upload_to='dry_hair_pics')),
                ('wet_hair_prod', models.ImageField(upload_to='wet_hair_product_pics')),
                ('dry_hair_prod', models.ImageField(upload_to='dry_hair_product_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
