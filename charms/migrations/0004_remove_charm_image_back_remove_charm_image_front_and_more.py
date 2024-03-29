# Generated by Django 4.1.4 on 2023-02-03 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charms', '0003_charm_image_back_charm_image_front'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charm',
            name='image_back',
        ),
        migrations.RemoveField(
            model_name='charm',
            name='image_front',
        ),
        migrations.CreateModel(
            name='CharmImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('img_front', models.URLField()),
                ('img_back', models.URLField()),
                ('charm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='charm_image', to='charms.charm')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
