# Generated by Django 4.2.7 on 2023-12-21 06:44

from django.db import migrations, models
import django.db.models.deletion
import scholar_ships.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(db_index=True)),
                ('description', models.TextField()),
                ('scholar_link', models.URLField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('name', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images/', validators=[scholar_ships.models.validate_image_size])),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.provider')),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship_Seeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('scholarship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scholar_ships.scholarship')),
                ('seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.seeker')),
            ],
        ),
        migrations.AddField(
            model_name='scholarship',
            name='seeker',
            field=models.ManyToManyField(through='scholar_ships.Scholarship_Seeker', to='user.seeker'),
        ),
    ]
