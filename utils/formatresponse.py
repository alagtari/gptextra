from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters import HtmlFormatter


def format(text):
    unformatted = text.split('```')
    formatted = []
    for i in range(len(unformatted)) :
        single_response = dict()
        if i%2 == 0 :
            single_response["code"] = False
            single_response['response'] = unformatted[i]
        else:
            single_response['code'] = True
            lexer = guess_lexer(unformatted[i])

            formatter = HtmlFormatter(style='vs')
            highlighted_code = highlight(unformatted[i], lexer, formatter)
            single_response['response'] = highlighted_code
            
        formatted.append(single_response)
    return formatted 
    