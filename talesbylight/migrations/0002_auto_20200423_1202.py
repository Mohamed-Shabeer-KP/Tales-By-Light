# Generated by Django 3.0.5 on 2020-04-23 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talesbylight', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votedata',
            name='v_img_no',
            field=models.IntegerField(max_length=50, verbose_name='image_number'),
        ),
    ]