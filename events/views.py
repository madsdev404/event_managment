from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.db.models import Count
from datetime import date
from django.urls import reverse_lazy
from .models import Category, Event, Participant
from .forms import CategoryForm, EventForm, ParticipantForm

# Category Views
class CategoryListView(ListView):
    model = Category
    template_name = 'events/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'events/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'events/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'events/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'events/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

# Event Views
from django.db.models import Q
from datetime import date

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        queryset = super().get_queryset().select_related('category').prefetch_related('participants')

        # Search functionality
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(location__icontains=query))

        # Filter by category
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category__id=category_id)

        # Filter by date range
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')

        if start_date_str and end_date_str:
            try:
                start_date = date.fromisoformat(start_date_str)
                end_date = date.fromisoformat(end_date_str)
                queryset = queryset.filter(date__range=[start_date, end_date])
            except ValueError:
                # Handle invalid date format if necessary
                pass

        return queryset

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event_list')

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event_list')

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('event_list')

# Participant Views
class ParticipantListView(ListView):
    model = Participant
    template_name = 'events/participant_list.html'
    context_object_name = 'participants'

class ParticipantDetailView(DetailView):
    model = Participant
    template_name = 'events/participant_detail.html'
    context_object_name = 'participant'

class ParticipantCreateView(CreateView):
    model = Participant
    form_class = ParticipantForm
    template_name = 'events/participant_form.html'
    success_url = reverse_lazy('participant_list')

class ParticipantUpdateView(UpdateView):
    model = Participant
    form_class = ParticipantForm
    template_name = 'events/participant_form.html'
    success_url = reverse_lazy('participant_list')

class ParticipantDeleteView(DeleteView):
    model = Participant
    template_name = 'events/participant_confirm_delete.html'
    success_url = reverse_lazy('participant_list')

class DashboardView(TemplateView):
    template_name = 'events/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = date.today()

        # Stats Grid
        total_participants = Participant.objects.count()
        total_events = Event.objects.count()
        upcoming_events_count = Event.objects.filter(date__gte=today).count()
        past_events_count = Event.objects.filter(date__lt=today).count()
        today_events_count = Event.objects.filter(date=today).count()

        context['total_participants'] = total_participants
        context['total_events'] = total_events
        context['upcoming_events_count'] = upcoming_events_count
        context['past_events_count'] = past_events_count
        context['today_events_count'] = today_events_count

        # Today's Events Listing
        context['today_events'] = Event.objects.filter(date=today)

        # Interactive Stats (initial load or filtered)
        event_type = self.request.GET.get('event_type')
        if event_type == 'total':
            events_display = Event.objects.all()
        elif event_type == 'upcoming':
            events_display = Event.objects.filter(date__gte=today)
        elif event_type == 'past':
            events_display = Event.objects.filter(date__lt=today)
        else:
            events_display = Event.objects.all() # Default to all events

        context['events_display'] = events_display

        return context