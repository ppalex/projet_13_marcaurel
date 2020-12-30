import django_tables2 as tables

from core.models.match import Match
from django_tables2.utils import A


class MatchTable(tables.Table):

    classification = tables.Column(verbose_name='Type de match')
    fixture = tables.Column(verbose_name='Date')
    administrator = tables.Column(
        accessor='administrator.user', verbose_name='Administrateur')
    available_place = tables.Column(verbose_name='Place disponible')
    city = tables.Column(
        accessor='address.city', verbose_name='Ville')

    detail = tables.LinkColumn(
        "match-detail", verbose_name='Action', args=[A('pk')],
        orderable=False, empty_values=(),  attrs={
            'a': {'class': "btn btn-info btn-icon-split"}
        })

    class Meta:
        model = Match

        fields = ('classification', 'start_fixture', 'administrator',
                  'available_place', 'city')

    def render_detail(self):
        return 'Consulter'
