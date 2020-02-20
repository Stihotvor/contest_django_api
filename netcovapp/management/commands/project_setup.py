from django.core.management.base import BaseCommand, CommandError

from netcovapp.models import Operator


class Command(BaseCommand):
    help = "Operators setup"

    def handle(self, *args, **options):
        try:
            operators = [
                Operator(name='Orange', code=20801),
                Operator(name='SFR', code=20810),
                Operator(name='Free', code=20815),
                Operator(name='Bouygue', code=20820),
                ]
            Operator.objects.bulk_create(operators)
            self.stdout.write(self.style.SUCCESS("Project ready"))
        except Exception as e:
            raise CommandError(e)
