# Generated by Django 2.2.1 on 2019-07-31 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20190730_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='reg_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]