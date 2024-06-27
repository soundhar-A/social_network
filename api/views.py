from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from .models import User, FriendRequest
from .serializers import UserSerializer, FriendRequestSerializer
from django.db.models import Q

class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        keyword = self.request.query_params.get('search', '')
        return User.objects.filter(
            Q(email__iexact=keyword) |
            Q(username__icontains=keyword)
        )[:10]

@api_view(['POST'])
def send_friend_request(request):
    # Logic for sending friend request
    pass

@api_view(['POST'])
def accept_friend_request(request, request_id):
    # Logic for accepting friend request
    pass

@api_view(['POST'])
def reject_friend_request(request, request_id):
    # Logic for rejecting friend request
    pass

class ListFriendsView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(sent_requests__to_user=user, sent_requests__status='accepted')

class PendingFriendRequestsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        user = self.request.user
        return FriendRequest.objects.filter(to_user=user, status='pending')