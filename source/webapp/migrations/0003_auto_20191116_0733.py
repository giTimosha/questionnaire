# Generated by Django 2.2.7 on 2019-11-16 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20191116_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='assessment',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, verbose_name='оценка'),
        ),
    ]