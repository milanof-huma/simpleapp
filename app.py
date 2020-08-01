import json
import os
import random
import sys
from typing import OrderedDict

from flask import Flask
import logging

from pythonjsonlogger import jsonlogger

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

logger = logging.getLogger(__name__)


def setup_log():
    def json_translate(*args, **kwargs):
        if len(args) > 0:
            if isinstance(args[0], OrderedDict):
                level_name = args[0].get("levelname", None)
                args[0]["level"] = level_name
                args[0]["severity"] = level_name
        return json.dumps(*args, **kwargs)

    class SpecialJsonFormatter(jsonlogger.JsonFormatter):

        def __init__(self, *args, **kwargs):
            super().__init__(json_serializer=json_translate, json_encoder=json.JSONEncoder,
                             fmt="%(asctime)sZ %(levelname)s [%(name)s:%(funcName)s:%(lineno)s] %(message)s", *args,
                             **kwargs)

    if (len(sys.argv) > 1 and sys.argv[1] == 'enable_json_logging') or os.environ.get('ENABLE_JSON_LOGGING'):
        log_handler = logging.StreamHandler()
        formatter = SpecialJsonFormatter()
        log_handler.setFormatter(formatter)
        logger.addHandler(log_handler)


setup_log()


def get_random_message():
    log_messages = ('Brown fox jumped', 'Black pant run', 'Great bear :-)')
    return log_messages[random.randint(0, len(log_messages) - 1)]


@app.route('/log', defaults={'level': 'debug'})
@app.route('/log/<level>')
def hello_world(level: str):
    lower_case_level = level.lower()

    if lower_case_level == 'error':
        logger.error(get_random_message())
        return 'internal server error', 500
    elif lower_case_level == 'warning':
        logger.warning(get_random_message())
        return '', 401
    elif lower_case_level == 'info':
        logger.info(get_random_message())
        return {'foo': 'bar'}, 200

    logger.debug(get_random_message())
    return {'bar': 'foobar'}, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
