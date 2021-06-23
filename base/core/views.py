import json
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Property
from .filters import PropertyFilter


# ------------------------------------ Home View ------------------------------------
# Description: Render webpage based on GET request and its parameters
# Parameters: request - the http request
# -----------------------------------------------------------------------------------
def home(request):
    properties = Property.objects.all()
    search_field = request.GET.get('search')  # /?search=<parameter>
    home_filter = PropertyFilter(request.GET, queryset=properties)  # Django-filter used for filtering
    # properties with matching address and cities are stored in 'properties'
    # note that search has a higher priority than filter
    if search_field is not None:
        properties = Property.objects.filter(Q(address_1__icontains=search_field)
                                             | Q(address_2__icontains=search_field)
                                             | Q(zip__icontains=search_field)
                                             | Q(city__icontains=search_field)
                                             | Q(state__icontains=search_field)
                                             | Q(property_type__icontains=search_field)
                                             )
    else:
        properties = home_filter.qs
    context = {'object_list': properties, 'home_filter': home_filter}
    return render(request, 'home.html', context)


# ---------------------------------- Property Json ----------------------------------
# Description: return Json through GET request
# Parameters: request - the http request
#             slug - unique slug field for each property
# -----------------------------------------------------------------------------------
def homeJson(request, slug):
    response = ''  # response is set to empty by default
    property_qs = Property.objects.filter(slug=slug)  # find property, note slug is unique
    if property_qs.exists():
        property = property_qs[0]
        serialized_date = property.listed_date.strftime("%Y-%m-%d %H:%M:%S")  # serializing date, but loses significance
        serialized_picture_url = request.get_host() + property.item_picture.url  # serializing url
        response = json.dumps([{'address1': property.address_1,
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


# ------------------------------------ Detail View ------------------------------------
# Description: Render detail page based on model.
# Parameters: DetailView - generic view
# -----------------------------------------------------------------------------------
class HomeDetailView(DetailView):
    model = Property
    template_name = "property_detail.html"

    # redirects the search bar when user is on detail view
    def get(self, request, *args, **kwargs):
        search_field = request.GET.get('search')
        if search_field is not None:
            return redirect('/?search=' + search_field)
        return super().get(self, request, *args, **kwargs)
