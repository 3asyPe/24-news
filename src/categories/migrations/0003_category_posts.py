# Generated by Django 3.2 on 2021-04-28 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_merge_0007_post_category_0007_post_tags'),
        ('categories', '0002_remove_category_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='posts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.post'),
        ),
    ]
