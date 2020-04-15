import unittest

from src.pynwb.ndx_fllab_novela.probe import Probe


class TestProbe(unittest.TestCase):

    def test_probe_successfully_created(self):
        probe = Probe(
            id=1,
            name='Probe1',
            probe_type='type_1',
            units='um',
            num_shanks=2,
            contact_side_numbering=True,
            contact_size=1.0
        )
            
        self.assertIsInstance(probe, Probe)

        self.assertIsInstance(probe.id, int)
        self.assertIsInstance(probe.name, str)
        self.assertIsInstance(probe.probe_type, str)
        self.assertIsInstance(probe.units, str)
        self.assertIsInstance(probe.num_shanks, int)
        self.assertIsInstance(probe.contact_side_numbering, bool)
        self.assertIsInstance(probe.contact_size, float)

        self.assertEqual(probe.id, 1)
        self.assertEqual(probe.name, 'Probe1')
        self.assertEqual(probe.probe_type, 'type_1')
        self.assertEqual(probe.units, 'um')
        self.assertEqual(probe.num_shanks, 2)
        self.assertEqual(probe.contact_side_numbering, True)
        self.assertEqual(probe.contact_size, 1.0)

