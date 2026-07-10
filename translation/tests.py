import requests
from django.test import TestCase
from django.conf import settings
from unittest.mock import patch, Mock

from .service import translate_text


class TranslationServiceTests(TestCase):
    def setUp(self):
        self.original_api_key = settings.SUNBIRD_API_KEY
        settings.SUNBIRD_API_KEY = 'test-key'
        self.api_url = getattr(settings, 'SUNBIRD_API_URL', 'https://api.sunbird.ai/tasks/nllb_translate')

    def tearDown(self):
        settings.SUNBIRD_API_KEY = self.original_api_key

    @patch('translation.service.requests.post')
    def test_translate_text_returns_translated_text(self, mock_post):
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {'output': {'translated_text': 'translated'}}
        mock_post.return_value = mock_response

        translated = translate_text('hello', source_lang='en', target_lang='lug')

        self.assertEqual(translated, 'translated')
        mock_post.assert_called_once_with(
            self.api_url,
            json={'source_language': 'en', 'target_language': 'lug', 'text': 'hello'},
            headers={
                'Authorization': 'Bearer test-key',
                'X-API-Key': 'test-key',
                'Content-Type': 'application/json',
            },
            timeout=10,
        )

    def test_translate_text_same_language_returns_original(self):
        self.assertEqual(translate_text('hello', source_lang='en', target_lang='en'), 'hello')

    @patch('translation.service.requests.post')
    def test_translate_text_on_api_error_returns_original(self, mock_post):
        mock_post.side_effect = requests.RequestException('fail')
        self.assertEqual(translate_text('hello', source_lang='en', target_lang='lug'), 'hello')
