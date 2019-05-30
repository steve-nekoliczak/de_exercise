from json import loads
import re
import requests

from api_settings.nlp import process_sentences_url as url
import config


def tokenize_sentence(snt):
    return requests.get(url=url,
                        params={'sentences_str': snt})


def build_topic_words_list(snt):
    found_tw = False
    nlp_results = loads(tokenize_sentence(snt).content)[0]
    tws = []

    # Step through each word in the processed sentence.
    for token in nlp_results:

        tw = {}
        if 'PronType' in token['feats'] \
                and token['feats']['PronType'] == 'Art':
            tw['type'] = 'article'
            found_tw = True

        if token['pos'] == 'ADJ':
            tw['type'] = 'adjective'
            found_tw = True

        if token['pos'] == 'VERB':
            tw['type'] = 'verb'
            found_tw = True

        if found_tw:
            tw['feats'] = token['feats']
            tw['text'] = token['text']
            tw['lemma'] = token['lemma']
            tw['pos'] = token['pos']
            tw['index'] = token['index']
            tws.append(tw)

        found_tw = False

    return tws


def generate_ex(filepath, document_title, document_author):
    with open(filepath) as f:

        end_snt_regex = re.compile(r'[.!?]')
        blank_line_regex = re.compile(r'^[\s]*$')

        lines = f.readlines()

        snt = ''
        para_index = -1

        for line in lines:

            # Found blank line
            if blank_line_regex.search(line):
                continue

            words = line.split(' ')

            para_start = True
            para_index += 1
            snt_index = 0

            for word in words:
                snt += word + ' '

                # Got a full sentence
                if end_snt_regex.search(word):

                    ex = {}
                    ex['document_title'] = document_title
                    ex['document_author'] = document_author
                    ex['paragraph_start'] = para_start
                    ex['paragraph_index'] = para_index
                    ex['sentence_index'] = snt_index
                    ex['sentence_text'] = snt
                    ex['topic_words'] = build_topic_words_list(snt)

                    config.mongo.db.exercise.insert(ex)

                    snt = ''
                    snt_index += 1
                    para_start = False

