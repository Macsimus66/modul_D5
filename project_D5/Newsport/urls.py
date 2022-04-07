from django.urls import path
from .views import NewsList, NewsDetail, NewsCreate, SearchList, NewsUpdate, NewsDelete, UserUpdate, AuthorDetail, IndexView


urlpatterns = [
    path('', IndexView.as_view()),
    path('news/', NewsList.as_view(), name='news'),
    path('news/<int:pk>', NewsDetail.as_view(), name='post'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('search/', SearchList.as_view(), name='search'),
    path('news/<int:pk>/update/', NewsUpdate.as_view(), name='news_create'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('author/<int:pk>/', AuthorDetail.as_view(), name='author'),
    path('author/<int:pk>/edit/', UserUpdate.as_view(), name='edit_user'),
]