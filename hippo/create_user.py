import requests
import json


def main():
    url = 'http://s3.amazonaws.dev:8080/riak-cs/user'
    data = {'email': 'foobar6@localhost', 'name': 'foobar6'}
    response = requests.post(url, json=data)
    response_dict = json.loads(response.text)
    # {
    #     'display_name': 'foobar4',
    #     'email': 'foobar4@localhost',
    #     'key_secret': 'eJK8OQFfge-yv5cTnQCfYYbv6P2DrTQ1lFnLfg==',
    #     'key_id': 'JSLXGTSRAY4CP7WRWT8L',
    #     'name': 'foobar4',
    #     'id': 'cca3924de13d46b57a9f0dcf836cc64cf501b9d72774378a972207f73600f2b9',
    #     'status': 'enabled'
    # }
    id = response_dict['id']
    display_name = response_dict['display_name']
    name = response_dict['name']
    email = response_dict['email']
    key_id = response_dict['key_id']
    key_secret = response_dict['key_secret']
    status = response_dict['status']

    print('id:\t\t\t\t{}'.format(id))
    print('display_name:\t\t\t{}'.format(display_name))
    print('name:\t\t\t\t{}'.format(name))
    print('email:\t\t\t\t{}'.format(email))
    print('key_id:\t\t\t\t{}'.format(key_id))
    print('key_secret:\t\t\t{}'.format(key_secret))
    print('status:\t\t\t\t{}'.format(status))
    

if __name__ == '__main__':
    main()
