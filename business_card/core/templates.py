import re

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext, ungettext
from jinja2 import nodes
from jinja2.environment import Environment
from jinja2.ext import Extension
from jinja2.loaders import FileSystemLoader

from business_card.settings import TEMPLATE_DIRS, DEBUG

#-------------------------------------------------------------------------------


class Spaceless(Extension):
    """
    Emulates the django spaceless template tag.
    """

    tags = set(['spaceless'])

    def parse(self, parser):
        """
        Parses the statements and calls back to strip spaces.
        """

        lineno = parser.stream.next().lineno
        body = parser.parse_statements(['name:endspaceless'], drop_needle=True)
        return nodes.CallBlock( self.call_method('_render_spaceless'), [], [], body).set_lineno(lineno)

    def _render_spaceless(self, caller=None):
        """
        Strip the spaces between tags using the regular expression
        from django. Stolen from `django.util.html` Returns the given HTML
        with spaces between tags removed.
        """

        if not caller:
            return ''
        return re.sub(r'>\s+<', '><', caller().strip())


#-------------------------------------------------------------------------------


TEMPLATE_SETTINGS = {
    'loader': FileSystemLoader(TEMPLATE_DIRS),
    'auto_reload': DEBUG,
    'autoescape': True,
    'extensions': [
        'jinja2.ext.i18n',
        'jinja2.ext.with_',
        'business_card.core.templates.Spaceless',
    ],
}

TEMPLATE_ENV = Environment(**TEMPLATE_SETTINGS)
TEMPLATE_ENV.install_gettext_callables(ugettext, ungettext)
TEMPLATE_ENV.globals.update(**{
    'url':                  reverse,
})

TEMPLATE_ENV.filters.update(**{

})
