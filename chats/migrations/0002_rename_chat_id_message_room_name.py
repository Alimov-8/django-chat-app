# Generated by Django 3.2.6 on 2021-08-05 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='chat_id',
            new_name='room_name',
        ),
    ]
