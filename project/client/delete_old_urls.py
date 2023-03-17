from django.core.management.base import BaseCommand
from django.utils import timezone
from .models import URL

class Command(BaseCommand):
    help = 'Deletes URLS older than 30 days'

    def handle(self, *args, **options):
        URL.objects.filter(created_date__lt=timezone.now() - timezone.timedelta(days=30)).delete()
