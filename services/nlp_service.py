from googletrans import Translator

translator = Translator()

def translate_text(text, dest_lang='en'):
    """Translates text to the destination language."""
    try:
        translation = translator.translate(text, dest=dest_lang)
        return translation.text, translation.src
    except Exception as e:
        print(f"Translation error: {e}")
        return text, 'en' # Fallback to original text

def translate_to_original_lang(text, src_lang):
    """Translates text back to the original source language."""
    if src_lang == 'en':
        return text
    try:
        translation = translator.translate(text, dest=src_lang)
        return translation.text
    except Exception as e:
        print(f"Translation error: {e}")
        return text # Fallback to English text