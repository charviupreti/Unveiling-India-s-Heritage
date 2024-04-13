from translate import Translator
from iso639 import Lang
from langcodes import *


def translate_it(text, lang):
    """
    Translates the given text to the specified language.

    Parameters:
    text (str): The text to be translated.
    lang (str): The language code for the target language.

    Returns:
    str: The translated text.
    """

    # Convert the language code to ISO 639-1 format
    iso_lang = Lang(lang).pt1

    # Standardize the language tag
    tag = standardize_tag(iso_lang)

    # Initialize the translator with the target language
    translator = Translator(to_lang=tag)

    # Translate the text
    translation = translator.translate(text)

    return translation
