import logging

import yaml


def get_config_parameters(app_config_file: str) -> dict:
    """
    Function to read yaml file.

    Args:
        :param  app_config_file: yaml file

    Returns:
        config_dict: config file
    """
    try:
        logging.info(f"In get_config_parameters: Parsing app config parameter from: "
                     f"{app_config_file}")
        config_dict = read_config_parameters(app_config_file)
    except Exception as ex:
        logging.exception(f"In get_config_parameters: {ex}")
        raise RuntimeError(f"In get_config_parameters: Problem in the config file at: "
                           f"{app_config_file}")

    return config_dict


def read_config_parameters(app_config_file: str) -> dict:
    with open(app_config_file, "r") as stream:
        try:
            config_dict = yaml.safe_load(stream)
        except yaml.YAMLError as ex:
            logging.exception(f"Error reading config file {ex}")
            raise RuntimeError(f"In get_config_parameters: Missing config file at: "
                               f"{app_config_file}")
    return config_dict
