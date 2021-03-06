# Generated by Django 3.0.3 on 2020-04-13 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stutable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True, verbose_name='用户名')),
                ('email', models.CharField(max_length=64, unique=True, verbose_name='邮箱')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='出生年月')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女'), ('unknown', '未知')], default='unknown', max_length=8, verbose_name='性别')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='电话')),
                ('password_hash', models.CharField(blank=True, max_length=128, null=True, verbose_name='密码')),
                ('head_img', models.ImageField(null=True, upload_to='img/%Y/%m/%d', verbose_name='头像')),
                ('create_time', models.DateTimeField(blank=True, null=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
    ]
