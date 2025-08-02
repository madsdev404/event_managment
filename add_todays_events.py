import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
import django
django.setup()

from faker import Faker
import random
from events.models import Category, Event
from datetime import date, time

def add_todays_events():
    fake = Faker()
    today = date.today()

    # Ensure there's at least one category to link events to
    categories = list(Category.objects.all())
    if not categories:
        default_category = Category.objects.create(name="General", description="General events")
        categories.append(default_category)
        print("Created a default category.")

    # Create a few events for today
    for i in range(3):
        event_time = time(random.randint(9, 17), random.choice([0, 30]))
        event = Event.objects.create(
            name=f"Today's Special Event {i+1}",
            description=fake.paragraph(nb_sentences=3),
            date=today,
            time=event_time,
            location=fake.address(),
            category=random.choice(categories)
        )
        print(f"Created event: {event.name} on {event.date}")

if __name__ == "__main__":
    add_todays_events()