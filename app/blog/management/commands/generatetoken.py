from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token

from accounts.models import User


class Command(BaseCommand):
    help = 'Generationg Tokens'

    def handle(self, *args, **options):
        print('Generate created users tokens')
        for user in User.objects.all():
            token = Token.objects.get_or_create(user=user)
            print('{} {}'.format(user, token[0]))
