from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from . import models
# from .forms import CommentForm
from .models import Articles
from django.views.generic import DetailView, FormView, CreateView, UpdateView, DeleteView


class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'main/detail_view.html'
    context_object_name = 'article'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["comment_form"] = CommentForm()
    #     return context

#
# class BaseCommentView:
#     model = CommentModel
#
#     def get_success_url(self):
#         post = models.Articles.objects.get(pk=self.model.pk)
#         return reverse(
#             "news",
#             kwargs={"pk": post.pk},
#         )
#
#
# class AddCommentView(BaseCommentView, CreateView):
#     form_class = CommentForm
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.instance.post = models.Articles.objects.get(pk=self.kwargs.get("pk"))
#         return super().form_valid(form)
#
#
# class EditCommentView(BaseCommentView, UpdateView):
#     form_class = CommentForm
#     template_name = "main/comment_edit.html"
#
#
# class DeleteCommentView(BaseCommentView, DeleteView):
#     template_name = "main/comment_delete.html"


def index(request):
    news = Articles.objects.order_by('-pub_date')[:2]
    data = {
        'title': 'Соседи',
    }
    return render(request, 'main/index.html', {'news': news, 'data': data})


def about(request):
    return render(request, 'main/about.html')


def rooms(request):
    return render(request, 'main/rooms.html')


def services(request):
    return render(request, 'main/amenities.html')


def contacs(request):
    return render(request, 'main/contact.html')


def news(request):
    news = Articles.objects.order_by('-pub_date')
    return render(request, 'main/news.html', {'news': news})
