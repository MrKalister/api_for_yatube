from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from posts.models import Follow, Group, Post

from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)
from .viewsets import CreateListViewSet


class CommentViewSet(viewsets.ModelViewSet):
    '''
    Allows the author access to modify, delete, extract and create
    comments, anonymous users have read-only access.
    '''
    serializer_class = CommentSerializer

    def get_queryset(self):
        return get_object_or_404(
            Post,
            pk=self.kwargs.get("post_id")
        ).comments.all()

    def perform_create(self, serializer):
        s_post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        serializer.save(author=self.request.user, post=s_post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    Provides all users with read-only access.
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(CreateListViewSet):
    '''
    Provides you the opportunity to create a following on the author
    and get your own followings, available only to authorized users.
    Has a research search using the "?search" parameter.
    '''
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    '''
    Allows the author access to modify, delete, extract and create
    posts, anonymous users have read-only access.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
