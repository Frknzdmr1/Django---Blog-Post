# Generated by Django 4.1.4 on 2022-12-22 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_page', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/images')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('N', 'Not to sa'), ('F', 'Female')], max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.user')),
            ],
        ),
    ]
