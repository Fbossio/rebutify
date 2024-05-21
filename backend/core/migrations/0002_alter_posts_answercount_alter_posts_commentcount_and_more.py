# Generated by Django 5.0.4 on 2024-05-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="answerCount",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="posts",
            name="commentCount",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="posts",
            name="favoriteCount",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="posts",
            name="score",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="posts",
            name="viewcount",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="tags",
            name="count",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="tags",
            name="isModeratorOnly",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="tags",
            name="isRequired",
            field=models.BooleanField(default=False),
        ),
    ]
