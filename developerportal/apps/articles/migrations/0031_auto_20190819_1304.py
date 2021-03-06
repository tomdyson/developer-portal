# Generated by Django 2.2.4 on 2019-08-19 13:04

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [("articles", "0030_auto_20190813_1503")]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="description",
            field=wagtail.core.fields.RichTextField(
                blank=True,
                default="",
                help_text="Optional short text description, max. 400 characters",
                max_length=400,
            ),
        ),
        migrations.AlterField(
            model_name="articles",
            name="description",
            field=wagtail.core.fields.RichTextField(
                blank=True,
                default="",
                help_text="Optional short text description, max. 400 characters",
                max_length=400,
            ),
        ),
    ]
