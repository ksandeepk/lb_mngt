# Generated by Django 2.2.1 on 2019-07-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='branch',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
