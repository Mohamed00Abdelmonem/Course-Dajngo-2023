# Generated by Django 4.2.3 on 2023-07-10 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


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
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('tag', models.CharField(max_length=255)),
                ('pdf_file', models.FileField(upload_to='pdfs/')),
                ('draft', models.BooleanField(default=True)),
                ('pdf', models.FileField(upload_to='pdfs/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
