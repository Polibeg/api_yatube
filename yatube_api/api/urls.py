from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CommentViewSet,
                       GroupViewSet,
                       PostViewSet)

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'^posts/(?P<post_id>[^/.]+)/comments',
                CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
]