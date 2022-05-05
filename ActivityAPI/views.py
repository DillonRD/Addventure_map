from rest_framework import status
from .serializers import ActivitySerializer, FetchActivitySerializer
from .models import Activity
from LocationAPI.models import Location
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class FetchActivityByLocationView(APIView):
    serializer_class = ActivitySerializer

    def get(self, request, name):

        try:
            activity = Activity.objects.filter(location__name__contains=name)
            serializer = FetchActivitySerializer(activity, many=True)
            return Response(serializer.data, status.HTTP_200_OK)

        except Activity.DoesNotExist:
            return Response("No activities exist for this location", status.HTTP_404_NOT_FOUND)


class FetchActivityView(APIView):
    serializer_class = ActivitySerializer

    def get(self, request, activity_id):
        #if self.request.session.get('session_token') is None:
            #return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        try:
            activity = Activity.objects.get(id=activity_id)
        except Activity.DoesNotExist:
            return Response("Activity does not exist", status.HTTP_404_NOT_FOUND)

        return Response(FetchActivitySerializer(activity).data, status.HTTP_200_OK)


class CreateActivityView(APIView):
    serializer_class = ActivitySerializer

    def post(self, request):
        #if self.request.session.get('session_token') is None:
            #return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            description = serializer.data.get('description')
            name = serializer.data.get('name')
            approach = serializer.data.get('approach')
            altitude = serializer.data.get('altitude')
            height = serializer.data.get('height')
            difficulty = serializer.data.get('difficulty')
            start_latitude = serializer.data.get('start_latitude')
            start_longitude = serializer.data.get('start_longitude')
            finish_latitude = serializer.data.get('finish_latitude')
            finish_longitude = serializer.data.get('finish_longitude')
            location = serializer.data.get('location')
            temp = Location.objects.get(id=location)
            activity = Activity(description=description, name=name, approach=approach, altitude=altitude, height=height
                                , difficulty=difficulty, start_latitude=start_latitude, start_longitude=start_longitude
                                , finish_latitude=finish_latitude, finish_longitude=finish_longitude, location=temp)
            activity.save()
            return Response(FetchActivitySerializer(activity).data, status.HTTP_201_CREATED)


class DeleteActivityView(APIView):

    def delete(self, request, activity_id):
        #if self.request.session.get('session_token') is None:
            #return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        try:
            activity = Activity.objects.get(id=activity_id)
        except Activity.DoesNotExist:
            return Response("Activity does not exist", status.HTTP_404_NOT_FOUND)

        activity.delete()
        return Response("Activity deleted", status.HTTP_200_OK)


class UpdateActivityView(APIView):
    serializer_class = ActivitySerializer

    def put(self, request, activity_id):
        #if self.request.session.get('session_token') is None:
            #return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            description = serializer.data.get('description')
            name = serializer.data.get('name')
            approach = serializer.data.get('approach')
            altitude = serializer.data.get('altitude')
            height = serializer.data.get('height')
            difficulty = serializer.data.get('difficulty')
            start_latitude = serializer.data.get('start_latitude')
            start_longitude = serializer.data.get('start_longitude')
            finish_latitude = serializer.data.get('finish_latitude')
            finish_longitude = serializer.data.get('finish_longitude')

            activity = Activity.objects.get(id=activity_id)
            fieldsToUpdate = []

            if description != activity.description:
                activity.description = description
                fieldsToUpdate.append('description')
            if name != activity.name:
                activity.name = name
                fieldsToUpdate.append('name')
            if approach != activity.approach:
                activity.approach = approach
                fieldsToUpdate.append('approach')
            if altitude != activity.altitude:
                activity.altitude = altitude
                fieldsToUpdate.append('altitude')
            if height != activity.height:
                activity.height = height
                fieldsToUpdate.append('height')
            if difficulty != activity.difficulty:
                activity.difficulty = difficulty
                fieldsToUpdate.append('difficulty')
            if start_latitude != activity.start_latitude:
                activity.start_latitude = start_latitude
                fieldsToUpdate.append('start_latitude')
            if start_longitude != activity.start_longitude:
                activity.start_longitude = start_longitude
                fieldsToUpdate.append('start_longitude')
            if finish_latitude != activity.finish_latitude:
                activity.finish_latitude = finish_latitude
                fieldsToUpdate.append('finish_latitude')
            if finish_longitude != activity.finish_longitude:
                activity.finish_longitude = finish_longitude
                fieldsToUpdate.append('finish_longitude')

            activity.save(update_fields=fieldsToUpdate)
            return Response("Activity updated", status.HTTP_200_OK)
