from json import loads

from bson.json_util import dumps, RELAXED_JSON_OPTIONS

import config


def get_ex(document_title):
    result = config.mongo.db.exercise.find({"document_title": document_title})
    json_result = loads(dumps(result, json_options=RELAXED_JSON_OPTIONS))
    return json_result

