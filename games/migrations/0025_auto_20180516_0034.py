# Generated by Django 2.0.5 on 2018-05-15 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0024_auto_20180515_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featured',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]
