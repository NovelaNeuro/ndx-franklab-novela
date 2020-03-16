import unittest
from unittest.mock import Mock

from pynwb.device import Device

from src.pynwb.ndx_fllab_novela.nwb_electrode_group import NwbElectrodeGroup


class TestNwbElectrodeGroup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mock_device = Mock()
        cls.mock_device.__class__ = Device

        cls.nwb_electrode_group = NwbElectrodeGroup(
            name='NwbElectrodeGroup1',
            id=1,
            description='Sample description',
            location='Sample location',
            device=cls.mock_device,
        )

    def test_successfulNodeCreation_true(self):
        self.assertIsInstance(self.nwb_electrode_group, NwbElectrodeGroup)

    def test_checkNodeCorrectValue_true(self):
        self.assertEqual(self.nwb_electrode_group.name, 'NwbElectrodeGroup1')
        self.assertEqual(self.nwb_electrode_group.description, 'Sample description')
        self.assertEqual(self.nwb_electrode_group.location, 'Sample location')
        self.assertEqual(self.nwb_electrode_group.device, self.mock_device)
        self.assertEqual(self.nwb_electrode_group.id, 1)

    def test_checkNodeCorrectType_true(self):
        self.assertIsInstance(self.nwb_electrode_group.name, str)
        self.assertIsInstance(self.nwb_electrode_group.description, str)
        self.assertIsInstance(self.nwb_electrode_group.location, str)
        self.assertIsInstance(self.nwb_electrode_group.device, Device)
        self.assertIsInstance(self.nwb_electrode_group.id, int)
