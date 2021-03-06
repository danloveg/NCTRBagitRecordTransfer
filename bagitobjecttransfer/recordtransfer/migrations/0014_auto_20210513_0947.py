# Generated by Django 3.1.8 on 2021-05-13 14:47

from django.db import migrations, models
import recordtransfer.storage


def initial_rights(apps, schema_editor):
    right_model = apps.get_model('recordtransfer', 'Right')
    other_right = right_model()
    other_right.name = "Other"
    other_right.description = "Placeholder right to allow user to specify unique rights"
    other_right.save()


class Migration(migrations.Migration):

    dependencies = [
        ('recordtransfer', '0013_auto_20210428_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Right',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='attached_file',
            field=models.FileField(blank=True, null=True, storage=recordtransfer.storage.OverwriteStorage, upload_to='jobs/zipped_bags'),
        ),
        migrations.RunPython(initial_rights),
    ]
