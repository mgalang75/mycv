# Generated by Django 5.0.3 on 2024-03-27 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycv_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Berita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('deskripsi', models.TextField()),
                ('kategori', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Testimoni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('deskripsi', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.DeleteModel(
            name='Testimonial',
        ),
    ]