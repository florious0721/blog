from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.docutils import ReferenceRole, SphinxRole

class InterfaceRole(ReferenceRole):
    def run(self) -> tuple[[nodes.Node], [nodes.system_message]]:
        return ([nodes.literal(self.text, self.text)], [])

def setup(app: Sphinx):
    app.add_role('interface', InterfaceRole())
    return {
        'version': '0.0.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
