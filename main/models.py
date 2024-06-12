from django.contrib.auth.models import User
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


# class CommentModel(models.Model):
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, verbose_name="Пользователь"
#     )
#     post = models.ForeignKey(
#         Articles,
#         on_delete=models.CASCADE,
#         verbose_name="Пост",
#         related_name="comments",
#     )
#     comment = models.TextField(verbose_name="Комментарий")
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name = "Комментарий"
#         verbose_name_plural = "Комментарии"
#
#     def __str__(self):
#         return f"Комментарий от {self.user} к посту {self.post}"
