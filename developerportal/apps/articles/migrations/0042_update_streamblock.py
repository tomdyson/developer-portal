# Generated by Django 2.2.12 on 2020-05-12 15:54

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0041_add_3_2_ratio_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='authors',
            field=wagtail.core.fields.StreamField([('author', wagtail.core.blocks.PageChooserBlock(page_type=['people.Person'])), ('external_author', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Name')), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='16:9 aspect-ratio image', label='16:9 image')), ('image_3_2', wagtail.images.blocks.ImageChooserBlock(help_text='3:2 aspect-ratio image - optional but recommended', required=False)), ('description', wagtail.core.blocks.CharBlock(label='About', required=False)), ('url', wagtail.core.blocks.URLBlock(label='URL', required=False))]))], blank=True, help_text="Optional list of the post's authors. Use ‘External author’ to add guest authors without creating a profile on the system", null=True),
        ),
    ]
