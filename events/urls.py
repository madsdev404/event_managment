from django.urls import path
from .views import (
    CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView,
    ParticipantListView, ParticipantDetailView, ParticipantCreateView, ParticipantUpdateView, ParticipantDeleteView,
    DashboardView
)

urlpatterns = [
    # Category URLs
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/add/', CategoryCreateView.as_view(), name='category_add'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_edit'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    # Event URLs
    path('', EventListView.as_view(), name='event_list'), # Changed from 'events/'
    path('<int:pk>/', EventDetailView.as_view(), name='event_detail'), # Changed from 'events/<int:pk>/'
    path('add/', EventCreateView.as_view(), name='event_add'), # Changed from 'events/add/'
    path('<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit'), # Changed from 'events/<int:pk>/edit/'
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'), # Changed from 'events/<int:pk>/delete/'

    # Participant URLs
    path('participants/', ParticipantListView.as_view(), name='participant_list'),
    path('participants/<int:pk>/', ParticipantDetailView.as_view(), name='participant_detail'),
    path('participants/add/', ParticipantCreateView.as_view(), name='participant_add'),
    path('participants/<int:pk>/edit/', ParticipantUpdateView.as_view(), name='participant_edit'),
    path('participants/<int:pk>/delete/', ParticipantDeleteView.as_view(), name='participant_delete'),

    # Dashboard URL
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]