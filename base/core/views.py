import json

from django.http import HttpResponse
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

def homeJson(request, slug):
    response = ''
    property_qs = Property.objects.filter(slug=slug)
    if property_qs.exists():
        property = property_qs[0]
        serialized_date = property.listed_date.strftime("%Y-%m-%d %H:%M:%S")
        serialized_picture_url = request.get_host()+property.item_picture.url
        response = json.dumps([{ 'address1' : property.address_1,
                                 'address2': property.address_2,
                                 'listedDate': serialized_date,
                                 'city': property.city,
                                 'state': property.state,
                                 'zipCode': property.zip,
                                 'propertyType': property.property_type,
                                 'squareFeet': property.square_feet,
                                 'bedroomCount': property.number_bedroom,
                                 'bathroomCount': property.number_baths,
                                 'description': property.description,
                                 'status': property.transaction_state,
                                 'price': property.price,
                                 'primaryImageUrl': serialized_picture_url
                                 }])
    return HttpResponse(response, content_type='text/json')


class HomeDetailView(DetailView):
    model = Property
    template_name = "property_detail.html"


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
