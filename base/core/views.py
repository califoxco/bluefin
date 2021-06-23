from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Property
from .filters import PropertyFilter


# def home(request):
#     properties = Property.objects.all()
#     home_filter = PropertyFilter(request.GET, queryset=properties)
#     properties = home_filter.qs
#     context = {'properties': properties, 'home_filter': home_filter}
#     return render(request, 'home.html', context)


class HomeDetailView(DetailView):
    model = Property
    template_name = "property_detail.html"


# Could alternatively use ListView for better code optimization
class HomeView(ListView):
    model = Property
    template_name = "home.html"
    ordering = ['-listed_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        home_filter = PropertyFilter(self.request.GET, queryset=Property.objects.all())
        context['home_filter'] = home_filter
        context['object_list'] = home_filter.qs
        return context
