import django_filters

from core.models.match import Match


class MatchFilter(django_filters.FilterSet):
    class Meta:
        model = Match
        fields = ['classification']
