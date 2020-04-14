import unittest
from unittest.mock import Mock

from pynwb.device import Device

from src.pynwb.ndx_fllab_novela.ntrode import NTrode


class TestNTrode(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mock_device = Mock()
        cls.mock_device.__class__ = Device

        cls.ntrode = NTrode(
            name='NTrode1',
            description='Sample description',
            location='Sample location',
            device=cls.mock_device,
            ntrode_id=1,
            electrode_group_id=1,
            bad_channels=[1, 3],
            map=[[1, 2], [3, 4], [5, 6]]
        )

    def test_successfulNodeCreation_true(self):
        self.assertIsInstance(self.ntrode, NTrode)

    def test_checkNodeCorrectValue_true(self):
        self.assertEqual(self.ntrode.name, 'NTrode1')
        self.assertEqual(self.ntrode.description, 'Sample description')
        self.assertEqual(self.ntrode.location, 'Sample location')
        self.assertEqual(self.ntrode.device, self.mock_device)
        self.assertEqual(self.ntrode.ntrode_id, 1)
        self.assertEqual(self.ntrode.electrode_group_id, 1)
        self.assertEqual(self.ntrode.bad_channels, [1,3])
        self.assertEqual(self.ntrode.map, [[1, 2], [3, 4], [5, 6]])

    def test_checkNodeCorrectType_true(self):
        self.assertIsInstance(self.ntrode.name, str)
        self.assertIsInstance(self.ntrode.description, str)
        self.assertIsInstance(self.ntrode.location, str)
        self.assertIsInstance(self.ntrode.device, Device)
        self.assertIsInstance(self.ntrode.ntrode_id, int)
        self.assertIsInstance(self.ntrode.electrode_group_id, int)
        self.assertIsInstance(self.ntrode.map, list)