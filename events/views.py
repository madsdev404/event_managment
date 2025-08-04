from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.db.models import Count
from datetime import date
from django.urls import reverse_lazy
from .models import Category, Event
from .forms import CategoryForm, EventForm
from users.models import CustomUser
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from users.decorators import admin_required, organizer_required, participant_required

# Category Views
class CategoryListView(ListView):
    model = Category
    template_name = 'events/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'events/category_detail.html'
    context_object_name = 'category'

@organizer_required
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'events/category_form.html'
    success_url = reverse_lazy('category_list')

@organizer_required
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'events/category_form.html'
    success_url = reverse_lazy('category_list')

@organizer_required
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

@organizer_required
class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event_list')

@organizer_required
class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event_list')

@organizer_required
class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('event_list')

class HomeView(TemplateView):
    template_name = 'events/home.html'

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.db.models import Count
from datetime import date
from django.urls import reverse_lazy
from .models import Category, Event
from .forms import CategoryForm, EventForm
from users.models import CustomUser
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from users.decorators import admin_required, organizer_required, participant_required
from django.utils.decorators import method_decorator

# Category Views
class CategoryListView(ListView):
    model = Category
    template_name = 'events/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'events/category_detail.html'
    context_object_name = 'category'

@method_decorator(organizer_required, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'events/category_form.html'
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)

@method_decorator(organizer_required, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'events/category_form.html'
    success_url = reverse_lazy('category_list')

@method_decorator(organizer_required, name='dispatch')
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

@method_decorator(organizer_required, name='dispatch')
class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event_list')

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)

@method_decorator(organizer_required, name='dispatch')
class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event_list')

@method_decorator(organizer_required, name='dispatch')
class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('event_list')

class HomeView(TemplateView):
    template_name = 'events/home.html'

@method_decorator(admin_required, name='dispatch')
class AdminDashboardView(TemplateView):
    template_name = 'events/dashboard.html' # Using the existing dashboard for now

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = date.today()

        # Stats Grid
        total_participants = CustomUser.objects.count()
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

@method_decorator(organizer_required, name='dispatch')
class OrganizerDashboardView(TemplateView):
    template_name = 'events/dashboard.html' # Using the existing dashboard for now

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.filter(organizer=self.request.user) # Assuming an 'organizer' field on Event
        context['categories'] = Category.objects.filter(organizer=self.request.user) # Assuming an 'organizer' field on Category
        return context

@method_decorator(participant_required, name='dispatch')
class ParticipantDashboardView(TemplateView):
    template_name = 'events/dashboard.html' # Using the existing dashboard for now

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rsvped_events'] = self.request.user.events.all()
        return context

@login_required
def rsvp_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user in event.participants.all():
        event.participants.remove(request.user)
    else:
        event.participants.add(request.user)
    return redirect('event_detail', pk=event_id)

@login_required
def dashboard_redirect_view(request):
    if request.user.groups.filter(name='Admin').exists():
        return redirect('admin_dashboard')
    elif request.user.groups.filter(name='Organizer').exists():
        return redirect('organizer_dashboard')
    elif request.user.groups.filter(name='Participant').exists():
        return redirect('participant_dashboard')
    else:
        return redirect('home') # Default redirect if no role is assigned
