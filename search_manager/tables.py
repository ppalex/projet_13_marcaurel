import django_tables2 as tables
from django_tables2.utils import A

from core.models.match import Match


class MatchTable(tables.Table):

    classification = tables.Column(verbose_name='Type de match')
    start_fixture = tables.Column(verbose_name='Date')
    administrator = tables.Column(
        accessor='administrator.user', verbose_name='Administrateur')
    available_place = tables.Column(verbose_name='Place disponible')
    city = tables.Column(
        accessor='address.city', verbose_name='Ville')

    detail = tables.LinkColumn(
        "match-detail", verbose_name='Action', args=[A('pk')],
        orderable=False, empty_values=(),  attrs={
            'a': {'class': "btn btn-table"},
        })

    class Meta:
        model = Match

        fields = ('classification', 'start_fixture', 'administrator',
                  'available_place', 'city')

    def render_detail(self):
        return ""
