# Generated by Django 3.2.4 on 2021-06-11 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='idol_Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupName', models.CharField(max_length=200)),
                ('members', models.IntegerField()),
                ('isfemale', models.BooleanField()),
            ],
        ),
    ]