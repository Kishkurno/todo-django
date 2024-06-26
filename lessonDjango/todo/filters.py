import django_filters
from django.db.models import Q
from .models import Todo

class TodoFilter(django_filters.FilterSet):
    display_title = django_filters.CharFilter(method='filter_by_display_title')

    class Meta:
        model = Todo
        fields = []

    def filter_by_display_title(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(user__name__icontains=value)
        )
