from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView
from django.core.paginator import Paginator

from .models import Author, Post, PostCategory, Comment, Category
from django.contrib.auth.models import User
from .filters import NewsFilter
from .forms import NewsForm, UserForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.


class NewsList(ListView):
    model = Post
    template_name = 'about.html'
    context_object_name = 'about'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 3
    form_class = NewsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст

        context['form'] = NewsForm()
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'inc.html'
    context_object_name = 'inc'


class SearchList(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    form_class = NewsForm

    def get_filter(self):
        return NewsFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET,
                                       queryset=self.get_queryset())
        context['form'] = NewsForm()
        return context


class NewsCreate(LoginRequiredMixin, CreateView):
    template_name = 'news_create.html'
    form_class = NewsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_premium'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class NewsUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'news_create.html'
    form_class = NewsForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_premium'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class NewsDelete(LoginRequiredMixin, DeleteView):
    template_name = 'news_delete.html'
    # form_class = NewsForm
    queryset = Post.objects.all()
    success_url = '/news/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_premium'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class AuthorDetail(DetailView):
    model = Author
    template_name = 'author.html'
    context_object_name = 'author'


class UserUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'edit_user.html'
    form_class = UserForm
    success_url = '/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return User.objects.get(pk=id)


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_premium'] = not self.request.user.groups.filter(name='authors').exists()
        return context