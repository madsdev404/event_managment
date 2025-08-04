from django.urls import path
from .views import (
    CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView,
    AdminDashboardView, OrganizerDashboardView, ParticipantDashboardView, HomeView, rsvp_event, dashboard_redirect_view
)

urlpatterns = [
    # Category URLs
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/add/', CategoryCreateView.as_view(), name='category_add'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_edit'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    # Event URLs
    path('', HomeView.as_view(), name='home'),
    path('events/', EventListView.as_view(), name='event_list'),
    path('<int:pk>/', EventDetailView.as_view(), name='event_detail'), 
    path('add/', EventCreateView.as_view(), name='event_add'), 
    path('<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit'), 
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('event/<int:event_id>/rsvp/', rsvp_event, name='rsvp_event'),
    
    # Dashboard URLs
    path('dashboard/', dashboard_redirect_view, name='dashboard'),
    path('admin_dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('organizer_dashboard/', OrganizerDashboardView.as_view(), name='organizer_dashboard'),
    path('participant_dashboard/', ParticipantDashboardView.as_view(), name='participant_dashboard'),
]