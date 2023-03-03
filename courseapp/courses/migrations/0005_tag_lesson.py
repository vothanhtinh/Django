# Generated by Django 4.1.7 on 2023-03-02 14:28

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_day', models.DateTimeField(auto_now_add=True)),
                ('updated_day', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_day', models.DateTimeField(auto_now_add=True)),
                ('updated_day', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('subject', models.CharField(max_length=255)),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(null=True, upload_to='courses/%Y/%m')),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('tags', models.ManyToManyField(to='courses.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
