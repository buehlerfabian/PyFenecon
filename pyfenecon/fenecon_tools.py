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

REST_URL = f"{config['fenecon_url']}:80/rest/channel"
REST_USER = "x"
REST_PASSWORD = "user"


def get_status():
    session = requests.Session()
    session.auth = (REST_USER, REST_PASSWORD)
    response = session.get(f"{REST_URL}/.*/.*")
    response.raise_for_status()
    session.close()
    return json.loads(response.text)


def get_state_of_charge():
    session = requests.Session()
    session.auth = (REST_USER, REST_PASSWORD)
    response = session.get(f"{REST_URL}/_sum/EssSoc")
    response.raise_for_status()
    session.close()
    return json.loads(response.text)["value"]


def get_battery_power():
    session = requests.Session()
    session.auth = (REST_USER, REST_PASSWORD)
    response = session.get(f"{REST_URL}/ess0/DcDischargePower")
    response.raise_for_status()
    session.close()
    return json.loads(response.text)["value"]


def get_grid_power():
    session = requests.Session()
    session.auth = (REST_USER, REST_PASSWORD)
    response = session.get(f"{REST_URL}/_sum/GridActivePower")
    response.raise_for_status()
    session.close()
    return -json.loads(response.text)["value"]


def get_pv_power():
    session = requests.Session()
    session.auth = (REST_USER, REST_PASSWORD)
    response = session.get(f"{REST_URL}/_sum/ProductionActivePower")
    response.raise_for_status()
    session.close()
    return json.loads(response.text)["value"]


def get_house_power():
    session = requests.Session()
    session.auth = (REST_USER, REST_PASSWORD)
    response = session.get(f"{REST_URL}/_sum/ConsumptionActivePower")
    response.raise_for_status()
    session.close()
    return json.loads(response.text)["value"]
