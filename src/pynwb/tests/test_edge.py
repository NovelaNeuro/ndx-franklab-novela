import unittest
from unittest.mock import Mock

from src.pynwb.ndx_fllab_novela.apparatus import Node, Edge


class TestEdge(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.node_1 = Mock()
        cls.node_1.__class__ = Node
        cls.node_2 = Mock()
        cls.node_2.__class__ = Node

        cls.edge = Edge('EdgeName', [cls.node_1, cls.node_2])

    def test_successfulEdgeCreation_true(self):
        self.assertIsInstance(self.edge, Edge)

    def test_checkEdgeCorrectValue_true(self):
        self.assertEqual(self.edge.name, 'EdgeName')
        self.assertEqual(self.edge.edge_nodes, [self.node_1, self.node_2])

    def test_checkEdgeCorrectType_true(self):
        self.assertIsInstance(self.edge.name, str)
        self.assertIsInstance(self.edge.edge_nodes, list)
