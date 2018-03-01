import requests


BASE_URL = 'https://qiita.com/api/v2'


def fetch_entries(qiita_id):
    endpoint = '{base_url}/users/{qiita_id}/items'.format(base_url=BASE_URL, qiita_id=qiita_id)
    return requests.get(endpoint)
