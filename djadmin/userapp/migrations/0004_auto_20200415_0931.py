# Generated by Django 3.0.3 on 2020-04-15 01:31

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_auto_20200414_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stutable',
            name='head_img',
            field=stdimage.models.StdImageField(null=True, upload_to='path/to', verbose_name='头像'),
        ),
    ]
