import configparser as cfg

# Standard Variables - does not change from account to account
CONFIG_LOCATION = 'config.cfg'
URL_TEMPLATE = 'api.telegram.org/bot{}'

# Custom variables - changes from account to account
NOTIFICATION_RECIPIENT = XXXXXXXXX
NOTIFICATION_MESSAGE = 'Movement Detected.'

def get_token_from_config_file(config):
    parser = cfg.ConfigParser()
    parser.read(config)
    return parser.get('creds', 'token')