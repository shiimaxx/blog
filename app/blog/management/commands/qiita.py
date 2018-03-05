from django.core.management.base import BaseCommand, CommandError
from accounts.models import User
from aggregator.models import QiitaEntry

import json

import requests


class Command(BaseCommand):
    help = 'Fetch and save for qiita entries'

    def _fetch_qiita_entries(self, qiita_id):
        base_url = 'https://qiita.com/api/v2'
        endpoint = '{base_url}/users/{qiita_id}/items'.format(base_url=base_url, qiita_id=qiita_id)
        response = requests.get(endpoint)
        return json.loads(response.text)

    def save_qiita_entries(self, users):
        for user in users:
            entries_json = self._fetch_qiita_entries(user.qiita_id)

        entries = []
        for entry_json in entries_json:
            entries.append(
                QiitaEntry(
                    id=entry_json['id'],
                    title=entry_json['title'],
                    url=entry_json['url'],
                    created_at=entry_json['created_at'],
                    user=User.get_from_qiita_id(entry_json['user']['id'])
                )
            )
        QiitaEntry.objects.bulk_create(entries)

    def handle(self, *args, **options):
        users = User.find_qiita_user()
        self.save_qiita_entries(users)