"""
Function to read configuration file.
"""
import logging
import yaml

def get_app_config_parameters(app_config_file):
    """
    Function to read yaml file.

    Args:
        :param  app_config_file: yaml file

    Returns:
        config_dict: config file
    """
    try:
        logging.info('In get_app_config_parameters: Parsing app config parameter from: %s.',
                     app_config_file)
        with open(app_config_file, 'r', encoding="utf8") as stream:
            try:
                config_dict = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                logging.exception('Error reading config file %s', exc)
                raise RuntimeError(f'In get_app_config_parameters: Missing config file at: '
                                   f'{app_config_file}') from exc
    except Exception as err:
        logging.exception("In get_app_config_parameters: %s", err)
        raise RuntimeError(f'In get_app_config_parameters: Problem in the config file at: '
                           f'{app_config_file}') from err
    return config_dict
