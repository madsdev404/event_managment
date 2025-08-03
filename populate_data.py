import os
import django
from faker import Faker
import random
from datetime import timedelta, date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()

from events.models import Category, Event, Participant

fake = Faker()

def clear_data():
    print("Clearing existing data...")
    Participant.objects.all().delete()
    Event.objects.all().delete()
    Category.objects.all().delete()
    print("Data cleared.")

def populate_data(num_categories=5, num_events=20, num_participants=30):
    print("Populating data...")

    # Create Categories
    categories = []
    for _ in range(num_categories):
        category = Category.objects.create(name=fake.unique.word().capitalize() + ' Events')
        categories.append(category)
    print(f"Created {len(categories)} categories.")

    # Create Events
    events = []
    today = date.today()
    for i in range(num_events):
        category = random.choice(categories)
        if i < 3:  # Ensure at least 3 events are for today
            event_date = today
        else:
            event_date = fake.date_between(start_date='-30d', end_date='+365d')
        event = Event.objects.create(
            name=fake.sentence(nb_words=4).replace('.', '').title(),
            description=fake.paragraph(nb_sentences=5),
            date=event_date,
            time=fake.time_object(),
            location=fake.address(),
            category=category
        )
        events.append(event)
    print(f"Created {len(events)} events.")

    # Create Participants and register them for events
    participants = []
    for _ in range(num_participants):
        participant = Participant.objects.create(
            name=fake.name(),
            email=fake.unique.email()
        )
        participants.append(participant)

        # Register participant for 1 to 3 random events
        num_events_to_register = random.randint(1, 3)
        selected_events = random.sample(events, min(num_events_to_register, len(events)))
        for event in selected_events:
            participant.events.add(event)
    print(f"Created {len(participants)} participants and registered them for events.")

    print("Database populated successfully!")

if __name__ == '__main__':
    clear_data()
    populate_data()
