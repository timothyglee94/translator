"""
Translate english words to french
"""
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

URL_LT='####' # pylint: disable=line-too-long
APIKEY_LT='#####'
VERISON_LT='2018-05-01'

authenticator = IAMAuthenticator(APIKEY_LT)
language_translator = LanguageTranslatorV3(version=VERISON_LT,authenticator=authenticator)
language_translator.set_service_url(URL_LT)

def englishtofrench(english_text):
    """
    translates english text to french
    :param text: english text
    :type text: string
    """
    translate_fr = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    translation_fr = translate_fr['translations'][0]['translation']
    return translation_fr

def englishtogerman(english_text):
    """
    translates english text to french
    :param text: english text
    :type text: string
    """
    translate_fr = language_translator.translate(text=english_text, model_id='en-de').get_result()
    translation_fr = translate_fr['translations'][0]['translation']
    return translation_fr

