# Generated by Django 2.2.10 on 2021-10-21 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20211021_0818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quests',
            name='user_noauth',
        ),
        migrations.AlterField(
            model_name='quests',
            name='user_auth',
            field=models.IntegerField(null=True, verbose_name='Id пользователя'),
        ),
    ]
