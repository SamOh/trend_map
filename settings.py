"""
Project-wide settings for project.
"""

import os

# function to ensure env variables exist
def get_env_variable(var_name):
    try:
        return os.environ.get(var_name)
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise RuntimeError(error_msg)


API_KEY = get_env_variable("API_KEY")
API_SECRET = get_env_variable("API_SECRET")
