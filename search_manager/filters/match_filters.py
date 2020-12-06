import django_filters

from core.models.match import Match


class MatchFilter(django_filters.FilterSet):
    # classification = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Match
        fields = ['classification']
