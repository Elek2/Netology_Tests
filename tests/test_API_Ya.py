import requests
import pytest


def connect():
	token = open("./Ya_token.txt", "r").read()
	par = {
		'ya_url': 'https://cloud-api.yandex.net/v1/disk/resources',
		'ya_headers': {
			'Content-Type': 'application/json',
			'Authorization': f'OAuth {token}'
		}
	}
	return par

def create_folder(name):
	response = requests.put(connect()['ya_url'], headers=connect()['ya_headers'], params={"path": name})
	print(response.json())
	return response

@pytest.mark.parametrize('fol_name', ['aaa', 'bbb', 'acccaa', 'aaavaa'])
def test_response(fol_name):
	res = create_folder(fol_name)
	assert res.status_code == 201

def test_folder_exist():
	res = requests.get(connect()['ya_url'], headers=connect()['ya_headers'], params={"path": 'aaa'})
	assert res.status_code == 200

@pytest.mark.xfail
def test_wrong():
	res = requests.get(connect()['ya_url'], headers=connect()['ya_headers'], params={"path": 'new'})
	assert res.status_code == 200


# if __name__ == '__main__':
# 	create_folder('112')
