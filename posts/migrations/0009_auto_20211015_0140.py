# Generated by Django 2.2.4 on 2021-10-14 16:40

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_tag_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
