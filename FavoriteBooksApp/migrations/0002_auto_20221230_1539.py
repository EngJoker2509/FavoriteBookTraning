# Generated by Django 3.0 on 2022-12-30 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FavoriteBooksApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='uploaded_by_id',
            new_name='uploaded_by',
        ),
    ]
