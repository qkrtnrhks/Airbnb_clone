from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User

NAME = "users"


class Command(BaseCommand):

    help = f"This command creats {NAME}"

    def add_arguments(self, parser):  # 명령어에 인자추가하기(예들들어 갯수....)
        parser.add_argument(
            "--number", default=2, type=int, help="How many {NAME} you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(
            User,
            number,
            {
                "is_staff": False,
                "is_superuser": False,
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))