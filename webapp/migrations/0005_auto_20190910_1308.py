# Generated by Django 2.2.5 on 2019-09-10 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("webapp", "0004_auto_20190910_1307")]

    operations = [
        migrations.AlterModelOptions(
            name="category", options={"verbose_name_plural": "Category"}
        ),
        migrations.AlterModelOptions(
            name="laptops", options={"verbose_name_plural": "Laptops"}
        ),
    ]
