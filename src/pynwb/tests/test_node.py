import unittest

from src.pynwb.ndx_fllab_novela.apparatus import Node


class TestNode(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.node = Node('NodeName', 10)

    def test_successfulNodeCreation_true(self):
        self.assertIsInstance(self.node, Node)

    def test_checkNodeCorrectValue_true(self):
        self.assertEqual(self.node.name, 'NodeName')
        self.assertEqual(self.node.value, 10)

    def test_checkNodeCorrectType_true(self):
        self.assertIsInstance(self.node.name, str)
        self.assertIsInstance(self.node.value, int)
