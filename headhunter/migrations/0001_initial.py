# Generated by Django 4.1.1 on 2022-10-02 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('DR', 'Draft'), ('PB', 'Published')], default='DR', max_length=2, verbose_name='статус')),
                ('grade', models.CharField(choices=[('JUN', 'Junior'), ('MID', 'Middle'), ('SEN', 'Senior')], max_length=3, verbose_name='грейд')),
                ('specialty', models.CharField(max_length=250, verbose_name='специальность')),
                ('salary', models.FloatField(verbose_name='зарплата')),
                ('education', models.TextField(verbose_name='образование')),
                ('experience', models.TextField(verbose_name='опыт')),
                ('portfolio', models.URLField(verbose_name='портфолио')),
                ('title', models.CharField(max_length=250, verbose_name='название')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
    ]
