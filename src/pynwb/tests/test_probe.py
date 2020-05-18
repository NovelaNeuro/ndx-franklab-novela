import unittest
from unittest.mock import Mock

from src.pynwb.ndx_fl_novela.probe import Probe, Electrode, Shank


class TestElectrode(unittest.TestCase):
    
    def test_electrode_successfully_created(self):
        electrode = Electrode(
            name='0',
            rel_x=1.0,
            rel_y=2.0,
            rel_z=3.0
        )

        self.assertIsInstance(electrode, Electrode)

        self.assertIsInstance(electrode.name, str)
        self.assertIsInstance(electrode.rel_x, float)
        self.assertIsInstance(electrode.rel_y, float)
        self.assertIsInstance(electrode.rel_z, float)

        self.assertEqual(electrode.name, '0')
        self.assertEqual(electrode.rel_x, 1.0)


class TestShank(unittest.TestCase):

    def test_electrode_successfully_created(self):

        mock_electrode_1 = Mock(spec=Electrode)
        mock_electrode_1.name = '1'
        mock_electrode_1.rel_x = 1.0
        mock_electrode_2 = Mock(spec=Electrode)
        mock_electrode_2.name = '2'
        mock_electrode_2.rel_x = 2.0

        shank = Shank(
            name='0',
        )

        shank.add_electrode(mock_electrode_1)
        shank.add_electrode(mock_electrode_2)

        self.assertIsInstance(shank, Shank)

        self.assertIsInstance(shank.name, str)
        self.assertIsInstance(shank.electrodes, dict)
        self.assertIsInstance(shank.electrodes['1'], Electrode)
        self.assertIsInstance(shank.electrodes['1'].rel_x, float)

        self.assertEqual(shank.name, '0')
        self.assertEqual(shank.electrodes, {'1': mock_electrode_1, '2': mock_electrode_2})
        self.assertEqual(shank.electrodes['1'].rel_x, 1.0)


class TestProbe(unittest.TestCase):

    def test_probe_successfully_created(self):
        mock_shank_1 = Mock(spec=Shank)
        mock_shank_2 = Mock(spec=Shank)

        probe = Probe(
            id=1,
            name='Probe1',
            probe_type='type_1',
            units='um',
            probe_description='sample description',
            num_shanks=2,
            contact_side_numbering=True,
            contact_size=1.0,
        )
        probe.add_shank(mock_shank_1)
        probe.add_shank(mock_shank_2)

        self.assertIsInstance(probe, Probe)

        self.assertIsInstance(probe.id, int)
        self.assertIsInstance(probe.name, str)
        self.assertIsInstance(probe.probe_type, str)
        self.assertIsInstance(probe.units, str)
        self.assertIsInstance(probe.probe_description, str)
        self.assertIsInstance(probe.num_shanks, int)
        self.assertIsInstance(probe.contact_side_numbering, bool)
        self.assertIsInstance(probe.contact_size, float)
        self.assertIsInstance(probe.shanks, dict)

        self.assertEqual(probe.id, 1)
        self.assertEqual(probe.name, 'Probe1')
        self.assertEqual(probe.probe_type, 'type_1')
        self.assertEqual(probe.units, 'um')
        self.assertEqual(probe.probe_description, 'sample description')
        self.assertEqual(probe.num_shanks, 2)
        self.assertEqual(probe.contact_side_numbering, True)
        self.assertEqual(probe.contact_size, 1.0)
        self.assertEqual(probe.shanks, {
            mock_shank_1.name: mock_shank_1,
            mock_shank_2.name: mock_shank_2
        })

