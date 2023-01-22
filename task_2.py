
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def my_first_solution(ids):
    geo=[]
    for id in ids.values():
        geo += id
    print(set(geo))


def test_solution(ids):
    return set([i for id in ids.values() for i in id])


if __name__ == '__main__':
    my_first_solution(ids)
    print(test_solution(ids))

