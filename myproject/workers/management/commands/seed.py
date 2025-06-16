from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from workers.models import WorkerDetails
from employers.models import Employee  # Adjust if needed
from jobboard.models import Job        # Adjust path if needed
from faker import Faker
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed database with dummy users and jobs'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Seeding data..."))

        fake = Faker()

        # Create Employers and Jobs
        for _ in range(3):
            email = fake.unique.email()
            user = User.objects.create_user(
                email=email,
                password='testpass123',
                user_type='employer'
            )
            employee = Employee.objects.create(
                user=user,
                company_name=fake.company(),
                company_address=fake.address(),
                company_phone_no=fake.phone_number()
            )

            # Each employer creates a few jobs
            for _ in range(2):
                Job.objects.create(
                    posted_by=employee,
                    title=fake.job(),
                    qualifications=fake.sentence(),
                    responsibilities=fake.paragraph(),
                    status=random.choice(['available', 'employed'])
                )

        # Create Workers
        for _ in range(10):
            email = fake.unique.email()
            name = fake.name()
            skills = random.choice(['Plumbing', 'Welding', 'Painting', 'Electrician', 'Cleaning'])
            status = random.choice(['available', 'employed'])

            user = User.objects.create_user(
                email=email,
                password='testpass123',
                user_type='worker'
            )

            WorkerDetails.objects.create(
                user=user,
                name=name,
                email=email,
                skills=skills,
                status=status
            )

        self.stdout.write(self.style.SUCCESS("Seeding completed"))
