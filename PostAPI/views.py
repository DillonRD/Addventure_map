from rest_framework import status
from .serializers import GetPostSerializer, UserPostSerializer, CreatePostSerializer
from .models import Post
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class GetPostsView(APIView):
    serializer_class = UserPostSerializer

    def get(self, request):
        #if self.request.session.get('session_token') is None:
            #return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        queryset = Post.objects.all()
        posts = UserPostSerializer(queryset, many=True).data
        return Response(posts, status.HTTP_200_OK)

class GetPostView(APIView):
    serializer_class = UserPostSerializer

    def get(self, request, user_id):
        #if self.request.session.get('session_token') is None:
            #return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        queryset = Post.objects.filter(user=user_id)
        posts = UserPostSerializer(queryset, many=True).data
        return Response(posts, status.HTTP_200_OK)


class CreatePostView(APIView):
    serializer_class = CreatePostSerializer

    def post(self, request):
        #if self.request.session.get('session_token') is None:
            #return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            activity = self.request.session.get('activity')
            location = self.request.session.get('location')
            user = self.request.session.get('user')
            photo = serializer.data.get('photo')
            likes = 0
            text = serializer.data.get('text')

            post = Post(activity=activity, location=location, user=user, photo=photo, likes=likes, text=text)
            post.save()
            return Response(GetPostSerializer(post).data, status.HTTP_201_CREATED)


class DeletePostView(APIView):

    def delete(self, request, post_id):
        #if self.request.session.get('session_token') is None:
            #return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response("Review does not exist", status.HTTP_404_NOT_FOUND)

        post.delete()
        return Response("Review deleted", status.HTTP_200_OK)


class UpdatePostView(APIView):
    serializer_class = CreatePostSerializer

    def put(self, request, post_id):
        #if self.request.session.get('session_token') is None:
            #return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            photo = serializer.data.get('photo')
            text = serializer.data.get('text')

            post = Post.objects.get(id=post_id)
            fieldsToUpdate = []

            if photo != post.photo:
                post.photo = photo
                fieldsToUpdate.append('photo')
            if text != post.text:
                post.text = text
                fieldsToUpdate.append('text')

            post.save(update_fields=fieldsToUpdate)
            return Response("Review updated", status.HTTP_200_OK)
