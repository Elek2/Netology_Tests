# само задание
# stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
# print(*[k for k, v in stats.items() if v == max(stats.values())])


# задание для тестов
def max_rate(stats):
	max_rate_name = [k for k, v in stats.items() if v == max(stats.values())]
	return max_rate_name


stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

if __name__ == '__main__':
	print(max_rate(stats))
