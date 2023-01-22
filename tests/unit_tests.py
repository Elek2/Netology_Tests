import task_1, task_2, task_4
from unittest import TestCase


class TestTask1(TestCase):

	def test_Russia(self):
		geo_logs_russia = [
			{'visit1': ['Москва', 'Россия']},
			{'visit3': ['Владимир', 'Россия']},
			{'visit7': ['Тула', 'Россия']},
			{'visit8': ['Тула', 'Россия']},
			{'visit9': ['Курск', 'Россия']},
			{'visit10': ['Архангельск', 'Россия']}
		]
		self.assertEqual(task_1.geo_filter(task_1.geo_logs, 'Россия'), geo_logs_russia)

	def test_Portugal(self):
		geo_logs_portugal = [
			{'visit4': ['Лиссабон', 'Португалия']},
			{'visit6': ['Лиссабон', 'Португалия']}
		]
		self.assertEqual(task_1.geo_filter(task_1.geo_logs, 'Португалия'), geo_logs_portugal)


class TestTask2(TestCase):

	def test_ids(self):
		ids_result = {98, 35, 15, 213, 54, 119}
		self.assertEqual(task_2.test_solution(task_2.ids), ids_result)


class TestTask3(TestCase):

	def test_rate(self):
		res = task_4.max_rate(task_4.stats)
		self.assertIsInstance(res, list)
		self.assertIn('yandex', res)