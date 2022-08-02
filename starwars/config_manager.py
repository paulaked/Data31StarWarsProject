from definitions import PROJECT_ROOT_DIR
import configparser
import os

_config = configparser.ConfigParser()

_config.read(os.path.join(PROJECT_ROOT_DIR, 'config.ini'))

SWAPI_STARSHIPS = _config['default']['starships']
FAKE_URL = _config['default']['fake_url']
DATABASE = _config['default']['database']