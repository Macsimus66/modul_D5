from django_filters import FilterSet, DateFilter
from .models import Post
import django.forms


class NewsFilter(FilterSet):
    dateCreation = DateFilter(
        lookup_expr='gte',
        widget=django.forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    class Meta:
        model = Post

        fields = {
            'author': ['exact'],
            'postCategory': ['exact'],
            'rating': ['gt'],
        }