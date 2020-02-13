import unittest
from unittest.mock import Mock

from pynwb.device import Device

from src.pynwb.ndx_novela_namespace.fl_electrode_group import FLElectrodeGroup


class TestFLElectrodeGroup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mock_device = Mock()
        cls.mock_device.__class__ = Device

        cls.fl_electrode_group = FLElectrodeGroup(
            name='FLElectrodeGroup1',
            id=1,
            description='Sample description',
            location='Sample location',
            device=cls.mock_device,
        )

    def test_successfulNodeCreation_true(self):
        self.assertIsInstance(self.fl_electrode_group, FLElectrodeGroup)

    def test_checkNodeCorrectValue_true(self):
        self.assertEqual(self.fl_electrode_group.name, 'FLElectrodeGroup1')
        self.assertEqual(self.fl_electrode_group.description, 'Sample description')
        self.assertEqual(self.fl_electrode_group.location, 'Sample location')
        self.assertEqual(self.fl_electrode_group.device, self.mock_device)
        self.assertEqual(self.fl_electrode_group.id, 1)

    def test_checkNodeCorrectType_true(self):
        self.assertIsInstance(self.fl_electrode_group.name, str)
        self.assertIsInstance(self.fl_electrode_group.description, str)
        self.assertIsInstance(self.fl_electrode_group.location, str)
        self.assertIsInstance(self.fl_electrode_group.device, Device)
        self.assertIsInstance(self.fl_electrode_group.id, int)
