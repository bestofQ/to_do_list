# Generated by Django 3.0 on 2020-02-04 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thing', models.CharField(max_length=50)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
