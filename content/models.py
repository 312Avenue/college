from django.db import models
from django.contrib.auth import get_user_model


class Content(models.Model):
    slug = models.SlugField(verbose_name='Поле слаг', max_length=155)
    text = models.TextField(verbose_name='Текст')

    def __str__(self) -> str:
        return self.slug

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контенты'


class Img(models.Model):
    content = models.ForeignKey(Content, verbose_name='Контент', 
                            on_delete=models.CASCADE, related_name='image')
    img = models.ImageField(verbose_name='Фото', upload_to='content')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class File(models.Model):
    content = models.ForeignKey(Content, verbose_name='Контент', 
                            on_delete=models.CASCADE, related_name='file')
    file = models.FileField(verbose_name='Файл', upload_to='content')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class Comment(models.Model):
    rating_choice = (
        (1, '🌟'),
        (2, '🌟🌟'),
        (3, '🌟🌟🌟'),
        (4, '🌟🌟🌟🌟'),
        (5, '🌟🌟🌟🌟🌟'),
    )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comment')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='comment')
    text = models.TextField()
    rating = models.IntegerField(choices=rating_choice, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.rating and self.text:
            return f'Комментарий и оценка от {self.author.name} к посту {self.content}'
        elif self.rating:
            return f'Оценка от {self.author.name} к посту {self.content}'
        elif self.text:
            return f'Комментарий от {self.author.name} к посту {self.content}'


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-create_date']