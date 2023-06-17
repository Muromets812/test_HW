import main
from main import visit, unic_geo_id, search_queries
from main import YaUploader
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']},
]
geo_logs_true = [
    {'visit1': ['Москва', 'Россия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']},
]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]
       }
ids_true = [98, 35, 15, 213, 54, 119]

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]
dict_true = {3: '57 %', 2: '43 %'}


class TestHW:

    def test_visted(self):
        assert visit(geo_logs) == geo_logs_true

    def test_unic(self):
        assert unic_geo_id(ids) == ids_true

    def test_search_queries(self):
        assert search_queries(queries) == dict_true

class TestYA:

    ya_class = YaUploader(main.TOKEN)
    name_folder = 'name_folder'
    FAKE_TOKEN = 'y0_AgAAAAA-UarqAATuwQAAAADltMw7bp76QbCWQPqm1l8vwoysBh2jTqg'

    def test_answer(self, name_folder=name_folder, ya_class=ya_class):
        assert ya_class.create_path(name_folder).status_code == 200

    def test_folder_exist(self, name_folder=name_folder, ya_class=ya_class):
        result = ya_class.create_path(name_folder)
        assert result == 409, 'Folder not exist yet'

    def test_fake_token(self, token=FAKE_TOKEN, name_folder=name_folder):
        f_ya_class = YaUploader(token)
        assert f_ya_class.create_path(name_folder).status_code == 403
