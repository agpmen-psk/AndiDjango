from django.urls import path
from main import views

urlpatterns = [
    path('', views.index,name='home'),
    path('about', views.about,name='about'),
    path('rooms', views.rooms,name='rooms'),
    path('services', views.services,name='services'),
    path('contacs', views.contacs,name='contacs'),
    path('news', views.news,name='news'),
    path('news/<int:pk>', views.ArticleDetailView.as_view(),name='news-detail'),

    # path("comment/add/<int:pk>/", views.AddCommentView.as_view(), name="add_comment"),
    # path("comment/edit/<int:pk>/", views.EditCommentView.as_view(), name="edit_comment"),
    # path("comment/delete/<int:pk>/", views.DeleteCommentView.as_view(), name="delete_comment",),
]