from unittest import TestCase
from unittest.mock import Mock

from src.pynwb.ndx_fllab_novela.apparatus import Apparatus, Node, Edge


class TestApparatus(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.node_1 = Mock()
        cls.node_1.__class__ = Node
        cls.node_2 = Mock()
        cls.node_2.__class__ = Node

        cls.node_3 = Mock()
        cls.node_3.__class__ = Node
        cls.node_4 = Mock()
        cls.node_4.__class__ = Node

        cls.edge_1 = Mock()
        cls.edge_1.__class__ = Edge
        cls.edge_2 = Mock()
        cls.edge_2.__class__ = Edge

        cls.apparatus = Apparatus(
            name='ApparatusName',
            edges=[cls.edge_1, cls.edge_2],
            nodes=[cls.node_1, cls.node_2, cls.node_3, cls.node_4]
        )

    def test_successfulEdgeCreation_true(self):
        self.assertIsInstance(self.apparatus, Apparatus)

    def test_checkEdgeCorrectValue_true(self):
        self.assertEqual(self.apparatus.name, 'ApparatusName')
        self.assertEqual(self.apparatus.edges, {self.edge_1.name: self.edge_1,
                                                self.edge_2.name: self.edge_2})
        self.assertEqual(self.apparatus.nodes, {self.node_1.name: self.node_1,
                                                self.node_2.name: self.node_2,
                                                self.node_3.name: self.node_3,
                                                self.node_4.name: self.node_4})

    def test_checkEdgeCorrectType_true(self):
        self.assertIsInstance(self.apparatus.name, str)
        self.assertIsInstance(self.apparatus.edges, dict)
        self.assertIsInstance(self.apparatus.nodes, dict)
