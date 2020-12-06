from django.shortcuts import render

from django.views.generic import View

from core.models.match import Match

from .filters.match_filters import MatchFilter

from django_filters.views import FilterView

from .forms import MatchFormFilter, AddressFormFilter

from django.core.serializers import serialize
# class SearchMatchView(FilterView):
#     model = Match
#     template_name = "search_manager/search_match.html"
#     filter_class = MatchFilter

#     def get_context_data(self, **kwargs):

#         context = super().get_context_data(**kwargs)

#         context['filter_class'] = self.filter_class

#         print(self.filter_class.qs)

#         return context

#     def post(self, request, *args, **kwargs):

#         match_filter = self.filter_class
#         context = {}
#         context['filter_class'] = match_filter

#         return render(request, self.template_name, context)


class SearchMatchView(View):

    template_name = "search_manager/search_match.html"

    def get(self, request, *args, **kwargs):

        context = {}
        context['match_filter'] = MatchFormFilter()
        context['address_filter'] = AddressFormFilter()
        context['object_list'] = Match.objects.all()

        return render(request, self.template_name, context)
