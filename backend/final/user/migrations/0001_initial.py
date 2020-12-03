# Generated by Django 3.0 on 2019-12-16 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, db_column='userName', max_length=100, null=True)),
                ('password', models.CharField(blank=True, db_column='passWord', max_length=100, null=True)),
            ],
            options={
                'db_table': 'user_info',
                'managed': False,
            },
        ),
    ]
