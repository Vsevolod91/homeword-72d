from django.db import models
from tinymce import models as tinymce_models
from django.urls import reverse_lazy
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    BANNED_TRUE = 'Заблокирован модератором'
    BANNED_FALSE = 'Не заблокирован'
    BANNED_STATUSES = (
        (BANNED_TRUE, 'ЗАБЛОКИРОВАТЬ'),
        (BANNED_FALSE, 'РАЗБЛОКИРОВАТЬ')
    )

    AUTHOR = 'Автор'
    CUSTOMER = 'Слушатель'
    ROLES = (
        (AUTHOR, 'Автор'),
        (CUSTOMER, 'Слушатель')
    )

    username = None
    email = models.EmailField(verbose_name='Почта', unique=True)
    phone = models.CharField(verbose_name='Телефон', max_length=20, **NULLABLE)
    country = models.CharField(verbose_name='Страна', max_length=30, **NULLABLE)
    city = models.CharField(verbose_name='Город', max_length=30, **NULLABLE)
    avatar = models.ImageField(verbose_name='Аватарка', upload_to='usersavatars/', help_text=f'рекомендуемый размер 600*600', **NULLABLE)
    email_verify = models.BooleanField(default=False)
    banned = models.CharField(choices=BANNED_STATUSES, default=BANNED_FALSE, max_length=30, verbose_name='Забанить пользователя?')
    comment = models.CharField(verbose_name='Комментарий пользователю', **NULLABLE, max_length=100)
    role = models.CharField(max_length=20, choices=ROLES, verbose_name='Роль')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return  f'{self.email}, {self.phone}, {self.country}, {self.city}'


class Course(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Автор курса')
    title = models.CharField(max_length=70, verbose_name='Название курса', db_index=True, unique=True)
    annotation = models.CharField(max_length=200, verbose_name='Аннотация')
    content = tinymce_models.HTMLField(verbose_name='Подробное описание', **NULLABLE)
    picture = models.ImageField(verbose_name='Картинка', upload_to='picture_courses/', help_text='Рекомендуемый размер 2000*1000', **NULLABLE)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return f'{self.title}'


class Lesson(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Автор курса')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='Курс урока')
    title = models.CharField(max_length=70, verbose_name='Название курса', unique=False)
    annotation = models.CharField(max_length=200, verbose_name='Аннотация')
    content = tinymce_models.HTMLField(verbose_name='Подробное описание', **NULLABLE)
    picture = models.ImageField(verbose_name='Картинка', upload_to='picture_courses/', help_text='Рекомендуемый размер 2000*1000', **NULLABLE)
    link_movie = models.CharField(max_length=300, verbose_name='Ссылка на видео на YouTube', **NULLABLE)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return f'{self.title}'


class Payment(models.Model):
    CASH = 'Наличный расчет'
    CASHLESS = 'Безналичный расчет'
    TYPE_PAYMENTS = (
        (CASH, 'Наличный расчет'),
        (CASHLESS, 'Безналичный расчет')
    )

    customer = models.ForeignKey('User', on_delete=models.PROTECT)
    course = models.ForeignKey('Course', on_delete=models.PROTECT)
    lesson = models.ForeignKey('Lesson', on_delete=models.PROTECT, **NULLABLE)
    date = models.DateTimeField(auto_now=True, verbose_name='Дата оплаты')
    amount = models.SmallIntegerField(verbose_name='Сумма оплаты')
    type = models.CharField(choices=TYPE_PAYMENTS, max_length=30)


