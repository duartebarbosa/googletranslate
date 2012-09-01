import sys, os
import optparse

from Languages import Language, Translation
import Communication

def main(argv=None):
    """ Function that is called to start the process """
    
    print "\nPython - Google Translate Api\nFor help, add the --help flag on command prompt."  
    settings = process_command_line(argv)

    run(settings)

    # run(settings, args)
    print "\nThanks for your flops! Greatly apreciated :)\n\t\t\t\t\t\t\t\t...better go. kill dash 9 is coming!\n"

    return 0        # success

def run(settings):
    """ Run does the high level translation work receiving the settings already parsed """

    original_language = Language(Language.languages_choose[int(settings.origin_language) - 1])
    destiny_language = Language(Language.languages_choose[int(settings.destination_language) - 1])
    translation = Translation(original_language, destiny_language)
    word = settings.word

    translated_word = Communication.translate(word, translation)

    print "\nThe translated word is: %s" % translated_word
    again = raw_input("Do you wish to translate any more words from %s to %s? [y/n]: " % (original_language, destiny_language))

    if again == 'y':
    	word2 = raw_input("Please type the Word:")
    	settings.word = word2
    	run(settings)
    elif again == 'n':
    	again2 = raw_input("Do you wish to translate any more words? [y/n] ")
    	if again2 == 'y':
    		settings = process_command_line(None)
		run(settings)
	else:
		return os.EX_OK # Returns everything went ok to the environment
    else:
	print "wtf? You are doing it Wrong. Quiting!"
	# sometimes I just miss goto statement. Am I weird? bah.
	return 1

def process_command_line(argv):
    """
    Return a 2-tuple: (settings object, args list).
    `argv` is a list of arguments, or `None` for ``sys.argv[1:]``.
    """
    if argv is None:
        argv = sys.argv[1:]

    # initialize the parser object:
    parser = optparse.OptionParser(
        formatter = optparse.TitledHelpFormatter(width = 78),
        add_help_option = None)

    # define options here:
    parser.add_option(      # customized description; put --help last
        '-h', '--help', action = 'help',
        help = "Show this help message and exit.")

    # define options here:
    parser.add_option(      # word to be translated;
        '-w', '--word', dest = 'word',
        help = "Word to be translated")

    # define options here:
    parser.add_option(      # word to be translated;
        '-o', '--origin-language', dest='origin_language',
        help = "Original Language of the word")

    # define options here:
    parser.add_option(      # word to be translated;
        '-d', '--destination-language', dest = 'destination_language',
        help = "Language to translate the word")

    #List the various languages supported
    parser.add_option("-l", "--list", action = "callback",
                      callback = list_all_languages)

    settings, args = parser.parse_args(argv)

    list_all_languages_column()

    settings.origin_language = settings.origin_language or \
    			       raw_input("\nOrigin Language, please choose the desired number: ")
			       
    settings.destination_language = settings.destination_language or \
                                    raw_input("Destination Language, please choose the desired number: ")
    settings.word = settings.word or raw_input("Please type the Word: ")
	
    if settings.origin_language == settings.destination_language:	
	print "\nThat was a bit dumb, don't you think?.."
	
    # check number of arguments, verify values, etc.:
    if args:
        parser.error('program takes no command-line arguments; '
                     '"%s" ignored.' % (args,))

    return settings

def list_all_languages():
    """ Print all the supported languages to the stdout """

    print Language.list_all_languages()
    sys.exit(os.EX_OK)

def list_all_languages_column():
    print "\nAvailable Languages:"
    for i in xrange(1,20):
    	print "[%s] %s\t\t\t[%s] %s" % (i, Language.languages_choose[i - 1], (i + 17), Language.languages_choose[i + 16])


if __name__ == "__main__":
    try:
        STATUS = main()
        sys.exit(STATUS)
    except Exception, exp:
        print exp
        sys.exit(os.EX_SOFTWARE)
