import toml
import os
import requests

# read config file
try:
    with open('pyfeneconrc', 'r') as f:
        config = toml.load(f)
except FileNotFoundError:
    home = os.path.expanduser('~')
    try:
        with open(f'{home}/.config/pyfeneconrc', 'r') as f:
            config = toml.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(
            'No pyfeneconrc file found in working directory'
            ' or in ~/.config directory.')

REST_URL = f"{config['fenecon_url']}:80/rest/channel"
REST_USER = "x"
REST_PASSWORD = "user"


def get_status():
    pass


def get_State_of_charge():
    session = requests.Session()
    session.auth = (REST_USER, REST_PASSWORD)
    response = session.get(f"{REST_URL}/_sum/EssSoc")
    response.raise_for_status()
    return response
