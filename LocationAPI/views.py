from rest_framework import status
from .serializers import LocationSerializer, FetchLocationSerializer
from .models import Location
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class FetchLocationView(APIView):
    serializer_class = LocationSerializer

    def get(self, request, location_id):
        #if self.request.session.get('session_token') is None:
            #return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        try:
            location = Location.objects.get(id=location_id)
        except Location.DoesNotExist:
            return Response("Location does not exist", status.HTTP_404_NOT_FOUND)

        return Response(FetchLocationSerializer(location).data, status.HTTP_200_OK)


class CreateLocationView(APIView):
    serializer_class = LocationSerializer

    def post(self, request):
        #if self.request.session.get('session_token') is None:
            #return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            description = serializer.data.get('description')
            name = serializer.data.get('name')
            latitude = serializer.data.get('latitude')
            longitude = serializer.data.get('longitude')
            address = serializer.data.get('address')
            city = serializer.data.get('city')
            zipcode = serializer.data.get('zipcode')
            altitude = serializer.data.get('altitude')

            location = Location(description=description, name=name, latitude=latitude, longitude=longitude, address=address, city=city, zipcode=zipcode, altitude=altitude)
            location.save()
            return Response(FetchLocationSerializer(location).data, status.HTTP_201_CREATED)


class DeleteLocationView(APIView):

    def delete(self, request, location_id):
        #if self.request.session.get('session_token') is None:
            #return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        try:
            location = Location.objects.get(id=location_id)
        except Location.DoesNotExist:
            return Response("Location does not exist", status.HTTP_404_NOT_FOUND)

        location.delete()
        return Response("Location deleted", status.HTTP_200_OK)


class UpdateLocationView(APIView):
    serializer_class = LocationSerializer

    def put(self, request, location_id):
        #if self.request.session.get('session_token') is None:
            #return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            description = serializer.data.get('description')
            name = serializer.data.get('name')
            latitude = serializer.data.get('latitude')
            longitude = serializer.data.get('longitude')
            address = serializer.data.get('address')
            city = serializer.data.get('city')
            zipcode = serializer.data.get('zipcode')
            altitude = serializer.data.get('altitude')

            location = Location.objects.get(id=location_id)
            fieldsToUpdate = []

            if description != location.description:
                location.description = description
                fieldsToUpdate.append('description')
            if name != location.name:
                location.name = name
                fieldsToUpdate.append('name')
            if latitude != location.latitude:
                location.latitude = latitude
                fieldsToUpdate.append('latitude')
            if longitude != location.longitude:
                location.longitude = longitude
                fieldsToUpdate.append('longitude')
            if address != location.address:
                location.address = address
                fieldsToUpdate.append('address')
            if city != location.city:
                location.city = city
                fieldsToUpdate.append('city')
            if zipcode != location.zipcode:
                location.zipcode = zipcode
                fieldsToUpdate.append('zipcode')
            if altitude != location.altitude:
                location.altitude = altitude
                fieldsToUpdate.append('altitude')

            location.save(update_fields=fieldsToUpdate)
            return Response("Location updated", status.HTTP_200_OK)
