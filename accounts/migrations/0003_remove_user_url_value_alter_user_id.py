# Generated by Django 4.1.4 on 2023-01-25 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_email_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='url_value',
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
