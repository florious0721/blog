from docutils import nodes
from sphinx.application import Sphinx
from sphinx.directives import SphinxDirective
from sphinx.roles import SphinxRole
from sphinx.util import logging
from sphinx.util.nodes import make_id

log = logging.getLogger(__name__)

class LeetCodeRole(SphinxRole):
    objtype = 'exercise'
    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        code = self.text
        label = f'lc{code.lower()}'
        url = f'https://lcid.cc/cn/{code}'
        display = f'力扣 {code}'

        nid = make_id(self.env, self.inliner.document, self.objtype, label)
        tg = nodes.target(
            '', '', ids=[nid]
        )
        ref = nodes.reference(
            url, display,
            refuri=url,
            internal=False
        )

        #self.inliner.document.note_explicit_target(tg)

        std = self.env.domains.standard_domain # TODO
        std.note_hyperlink_target(label, self.env.docname, nid, display)

        return [tg, ref], []

class LuoguRole(SphinxRole): # Generate label like `lgp39`
    objtype = 'exercise'
    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        code = self.text
        label = f'lg{code.lower()}'
        url = f'https://www.luogu.com.cn/problem/{code}'
        display = f'洛谷 {code}'

        nid = make_id(self.env, self.inliner.document, self.objtype, label)
        tg = nodes.target(
            '', '', ids=[nid]
        )
        ref = nodes.reference(
            url, display,
            refuri=url,
            internal=False
        )
        #self.inliner.document.note_explicit_target(tg)

        std = self.env.domains.standard_domain # TODO
        std.note_hyperlink_target(label, self.env.docname, nid, display)

        return [tg, ref], []

class VJudgeRole(SphinxRole): # Generate label like `vjhdu-1213`
    objtype = 'exercise'
    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        code = self.text
        label = f'vj{code.lower()}'
        url = f'https://vjudge.net/problem/{code}'
        display = f'VJudge {code}'

        nid = make_id(self.env, self.inliner.document, self.objtype, label)
        tg = nodes.target(
            '', '', ids=[nid]
        )
        ref = nodes.reference(
            url, display,
            refuri=url,
            internal=False
        )
        #self.inliner.document.note_explicit_target(tg)

        std = self.env.domains.standard_domain # TODO
        std.note_hyperlink_target(label, self.env.docname, nid, display)

        return [tg, ref], []

def setup(app: Sphinx):
    app.add_role('leetcode', LeetCodeRole())
    app.add_role('luogu', LuoguRole())
    app.add_role('vjudge', VJudgeRole())
    return {
        'version': '0.0.3',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
