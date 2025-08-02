import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
import django
django.setup()

from faker import Faker
import random
from events.models import Category, Event, Participant
from datetime import date, time, timedelta

# Function to populate the database

def populate_db():
    # Initialize Faker
    fake = Faker()

    # Create Categories
    categories = []
    for _ in range(5):
        category = Category.objects.create(
            name=fake.unique.word().capitalize(),
            description=fake.paragraph()
        )
        categories.append(category)
    print(f"Created {len(categories)} categories.")

    # Create Events
    events = []
    today = date.today()
    # Create a few events for today
    for _ in range(3):
        event_time = time(random.randint(9, 17), random.choice([0, 30]))
        event = Event.objects.create(
            name=f"Today's Event {_+1}",
            description=fake.paragraph(nb_sentences=3),
            date=today,
            time=event_time,
            location=fake.address(),
            category=random.choice(categories) if categories else None
        )
        events.append(event)

    # Create other events (past and future)
    for _ in range(17): # Reduced from 20 to 17 to account for today's events
        event_date = fake.date_between(start_date='-30d', end_date='+90d')
        event_time = time(random.randint(9, 17), random.choice([0, 30]))
        event = Event.objects.create(
            name=fake.sentence(nb_words=4),
            description=fake.paragraph(nb_sentences=3),
            date=event_date,
            time=event_time,
            location=fake.address(),
            category=random.choice(categories) if categories else None
        )
        events.append(event)
    print(f"Created {len(events)} events.")

    # Create Participants
    participants = []
    for _ in range(30):
        participant = Participant.objects.create(
            name=fake.name(),
            email=fake.unique.email()
        )
        # Assign random events to participants
        num_events = random.randint(0, 5)
        assigned_events = random.sample(events, min(num_events, len(events)))
        participant.events.set(assigned_events)
        participants.append(participant)
    print(f"Created {len(participants)} participants.")

    print("Database populated successfully!")


if __name__ == "__main__":
    populate_db()
