from django.core.management.base import BaseCommand
from rooms.models import Facility

NAME = "facilities"


class Command(BaseCommand):

    help = f"This command creates {NAME}"

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilities:
            Facility.objects.get_or_create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created!"))