#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Class that treats the details of communication with google translation services
"""

import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error
from . import Languages
import json

def _create_url(word, translation):
    """
    Creates the URL to send to google

    word -- The word to be translated
    translation -- The translation to be performed
    """
    #Url to call the google translate service
    url = b'http://ajax.googleapis.com/ajax/services/language/translate?%s'

    params = urllib.parse.urlencode({"q":word, "langpair":str(translation), "hl":"it",
                               "ie":"UTF-8", "v":"1.0", "oe":"UTF-8"})

    request_url = url % params

    print('Request URL: %s' % request_url)       #TODO -This line is to remove
    return request_url


def translate(word, translation):
    """
    Translates a word

    translation -- The translation requested
    word -- The word to be translated
    """
    request_url =  _create_url(word, translation)
    response = urllib.request.urlopen(request_url.encode("ascii"))

    for text in response:
        jsonText = json.loads(text)
        translated_text = jsonText[b'responseData'][b'translatedText']

    print (translated_text)                       #TODO -This line is to remove
    return translated_text

def test():
    """
    Performs a simple test
    """
    origin_language = Languages.Language(b'PORTUGUESE')
    destiny_language = Languages.Language(b'ENGLISH')
    translation = Languages.Translationn(origin_language, destiny_language)

    assert translate('cadeira', translation) == b"chair"
    assert translate('casa', translation) == b"house"

if __name__ == "__main__":
    test()
