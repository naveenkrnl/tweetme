# Generated by Django 2.1.5 on 2019-01-27 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_auto_20190126_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, to='tweets.Tweet'),
        ),
    ]