import unittest

from src.pynwb.ndx_fllab_novela.probe import Probe


class TestProbe(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.probe = Probe(
            name='Probe1',
            id=1,
            contact_size=1.0,
            probe_type='type_1',
            num_shanks=2,
            contact_side_numbering=True
        )

    def test_successfulProbeCreation_true(self):
        self.assertIsInstance(self.probe, Probe)

    def test_checkEdgeCorrectValue_true(self):
        self.assertEqual(self.probe.name, 'Probe1')
        self.assertEqual(self.probe.id, 1)
        self.assertEqual(self.probe.contact_size, 1.0)
        self.assertEqual(self.probe.probe_type, 'type_1')
        self.assertEqual(self.probe.num_shanks, 2)
        self.assertEqual(self.probe.contact_side_numbering, True)

    def test_checkEdgeCorrectType_true(self):
        self.assertIsInstance(self.probe.name, str)
        self.assertIsInstance(self.probe.id, int)
        self.assertIsInstance(self.probe.contact_size, float)
        self.assertIsInstance(self.probe.probe_type, str)
        self.assertIsInstance(self.probe.num_shanks, int)