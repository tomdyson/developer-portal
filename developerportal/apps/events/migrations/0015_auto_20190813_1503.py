# Generated by Django 2.2.4 on 2019-08-13 15:03

import developerportal.apps.common.fields
from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_auto_20190813_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='agenda',
            field=wagtail.core.fields.StreamField([('agenda_item', wagtail.core.blocks.StructBlock([('start_time', wagtail.core.blocks.TimeBlock()), ('end_time', wagtail.core.blocks.TimeBlock(required=False)), ('title', wagtail.core.blocks.CharBlock()), ('speaker', wagtail.core.blocks.PageChooserBlock(page_type=['people.Person'], required=False)), ('external_speaker', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.URLBlock(label='URL', required=False))]))]))], blank=True, help_text='Optional list of agenda items for this event', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='body',
            field=developerportal.apps.common.fields.CustomStreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=('h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul', 'blockquote', 'code', 'hr'))), ('image', wagtail.images.blocks.ImageChooserBlock()), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock()), ('page_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(help_text='External URL to link to instead of a page.', required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('embed_html', wagtail.core.blocks.RawHTMLBlock(help_text='Warning: be careful what you paste here, since this field could introduce XSS (or similar) bugs. This field is meant solely for third-party embeds.')), ('code_snippet', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('css', 'CSS'), ('go', 'Go'), ('html', 'HTML'), ('js', 'JavaScript'), ('python', 'Python'), ('rust', 'Rust'), ('ts', 'TypeScript')])), ('code', wagtail.core.blocks.TextBlock())]))], blank=True, default=None, help_text='Optional body content. Supports rich text, images, embed via URL, embed via HTML, and inline code snippets', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, default='', help_text='Optional short text description, max. 400 characters', max_length=400),
        ),
        migrations.AlterField(
            model_name='event',
            name='speakers',
            field=wagtail.core.fields.StreamField([('speaker', wagtail.core.blocks.PageChooserBlock(page_type=['people.Person'], required=False)), ('external_speaker', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Name')), ('job_title', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('url', wagtail.core.blocks.URLBlock(label='URL', required=False))], required=False))], blank=True, help_text='Optional list of speakers for this event', null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='featured',
            field=wagtail.core.fields.StreamField([('event', wagtail.core.blocks.PageChooserBlock(page_type=['events.Event', 'externalcontent.ExternalEvent'], required=False)), ('external_page', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock()), ('title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.TextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock())]))], blank=True, help_text='Optional space to show a featured event', null=True),
        ),
    ]