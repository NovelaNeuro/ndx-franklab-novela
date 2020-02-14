from pynwb import register_class
from pynwb.core import MultiContainerInterface

from src.pynwb.ndx_franklab_novela.edge import Edge
from src.pynwb.ndx_franklab_novela.node import Node


@register_class('Apparatus', 'ndx-franklab-novela')
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
