from django.core.management.base import BaseCommand
from api.models import User , ActivityPeriod
from datetime import timedelta
from faker import Faker

faker = Faker()
class Command(BaseCommand):
    help = 'Create random Users and Activity period'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            user_id=faker.md5()[::4].upper()
            User.objects.create(user_id=user_id,real_name=faker.name(),tz=faker.timezone())

            for j in range(faker.random_int(1,4)):
                start_time=faker.date_time()
                ActivityPeriod.objects.create(User_id=user_id,start_time = start_time, end_time= start_time+timedelta(hours=2))
        self.stdout.write("%s Fake user details has been created successfully"%total)







