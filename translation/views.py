import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .service import translate_text, SUPPORTED_LANGUAGES


@login_required
@require_POST
def translate_view(request):
    """
    AJAX endpoint: POST {text, target_lang}
    Returns {translated, source_lang, target_lang}
    """
    try:
        data = json.loads(request.body)
        text        = data.get('text', '').strip()
        target_lang = data.get('target_lang', 'lug')
        source_lang = data.get('source_lang', 'en')

        if not text:
            return JsonResponse({'error': 'No text provided'}, status=400)
        if target_lang not in SUPPORTED_LANGUAGES:
            return JsonResponse({'error': f'Unsupported language: {target_lang}'}, status=400)

        translated = translate_text(text, source_lang, target_lang)
        return JsonResponse({
            'translated': translated,
            'source_lang': source_lang,
            'target_lang': target_lang,
            'target_name': SUPPORTED_LANGUAGES[target_lang],
        })
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)


def language_options(request):
    """Return supported language list as JSON."""
    return JsonResponse({'languages': SUPPORTED_LANGUAGES})
