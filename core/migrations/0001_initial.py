# Generated by Django 2.2 on 2020-08-27 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.IntegerField(blank=True, null=True, verbose_name='Page number')),
                ('pagesize', models.IntegerField(blank=True, null=True, verbose_name='Page Size')),
                ('fromdate', models.DateField(blank=True, null=True, verbose_name='From Date')),
                ('todate', models.DateField(blank=True, null=True, verbose_name='To Date')),
                ('order', models.CharField(choices=[('desc', 'Descending'), ('asc', 'Ascending')], default='desc', max_length=20, verbose_name='Order')),
                ('min_date', models.DateField(blank=True, null=True, verbose_name='Min date')),
                ('max_date', models.DateField(blank=True, null=True, verbose_name='Max date')),
                ('sort', models.CharField(choices=[('activity', 'Activity'), ('votes', 'Votes'), ('creation', 'Creation'), ('relevance', 'Relevance')], default='activity', max_length=20, verbose_name='Sort')),
                ('q', models.TextField(blank=True, verbose_name='')),
                ('accepted', models.BooleanField(blank=True, null=True, verbose_name='accepted')),
                ('answers', models.IntegerField(blank=True, null=True, verbose_name='Number of answers')),
                ('body', models.TextField(blank=True, help_text="text which must appear in returned questions' bodies.")),
                ('closed', models.BooleanField(blank=True, null=True, verbose_name='closed?')),
                ('migated', models.BooleanField(blank=True, null=True, verbose_name='migrated?')),
                ('notice', models.BooleanField(blank=True, null=True, verbose_name='Notice')),
                ('notagged', models.CharField(blank=True, max_length=253, verbose_name='Not tagged')),
                ('tagged', models.CharField(blank=True, max_length=255, verbose_name='Tagged')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('user', models.IntegerField(blank=True, null=True, verbose_name='Id of user')),
                ('url', models.CharField(blank=True, max_length=255, verbose_name='url')),
                ('views', models.IntegerField(blank=True, null=True, verbose_name='Minimum number of views')),
                ('wiki', models.BooleanField(blank=True, null=True, verbose_name='wiki')),
            ],
            options={
                'verbose_name': 'ApiData',
                'verbose_name_plural': 'ApiDatas',
            },
        ),
    ]
