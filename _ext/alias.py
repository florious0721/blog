from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.docutils import ReferenceRole, SphinxRole

class InterfaceRole(ReferenceRole):
    def run(self) -> tuple[[nodes.Node], [nodes.system_message]]:
        return ([nodes.literal(self.rawtext, self.text)], [])

class GLinkRole(ReferenceRole):
    module_prefix: dict[str, str] = {
        'glib': 'G',
        'gobject': 'G',
        'gtk4': 'Gtk',
    }

    def run(self) -> tuple[[nodes.Node], [nodes.system_message]]:
        module, t, name = self.text.split('.')

        uri = f'https://docs.gtk.org/{module}/{t}.{name}.html'

        prefix = self.module_prefix[module]

        if t in ('alias', 'class', 'enum', 'flags', 'struct', 'union'):
            name = prefix + name
        elif t in ('callback', 'func'):
            if name.isupper():
                name = f'{prefix.upper()}_{name}'
            else:
                name = f'{prefix.lower()}_{name}'
        elif t == 'const':
            name = f'{prefix.upper()}_{name}'
        else:
            raise ValueError()


        n = nodes.literal('', '')
        n += nodes.reference(
            self.rawtext, name,
            internal=False, refuri=uri
        )

        return ([n], [])

def setup(app: Sphinx):
    app.add_role('interface', InterfaceRole())
    app.add_role('glink', GLinkRole())
    return {
        'version': '0.0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
