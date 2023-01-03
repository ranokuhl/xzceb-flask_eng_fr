import json
import os
import unittest
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# import machinetranslation.translator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

class TestEnglishToFrench(unittest.TestCase):
    def testEnglishNull(self):
        self.assertNotEqual('', None)

    def testEnglishtoFrench(self):
        frenchText = language_translator.translate(
        text = "Hello",
        model_id ='en-fr').get_result()
        translation = frenchText["translations"][0]["translation"]
        self.assertEqual(translation, "Bonjour")

        
class TestFrenchToEnglish(unittest.TestCase):
    def testFrenchNull(self):
        self.assertNotEqual('', None)

    def testFrenchToEnglish(self):
        englishText = language_translator.translate(
        text = "Bonjour",
        model_id ='fr-en').get_result()
        translation = englishText["translations"][0]["translation"]
        self.assertEqual(translation, "Hello")


unittest.main()