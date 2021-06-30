import os.path
import markdown
import re
from jinja2 import evalcontextfilter
from markupsafe import Markup, escape

_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')

@evalcontextfilter
def nl2br(eval_ctx, value):
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', Markup('<br>\n'))
                          for p in _paragraph_re.split(escape(value)))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result


def openFile(file):
    file_path = os.path.join("app/pages/", file)
    with open(file_path, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    

    html = markdown.markdown(text)
    data = {
        "text": html
    }

    return data