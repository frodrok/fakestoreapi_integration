from django.core.management.base import BaseCommand

from django_q.models import Schedule

class Command(BaseCommand):
    def handle(self, **options):
        Schedule.objects.create(func='fakestoreapi_integration.tasks.fetch_store_api_data', minutes=60, repeats=-50)
        
