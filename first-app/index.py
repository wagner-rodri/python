def sentenceMaker(phrase):
    interrogatives = ('how', 'what', 'why')
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return '{}?'.format(capitalized)
    else:
        return '{}.'.format(capitalized)
