import pdb
"""
File where all the details of languages supported by the
google translation service are specified.
"""

class Language(object):
    """
    This class represents a language
    """

    languages = {
        'ARABIC' : "ar",
        'CHINESE' : "zh",
        'CHINESE_SIMPLIFIED' : "zh-CN",
        'CHINESE_TRADITIONAL' : "zh-TW",
        'DUTCH' : "nl",
        'ENGLISH' : "en",
        'FRENCH' : "fr",
        'GERMAN' : "de",
        'GREEK' : "el",
        'ITALIAN' : "it",
        'JAPANESE' : "ja",
        'KOREAN' : "ko",
        'PORTUGUESE' : "pt",
        'RUSSIAN' : "ru",
        'SPANISH' : "es",
    }

    def __init__(self, language):
        """
        Constructor.

        language -- The language string in all uppercase
        """
        try:
            print(language)
            self._language =  Language.languages[language]
        except:
            raise Exception ("Language %s doesn't exist" % language)

    def __str__(self):
        return self._language

    def __cmp__(self, other):
        return cmp(self._language, other._language)

    @staticmethod
    def list_all_languages(separator="\n"):
        """ Returns a string with all available languages (one per line) """
        return str(separator).join(k for k in list(Language.languages.keys()))

class Translation(object):
    """
    This class represents a translation between two langagues
    """
    translation_pairs = (
            (Language('ARABIC'), Language('ENGLISH')),
            (Language('CHINESE'), Language('ENGLISH')),
            (Language('CHINESE_SIMPLIFIED'), Language('CHINESE_TRADITIONAL')),
            (Language('CHINESE_TRADITIONAL'), Language('CHINESE_SIMPLIFIED')),
            (Language('DUTCH'), Language('ENGLISH')),
            (Language('ENGLISH'), Language('ARABIC')),
            (Language('ENGLISH'), Language('CHINESE')),
            (Language('ENGLISH'), Language('CHINESE_SIMPLIFIED')),
            (Language('ENGLISH'), Language('CHINESE_TRADITIONAL')),
            (Language('ENGLISH'), Language('DUTCH')),
            (Language('ENGLISH'), Language('FRENCH')),
            (Language('ENGLISH'), Language('GERMAN')),
            (Language('ENGLISH'), Language('GREEK')),
            (Language('ENGLISH'), Language('ITALIAN')),
            (Language('ENGLISH'), Language('JAPANESE')),
            (Language('ENGLISH'), Language('KOREAN')),
            (Language('ENGLISH'), Language('PORTUGUESE')),
            (Language('ENGLISH'), Language('RUSSIAN')),
            (Language('ENGLISH'), Language('SPANISH')),
            (Language('FRENCH'), Language('ENGLISH')),
            (Language('FRENCH'), Language('GERMAN')),
            (Language('GERMAN'), Language('ENGLISH')),
            (Language('GERMAN'), Language('FRENCH')),
            (Language('GREEK'), Language('ENGLISH')),
            (Language('ITALIAN'), Language('ENGLISH')),
            (Language('JAPANESE'), Language('ENGLISH')),
            (Language('KOREAN'), Language('ENGLISH')),
            (Language('PORTUGUESE'), Language('ENGLISH')),
            (Language('RUSSIAN'), Language('ENGLISH')),
            (Language('SPANISH'), Language('ENGLISH')),
    )

    @staticmethod
    def is_valid_language_pair(language_origin, language_destiny):
        """ Checks if a language pair to be translated is valid """
        return (language_origin, language_destiny) \
               in Translation.translation_pairs

    def __init__(self, language_origin, language_destiny):
        """
        Creates a language pair where it is
        possible to translate languageA to languageB

        language_origin -- The origin language (Language)
        language_destiny -- The destination language (Language)
        """
        print ("3JJAODJIDOIJAWOJI")
        if not Translation.is_valid_language_pair(language_origin,
                                                  language_destiny):
            raise Exception (('translation %s to %s not valid'
                              % (language_origin, language_destiny)))

        self.language_origin = language_origin
        self.language_destiny = language_destiny

    def __str__(self):
        """
        """
        return  b'%s|%s' % (self.language_origin, self.language_destiny)

def test_translation():
    """
    Tests if translation classes and language classes
    are functioning properly
    """
    pt_language = Language("PORTUGUESE")
    en_language = Language("ENGLISH")

    translation = Translation(pt_language, en_language)

    assert translation.language_origin == pt_language
    assert translation.language_destiny == en_language
    assert str(translation) == "pt|en"

    sp_language = Language("SPANISH")
    assert sp_language

if __name__ == "__main__":
    test_translation()
