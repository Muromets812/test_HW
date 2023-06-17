import requests

TOKEN = ''


def visit(geo_logs):
    new_lst = []
    for geo_rus in geo_logs:
        for geo_r, g in geo_rus.items():
            if 'Россия' in g:
                new_lst.append(geo_rus)
    return new_lst


def unic_geo_id(ids):
    geo_id = []
    for g in ids.values():
        geo_id += g
    geo_set = set(geo_id)
    geo_id = list(geo_set)
    return geo_id


def search_queries(queries):
    qu = {}
    for result in queries:
        result = len(result.split(' '))
        if result not in qu.keys():
            qu[result] = 1
        else:
            qu[result] += 1
    for k, v in qu.items():
        qu[k] = f'{round(v * 100 / len(queries))} %'
    return qu


class YaUploader:
    def __init__(self, ya_token: str):
        self.ya_token = ya_token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.ya_token)
        }

    def create_path(self, path_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': path_name}
        result = requests.put(url, headers=headers, params=params)
        return result
