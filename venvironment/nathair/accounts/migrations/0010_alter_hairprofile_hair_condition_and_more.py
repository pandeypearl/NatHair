# Generated by Django 4.2.2 on 2023-11-20 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_textureprofile_dry_hair_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hairprofile',
            name='hair_condition',
            field=models.CharField(choices=[('Protein Overload', 'Protein Overload'), ('Moisture Overload', 'Moisture Overload'), ('Healthy', 'Healthy'), ('Dandruff', 'Dandruff'), ('Hair Loss', 'Hair Loss'), ('Dry Hair', 'Dry Hair'), ('Split Ends', 'Split Ends'), ('Greasy Hair', 'Greasy Hair'), ('Frizzy', 'Frizzy'), ('Heat Damage', 'Heat Damage'), ('Color Damage', 'Color Damage')], max_length=20),
        ),
        migrations.AlterField(
            model_name='hairprofile',
            name='hair_length',
            field=models.CharField(choices=[('Ear Length', 'Ear Length'), ('Neck (top) Length', 'Neck (top) Length'), ('Neck (bottom) Length', 'Neck (bottom) Length'), ('Collarbone Length', 'Collarbone Length'), ('Shoulder Length', 'Shoulder Length'), ('Armpit Length', 'Armpit Length'), ('Bra Strap Length', 'Bra Strap Length'), ('Mid Back Length', 'Mid Back Length'), ('Waist Length', 'Waist Length'), ('Hip Length', 'Hip Length'), ('Tailbone Length', 'Tailbone Length'), ('Classic Length', 'Classic Length'), ('Mid Thigh Length', 'Mid Thigh Length'), ('Knee Length', 'Knee Length'), ('Calf Length', 'Calf Length'), ('Ankle Length', 'Ankle Length'), ('Floor Length', 'Floor Length')], max_length=20),
        ),
        migrations.AlterField(
            model_name='hairprofile',
            name='hair_porosity',
            field=models.CharField(choices=[('Low Porosity', 'Low Porosity'), ('Medium Porosity', 'Medium Porosity'), ('Hight Porosity', 'Hight Porosity')], max_length=20),
        ),
        migrations.AlterField(
            model_name='hairprofile',
            name='hair_type',
            field=models.CharField(choices=[('1a', '1a'), ('1b', '1b'), ('1c', '1c'), ('2a', '2a'), ('2b', '2b'), ('2c', '2c'), ('3a', '3a'), ('3b', '3b'), ('3c', '3c'), ('4a', '4a'), ('4b', '4b'), ('4c', '4c')], max_length=2),
        ),
    ]
