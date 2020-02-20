from rest_framework.generics import ListAPIView, get_object_or_404

from netcovapp.models import Coverage, City
from netcovapp.serializers import CoverageSerializer
from netcovapp.services.location_tools import string_to_city


class CoverageView(ListAPIView):
    """
    API endpoint that allows coverage to be verified.
    """
    serializer_class = CoverageSerializer

    def get_queryset(self):
        location_string = self.request.query_params.get('q')
        city_name = string_to_city(location_string)
        city = get_object_or_404(City, name=city_name)
        queryset = Coverage.objects.filter(city=city)
        return queryset.order_by('-operator')
