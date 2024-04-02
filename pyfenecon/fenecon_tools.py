import toml
import os
import requests
import json

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

REST_URL = f"{config['fenecon_url1']}:80/rest/channel"
REST_USER = "x"
REST_PASSWORD = "user"


def _get_rest_url(config_number=1):
    url_key = f"fenecon_url{config_number}"
    return f"{config[url_key]}:80/rest/channel"


def get_status(config_number=1):
    session = requests.Session()
    session.auth = (REST_USER, REST_PASSWORD)
    response = session.get(f"{_get_rest_url(config_number)}/.*/.*",
                           timeout=3)
    response.raise_for_status()
    session.close()
    return json.loads(response.text)


def get_state_of_charge(config_number=1):
    session = requests.Session()
    session.auth = (REST_USER, REST_PASSWORD)
    response = session.get(f"{_get_rest_url(config_number)}/_sum/EssSoc",
                           timeout=3)
    response.raise_for_status()
    session.close()
    return json.loads(response.text)["value"]


def get_battery_power(config_number=1):
    session = requests.Session()
    session.auth = (REST_USER, REST_PASSWORD)
    response = session.get(f"{_get_rest_url(config_number)}"
                           "/ess0/DcDischargePower", timeout=3)
    response.raise_for_status()
    session.close()
    return -json.loads(response.text)["value"]


def get_grid_power(config_number=1):
    session = requests.Session()
    session.auth = (REST_USER, REST_PASSWORD)
    response = session.get(f"{_get_rest_url(config_number)}/"
                           "_sum/GridActivePower", timeout=3)
    response.raise_for_status()
    session.close()
    return -json.loads(response.text)["value"]


def get_pv_power(config_number=1):
    session = requests.Session()
    session.auth = (REST_USER, REST_PASSWORD)
    response = session.get(f"{_get_rest_url(config_number)}/"
                           "_sum/ProductionActivePower", timeout=3)
    response.raise_for_status()
    session.close()
    return json.loads(response.text)["value"]


def get_house_power(config_number=1):
    session = requests.Session()
    session.auth = (REST_USER, REST_PASSWORD)
    response = session.get(f"{_get_rest_url(config_number)}/"
                           "_sum/ConsumptionActivePower", timeout=3)
    response.raise_for_status()
    session.close()
    return json.loads(response.text)["value"]
