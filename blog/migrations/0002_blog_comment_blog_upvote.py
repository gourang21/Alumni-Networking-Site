# Generated by Django 3.1.1 on 2020-11-02 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_upvote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
                ('upvote_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blog_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('flag', models.CharField(blank=True, choices=[('abusive', 'abusive'), ('inappropriate', 'inappropriate'), ('other', 'other')], max_length=20, null=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
