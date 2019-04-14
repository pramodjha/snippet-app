from django.contrib.auth.models import User
from .models import TblSnippetTopics, TblSnippetData, TblLearnData, TblBlog
import django_filters
from django.forms.widgets import TextInput

class SnippetFilter(django_filters.FilterSet):
    snippet_data_keyword = django_filters.CharFilter(widget=TextInput(attrs={'placeholder': 'Search with Keyword'}),lookup_expr='icontains')
    class Meta:
        model = TblSnippetData
        fields = ['snippet_data_keyword']

class LearnFilter(django_filters.FilterSet):
    learn_data_keyword = django_filters.CharFilter(widget=TextInput(attrs={'placeholder': 'Search with Keyword'}),lookup_expr='icontains')
    class Meta:
        model = TblLearnData
        fields = ['learn_data_keyword']


class BlogFilter(django_filters.FilterSet):
    blog_keyword = django_filters.CharFilter(widget=TextInput(attrs={'placeholder': 'Search with Keyword'}),lookup_expr='icontains')
    class Meta:
        model = TblBlog
        fields = ['blog_keyword']
