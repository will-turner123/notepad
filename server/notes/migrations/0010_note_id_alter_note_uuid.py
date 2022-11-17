# Generated by Django 4.0.3 on 2022-11-16 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0009_alter_note_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='uuid',
            field=models.TextField(default='f1554dc6', editable=False, max_length=8),
        ),
    ]
