from hdmf import docval
from pynwb import register_class, NWBContainer


@register_class('Edge', 'ndx-novela-namespace')
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
