# Generated by Django 3.0.8 on 2020-07-14 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-modify_dt',), 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
    ]
