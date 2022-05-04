from rest_framework import status
from .serializers import LocationSerializer, FetchLocationSerializer, FetchCordsSerializer, FetchAllSerializer
from .models import Location
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

# Create your views here.
class FetchAllView(APIView):
    serializer_class = LocationSerializer
    def get(self, request):
        
        #print(self.request.session.get('user_id'))
        queryset = Location.objects.all()
        
        location = FetchAllSerializer(queryset, many=True).data
        return Response(location, status.HTTP_200_OK)

class FetchLocationView(APIView):
    serializer_class = LocationSerializer

    def get(self, request, location_id):

        try:
            location = Location.objects.get(id=location_id)
        except Location.DoesNotExist:
            return Response("Location does not exist", status.HTTP_404_NOT_FOUND)

        return Response(FetchLocationSerializer(location).data, status.HTTP_200_OK)


class FetchCordsView(APIView):
    serializer_class = LocationSerializer
    def get(self, request):
        
        #print(self.request.session.get('user_id'))
        queryset = Location.objects.all()
        
        location = FetchCordsSerializer(queryset, many=True).data
        return Response(location, status.HTTP_200_OK)
    

class CreateLocationView(APIView):
    serializer_class = LocationSerializer

    def post(self, request):
        # token = request.COOKIES.get('JWT')
        # if not token:
        #     raise AuthenticationFailed('Unauthenticated!')

        # try:
        #     payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        # except jwt.ExpiredSignatureError:
        #     raise AuthenticationFailed('Unauthenticated!')

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            description = serializer.data.get('description')
            name = serializer.data.get('name')
            latitude = serializer.data.get('lat')
            longitude = serializer.data.get('lng')
            address = serializer.data.get('address')
            city = serializer.data.get('city')
            zipcode = serializer.data.get('zipcode')
            altitude = serializer.data.get('altitude')

            location = Location(description=description, name=name, lat=latitude, lng=longitude, address=address, city=city, zipcode=zipcode, altitude=altitude)
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
