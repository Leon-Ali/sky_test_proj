from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField


class ResumeStatus(models.TextChoices):
    DRAFT = 'DR'
    PUBLISHED = 'PB'


class Grade(models.TextChoices):
    JUNIOR = 'JUN'
    MIDDLE = 'MID'
    SENIOR = 'SEN'


class Resume(models.Model):

    user = models.OneToOneField(User, verbose_name='пользователь')
    status = models.CharField(
        max_length=2,
        choices=ResumeStatus.choices,
        default=ResumeStatus.DRAFT,
        verbose_name='статус',
    )
    grade = models.CharField(
        max_length=3,
        choices=Grade.choices,
        verbose_name='грейд',
    )
    specialty = models.CharField(max_length=250, verbose_name='специальность')
    salary = models.FloatField(verbose_name='зарплата')
    education = models.TextField(verbose_name='образование')
    experience = models.TextField(verbose_name='опыт')
    portfolio = models.URLField(verbose_name='портфолио')
    title = models.CharField(max_length=250, verbose_name='название')
    phone = PhoneNumberField(blank=True, verbose_name='телефон')
    email = models.EmailField(verbose_name='email')
