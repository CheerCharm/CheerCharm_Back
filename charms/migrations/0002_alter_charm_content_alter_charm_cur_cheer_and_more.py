# Generated by Django 4.1.5 on 2023-01-10 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charm',
            name='content',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='charm',
            name='cur_cheer',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='응원수'),
        ),
        migrations.AlterField(
            model_name='charm',
            name='deleted_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='charm',
            name='image',
            field=models.IntegerField(blank=True, choices=[(1, 'Mouse'), (2, 'Goat'), (3, 'Squirrel'), (4, 'Monkey'), (5, 'Bird')], null=True),
        ),
        migrations.AlterField(
            model_name='charm',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='charm',
            name='total_cheer',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
