# Generated by Django 5.0.4 on 2024-05-02 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_rename_user_user_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='user_email',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]