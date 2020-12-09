from django.shortcuts import render

from django.views.generic import View

from core.models.match import Match


from .forms import MatchFormFilter, AddressFormFilter


class SearchMatchView(View):

    template_name = "search_manager/search_match.html"

    def get(self, request, *args, **kwargs):

        context = {}
        context['match_filter'] = MatchFormFilter()
        context['address_filter'] = AddressFormFilter()
        context['object_list'] = Match.objects.all()

        return render(request, self.template_name, context)
