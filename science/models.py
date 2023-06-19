from django.db import models


class Chapter(models.Model):
    name = models.CharField(verbose_name='Название раздела', max_length=155, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class News(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    chapter = models.ForeignKey(Chapter, verbose_name='Раздел', related_name='news_chapter', on_delete=models.CASCADE)
    file = models.FileField(verbose_name='', upload_to='sciense')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
