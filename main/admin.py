from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models
from .models import Articles

admin.site.register(Articles)


# @admin.register(models.CommentModel)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ("user", "post_link", "created_at", "comment")
#     list_filter = ("user", "post")
#
#     def post_link(self, obj):
#         return mark_safe(
#             f'<a href="{obj.post.get_absolute_url()}">{obj.post.title}</a>'
#         )
#
#     post_link.allow_tags = True
