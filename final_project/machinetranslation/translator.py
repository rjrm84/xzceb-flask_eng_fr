import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('rtRawnUaJq16n3RGV-Xzi3RerkCyruWFXzmp5RDOZ9EX')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')

# """ Translates English to French """
def englishToFrench (text1):

    frenchtranslation=language_translator.translate(
    text=text1, model_id='en-fr').get_result()
    return frenchtranslation.get("translations") [0].get("translation")

# """ Translates French to English """

def frenchToEnglish  (text1):
    englishtranslation=language_translator.translate(
    text=text1, model_id='fr-en').get_result()
    return englishtranslation.get("translations") [0].get("translation")
