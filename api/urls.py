from django.urls import path
from .views import UserSearchView, send_friend_request, accept_friend_request, reject_friend_request, ListFriendsView, PendingFriendRequestsView

urlpatterns = [
    path('', UserSearchView.as_view(), name='user-search'),
    path('friend-request/send/', send_friend_request, name='send-friend-request'),
    path('friend-request/accept/<int:request_id>/', accept_friend_request, name='accept-friend-request'),
    path('friend-request/reject/<int:request_id>/', reject_friend_request, name='reject-friend-request'),
    path('friends/', ListFriendsView.as_view(), name='list-friends'),
    path('friend-requests/pending/', PendingFriendRequestsView.as_view(), name='pending-friend-requests'),
]