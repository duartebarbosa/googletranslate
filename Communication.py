#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Class that treats the details of communication with google translation services
"""

import urllib
import urllib2
import Languages
import simplejson

def _create_translation_url(word, translation):
    """
    Creates the URL to send to google

    word -- The word to be translated
    translation -- The translation to be performed
    """
    #Url to call the google translate service
    url = u'http://ajax.googleapis.com/ajax/services/language/translate?%s'

    params = urllib.urlencode({"q":word, "langpair":str(translation), "hl":"it",
                               "ie":"UTF-8", "v":"1.0", "oe":"UTF-8"})

    request_url = url % params

    return request_url


def translate(word, translation):
    """
    Translates a word

    translation -- The translation requested
    word -- The word to be translated
    """
    request_url =  _create_translation_url(word, translation)
    response = urllib2.urlopen(request_url.encode("ascii"))

    for text in response:
        json = simplejson.loads(text)
        translated_text = json[u'responseData'][u'translatedText']

    return translated_text


def detection(word):
    """ Detects the language of some word or phrase """

    url = u'http://ajax.googleapis.com/ajax/services/language/translate?%s'

    params = urllib.urlencode({"q":word, "langpair":str(translation), "hl":"it",
                               "ie":"UTF-8", "v":"1.0", "oe":"UTF-8"})

    request_url = url % params

    return detected_language

def test():
    """ Performs a simple test """

    origin_language = Languages.Language(u'PORTUGUESE')
    destiny_language = Languages.Language(u'ENGLISH')
    translation = Languages.Translation(origin_language, destiny_language)

    assert translate('cadeira', translation) == u"chair"
    assert translate('casa', translation) == u"house"

if __name__ == "__main__":
    test()
