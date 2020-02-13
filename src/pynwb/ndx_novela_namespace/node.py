from hdmf import docval
from pynwb import register_class, NWBContainer


@register_class('Node', 'ndx-novela-namespace')
class Node(NWBContainer):
    '''A generic graph node. Subclass for more specific types of nodes.
    Attributes
    ----------
    name : str
    value: int
    '''

    __nwbfields__ = ('name',)

    @docval({'name': 'name', 'type': str, 'doc': 'name of this node'},
            {'name': 'value', 'type': int, 'doc': 'value of this node'})
    def __init__(self, **kwargs):
        super(Node, self).__init__(name=kwargs['name'])
        self.value = kwargs['value']
