# Generated by Django 2.1.5 on 2019-01-16 13:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0003_auto_20190116_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(default=1, on_delete=0, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
