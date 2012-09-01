import sys, os
import optparse

from .Languages import Language, Translation
from .Communication import translate

def main(argv=None):
    """ Function that is called to start the process """
    settings = process_command_line(argv)

    run(settings)

    # run(settings, args)
    return 0        # success

def run(settings):
    """
    Run does the high level translation work receiving
    the settings already parsed
    """
    original_language = Language(settings.origin_language)
    destiny_language = Language(settings.destination_language)
    translation = Translation(original_language, destiny_language)
    word = settings.word

    translated_word = Communication.translate(word, translation)

    print("The translated word is: %s" % translated_word)

    return os.EX_OK #Say that everithing went ok

def process_command_line(argv):
    """
    Return a 2-tuple: (settings object, args list).
    `argv` is a list of arguments, or `None` for ``sys.argv[1:]``.
    """
    if argv is None:
        argv = sys.argv[1:]

    # initialize the parser object:
    parser = optparse.OptionParser(
        formatter=optparse.TitledHelpFormatter(width=78),
        add_help_option=None)

    # define options here:
    parser.add_option(      # customized description; put --help last
        '-h', '--help', action='help',
        help='Show this help message and exit.')

    # define options here:
    parser.add_option(      # word to be translated;
        '-w', '--word', dest='word',
        help="Word to be translated")

    # define options here:
    parser.add_option(      # word to be translated;
        '-o', '--origin-language', dest='origin_language',
        help="Language that the word originally is")

    # define options here:
    parser.add_option(      # word to be translated;
        '-d', '--destination-language', dest='destination_language',
        help="Language to translate the word")

    #List the various languages supported
    parser.add_option("-l", "--list", action="callback",
                      callback=list_all_languages)

    settings, args = parser.parse_args(argv)

    settings.origin_language = settings.origin_language or \
                              input("Origin Language: ")
    settings.destination_language = settings.destination_language or \
                                    input("Destination Language: ")
    settings.word = settings.word or input("Word: ")

    # check number of arguments, verify values, etc.:
    if args:
        parser.error('program takes no command-line arguments; '
                     '"%s" ignored.' % (args,))

    return settings

def list_all_languages():
    """
    Print all the supported languages to the stdout
    """
    print(Language.list_all_languages())
    sys.exit(os.EX_OK)

if __name__ == "__main__":
    try:
        STATUS = main()
        sys.exit(STATUS)
    except Exception as exp:
        print (exp)
        sys.exit(os.EX_SOFTWARE)
