from django.db import models
from slugify import slugify


class Pulpit(models.Model):
    slug = models.SlugField(max_length=155, primary_key=True, 
                            verbose_name='Поле слаг', unique=True, 
                            blank=True)
    puplit = models.CharField(max_length=155, verbose_name='Кафедра')

    def __str__(self) -> str:
        return self.slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.puplit)
        super(Pulpit, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'

    
class Employe(models.Model):
    puplit = models.ForeignKey(Pulpit, related_name='puppit', 
                                verbose_name='Кафедра', 
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=155, verbose_name='Имя')
    last_name = models.CharField(max_length=155, verbose_name='Фамилия')
    otch = models.CharField(max_length=155, verbose_name='Отчество')
    email = models.EmailField(verbose_name='Почта')
    description = models.TextField(verbose_name='Описание')
    post = models.CharField(max_length=155, verbose_name='Должность')
    img = models.ImageField(upload_to='employe', verbose_name='Фото')

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'