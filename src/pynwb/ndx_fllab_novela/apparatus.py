from hdmf import docval
from pynwb import register_class
from pynwb.core import MultiContainerInterface, NWBContainer


@register_class('Edge', 'ndx-fllab-novela')
class Edge(NWBContainer):
    '''An undirected edge connecting two nodes in a graph.
    Attributes
    ----------
    name : str
    edge_nodes : iterable
        The names of the two Node objects connected by this edge (e.g.
        [node1 name, node2 name])
    '''

    __nwbfields__ = ('name', 'edge_nodes')

    @docval({'name': 'name', 'type': str, 'doc': 'name of this segement node'},
            {'name': 'edge_nodes', 'type': ('array_data', 'data'),
             'doc': 'the names of the two nodes in this undirected edge'})
    def __init__(self, **kwargs):
        super(Edge, self).__init__(name=kwargs['name'])
        self.edge_nodes = kwargs['edge_nodes']


@register_class('Node', 'ndx-fllab-novela')
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


@register_class('Apparatus', 'ndx-fllab-novela')
class Apparatus(MultiContainerInterface):
    """Topological graph representing connected components of a behavioral
    apparatus.
    Attributes
    ----------
    name : str
    nodes : list
        Node objects contained in this apparatus
    edges : list
        Edge objects contained in this apparatus
    """

    __nwbfields__ = ('name', 'edges', 'nodes')

    __clsconf__ = [
        {
            'attr': 'edges',
            'type': Edge,
            'add': 'add_edge',
            'get': 'get_edge'
        },
        {
            'attr': 'nodes',
            'type': Node,
            'add': 'add_node',
            'get': 'get_node'
        }
    ]
    __help = 'info about an apparatus.py'
