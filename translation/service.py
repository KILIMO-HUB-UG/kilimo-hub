"""
Sunbird AI Translation Service
Docs: https://sunbird.ai/
Supports: English <-> Luganda (lug), Acholi (ach), Runyankore (nyn), Lusoga (sog), Ateso (teo)
"""
import requests
from django.conf import settings


SUPPORTED_LANGUAGES = {
    'en':  'English',
    'lug': 'Luganda',
    'ach': 'Acholi',
    'nyn': 'Runyankore',
    'sog': 'Lusoga',
    'teo': 'Ateso',
}


def translate_text(text, source_lang='en', target_lang='lug'):
    """
    Translate text using Sunbird AI.
    Returns translated string, or original text on failure.
    """
    api_key = settings.SUNBIRD_API_KEY
    api_url = getattr(settings, 'SUNBIRD_API_URL', None)

    if not api_url or not api_key or not text.strip():
        return text
    if source_lang == target_lang:
        return text

    headers = {
        'Authorization': f'Bearer {api_key}',
        'X-API-Key': api_key,
        'Content-Type': 'application/json',
    }
    payload = {
        'source_language': source_lang,
        'target_language': target_lang,
        'text': text,
    }

    try:
        resp = requests.post(api_url, json=payload, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        output = data.get('output') or data.get('outputs') or data.get('result') or data
        if isinstance(output, list) and output:
            output = output[0]

        if isinstance(output, dict):
            return (
                output.get('translated_text') or
                output.get('translation') or
                output.get('translated') or
                output.get('result') or
                text
            )
        return output if isinstance(output, str) else text
    except requests.RequestException as e:
        print(f"[Sunbird] Translation error: {e}")
        return text
    except (KeyError, ValueError) as e:
        print(f"[Sunbird] Parse error: {e}")
        return text


def translate_batch(texts, source_lang='en', target_lang='lug'):
    """Translate a list of strings. Returns list of translated strings."""
    return [translate_text(t, source_lang, target_lang) for t in texts]



