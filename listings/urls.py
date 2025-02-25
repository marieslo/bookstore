from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, message_listing, view_messages


router = DefaultRouter()
router.register(r'listings', ListingViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('listings/<int:listing_pk>/message/', message_listing, name='message_listing'), 
    path('messages/', view_messages, name='view_messages'),
]
