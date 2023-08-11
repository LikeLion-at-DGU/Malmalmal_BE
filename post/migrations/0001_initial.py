# Generated by Django 4.2.4 on 2023-08-11 04:34

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('like', models.ManyToManyField(blank=True, default=0, related_name='liked_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Editor_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date', models.DateField()),
                ('recruit_date', models.DateField()),
                ('place', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('like', models.ManyToManyField(blank=True, default=0, related_name='editor_liked_post', to=settings.AUTH_USER_MODEL)),
                ('scarp', models.ManyToManyField(blank=True, default=0, related_name='scarped_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
