#
#   SCOREM
#
"""
support
----------

game support utils for the `scorem` module.
"""
import json


def is_valid_json(json_string):
    try:
        result = json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False