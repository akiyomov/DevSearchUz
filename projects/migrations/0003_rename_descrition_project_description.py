# Generated by Django 4.0 on 2021-12-23 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tag_project_vote_ratio_project_vote_total_review_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='descrition',
            new_name='description',
        ),
    ]
