from json import loads
from random import randint

from bson.json_util import dumps, RELAXED_JSON_OPTIONS
from pymongo import ASCENDING, DESCENDING

import config


def get_document(document_title):
    result = config.mongo.db.exercise.find({'document_title': document_title})
    json_result = loads(dumps(result, json_options=RELAXED_JSON_OPTIONS))
    if len(json_result) == 0:
        return 'Document with title \'' + document_title + '\' was not found.', 404
    return json_result


def get_paragraph(document_title, paragraph_index, ex_types=[]):
    last_para_result = config.mongo.db.exercise.find_one(
            {'document_title': document_title},
            sort=[("paragraph_index", DESCENDING)]
        )

    if not last_para_result:
        return 'Document with title \'' + document_title + '\' was not found.', 404

    last_para_index = last_para_result['paragraph_index']
    if paragraph_index > last_para_index \
            or paragraph_index < -1:
        return 'Paragraph number ' + str(paragraph_index) + ' does not ' + \
               'exist in \'' + document_title + '\'.', 404
    if paragraph_index == -1:
        paragraph_index = randint(0, last_para_index)

    result = config.mongo.db.exercise.find(
        {'document_title': document_title, 'paragraph_index': paragraph_index})
    json_result = loads(dumps(result, json_options=RELAXED_JSON_OPTIONS))

    # Only keep exercise types from ex_types.
    for ex in json_result:
        for j, tw in reversed(list(enumerate(ex['topic_words']))):
            if tw['type'] not in ex_types:
                del ex['topic_words'][j]

    return json_result


def get_document_list():
    result = config.mongo.db.exercise.distinct('document_title')
    json_result = loads(dumps(result, json_options=RELAXED_JSON_OPTIONS))
    return json_result
