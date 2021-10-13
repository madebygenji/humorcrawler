# Generated by Django 2.2.4 on 2021-10-12 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='abcd', unique=True),
            preserve_default=False,
        ),
    ]
