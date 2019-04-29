# Generated by Django 2.0.5 on 2019-04-22 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0005_auto_20190422_2024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tblblog',
            options={'managed': True},
        ),
        migrations.AddField(
            model_name='tblblog',
            name='blog_added_by',
            field=models.ForeignKey(db_column='blog_added_by', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tblblog',
            name='blog_keyword',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tblblog',
            name='blog_pics',
            field=models.FileField(blank=True, null=True, upload_to='blog/'),
        ),
        migrations.AddField(
            model_name='tblblog',
            name='blog_publish',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.TblPublish'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tblblog',
            name='url',
            field=models.SlugField(blank=True, max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='tblblog',
            name='blog_content',
            field=tinymce.models.HTMLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tblblog',
            name='blog_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='tblblog',
            name='blog_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tblblog',
            name='blog_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
