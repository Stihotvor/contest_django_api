from django.core.management.base import BaseCommand, CommandError

from netcovapp.services.coverage_tools import update_coverage


class Command(BaseCommand):
    help = "Updates coverage database with fresh data"

    def handle(self, *args, **options):
        try:
            update_coverage()
            self.stdout.write(self.style.SUCCESS("Coverage has been updated"))
        except Exception as e:
            raise CommandError(e)
