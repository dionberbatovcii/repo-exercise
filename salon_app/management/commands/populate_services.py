from django.core.management.base import BaseCommand
from salon_app.models import Service
from decimal import Decimal

class Command(BaseCommand):
    help = 'Populates the database with sample services'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Deleting existing services...'))
        Service.objects.all().delete()

        services_data = [
            {
                'name': 'Classic Haircut & Style',
                'description': 'A timeless cut and style tailored to your preference, includes wash and blow-dry.',
                'price': Decimal('55.00')
            },
            {
                'name': 'Luxury Manicure',
                'description': 'Pamper your hands with a shaping, cuticle care, massage, and polish application.',
                'price': Decimal('35.00')
            },
            {
                'name': 'Rejuvenating Facial',
                'description': 'A deep cleansing and hydrating facial to refresh and revitalize your skin.',
                'price': Decimal('75.00')
            },
            {
                'name': 'Swedish Massage (60 min)',
                'description': 'A relaxing full-body massage to ease tension and improve circulation.',
                'price': Decimal('90.00')
            },
            {
                'name': 'Bridal Makeup Package',
                'description': 'Complete makeup application for your special day, including a trial session.',
                'price': Decimal('150.00')
            }
        ]

        self.stdout.write(self.style.SUCCESS('Creating sample services...'))
        for service_data in services_data:
            Service.objects.create(**service_data)

        self.stdout.write(self.style.SUCCESS(f'Successfully populated {len(services_data)} services.'))
