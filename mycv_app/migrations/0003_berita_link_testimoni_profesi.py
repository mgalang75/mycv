# Generated by Django 5.0.3 on 2024-03-28 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycv_app', '0002_berita_testimoni_delete_news_delete_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='berita',
            name='link',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='testimoni',
            name='profesi',
            field=models.CharField(default='', max_length=200),
        ),
    ]