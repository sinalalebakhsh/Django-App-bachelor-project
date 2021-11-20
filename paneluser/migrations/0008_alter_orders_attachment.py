# Generated by Django 3.2.7 on 2021-11-20 08:43

from django.db import migrations, models
import paneluser.models


class Migration(migrations.Migration):

    dependencies = [
        ('paneluser', '0007_alter_orders_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=paneluser.models.order_file_path, verbose_name='پیوست'),
        ),
    ]
