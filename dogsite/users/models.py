from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUserManager(UserManager):
    def _create_user(self, login, password, **extra_fields):
        if not login:
            raise ValueError('Необходимо указать имя пользователя')

        user = self.model(
            login=login,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, login, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(login, password, **extra_fields)

    def create_superuser(self, login, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(login, password, **extra_fields)


class User(AbstractBaseUser):
    login = models.CharField('имя пользователя',
                             max_length=100,
                             help_text='Максимальная длина 100 символов',
                             unique=True,
                             blank=False)
    city = models.CharField('город (для кинологов)',
                            max_length=100,
                            help_text='Максимальная длина 100 символов',
                            default='No city')

    is_staff = models.BooleanField('сотрудник', default=False)
    is_cynologist = models.BooleanField('кинолог', default=False)
    is_superuser = models.BooleanField('админ', default=False)
    is_active = models.BooleanField('активный пользователь', default=True)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['password']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.login

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True
