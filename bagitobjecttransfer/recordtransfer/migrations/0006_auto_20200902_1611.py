# Generated by Django 3.0.4 on 2020-09-02 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recordtransfer', '0005_bag_review_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bag',
            old_name='bag_location',
            new_name='bag_name',
        ),
        migrations.RenameField(
            model_name='bag',
            old_name='report_location',
            new_name='report_name',
        ),
    ]