# Generated by Django 4.0.3 on 2022-11-16 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_alter_note_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='id',
        ),
        migrations.AlterField(
            model_name='note',
            name='uuid',
            field=models.TextField(default='82ac89aa', editable=False, primary_key=True, serialize=False),
        ),
    ]
