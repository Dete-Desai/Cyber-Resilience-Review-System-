# Generated by Django 2.2.12 on 2020-06-25 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crrs_app', '0010_auto_20200623_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cseformdb',
            name='expertid',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
