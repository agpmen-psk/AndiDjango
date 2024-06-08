from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=100)
    preview = models.CharField('Анонс', max_length=250)
    content = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
