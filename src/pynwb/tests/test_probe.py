import unittest

from src.pynwb.ndx_fllab_novela.probe import Probe


class TestProbe(unittest.TestCase):

    def test_probe_successfully_created(self):
        probe = Probe(
            id=1,
            name='Probe1',
            probe_type='type_1',
            units='um',
            probe_description='description of probe',
            num_shanks=2,
            contact_side_numbering=True,
            contact_size=1.0,
            shanks={'shanks': [
                {'shank_id': 0, 'electrodes': [
                    {'id': 0, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0},
                    {'id': 1, 'rel_x': 40, 'rel_y': 0, 'rel_z': 0}]},
                {'shank_id': 1, 'electrodes': [
                    {'id': 32, 'rel_x': 0, 'rel_y': 300, 'rel_z': 0},
                    {'id': 33, 'rel_x': 40, 'rel_y': 300, 'rel_z': 0}]},
            ]}
        )
            
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
        self.assertEqual(probe.probe_description, 'description of probe')
        self.assertEqual(probe.num_shanks, 2)
        self.assertEqual(probe.contact_side_numbering, True)
        self.assertEqual(probe.contact_size, 1.0)
        self.assertEqual(probe.shanks, {'shanks': [
                {'shank_id': 0, 'electrodes': [
                    {'id': 0, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0},
                    {'id': 1, 'rel_x': 40, 'rel_y': 0, 'rel_z': 0}]},
                {'shank_id': 1, 'electrodes': [
                    {'id': 32, 'rel_x': 0, 'rel_y': 300, 'rel_z': 0},
                    {'id': 33, 'rel_x': 40, 'rel_y': 300, 'rel_z': 0}]},
            ]})
