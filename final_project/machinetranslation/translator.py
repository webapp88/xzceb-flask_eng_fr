"""import watson translation module"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator('_rCKc1U4O1Jk-u5ks854xCYH-Q3hoaBv3-xj38mjsemx')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com/instances/65d13555-ecb8-4715-9d98-88a548e2f307')



def english_to_french(english_text):
    """english to french translation"""
    frenchtranslation=language_translator.translate(text=english_text,model_id='en-fr').get_result()
    return frenchtranslation.get("translations")[0].get["translation"]


def french_to_english(french_text):
    """frensh to english translation"""
    englishtranslation=language_translator.translate(text=french_text,model_id='fr-en').get_result()
    return englishtranslation.get("translations")[0].get["translation"]
