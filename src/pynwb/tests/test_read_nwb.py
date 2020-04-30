import os
import unittest

import pynwb
from pynwb import NWBHDF5IO

from datetime import datetime
from dateutil.tz import tzlocal
from pynwb import NWBFile

from src.pynwb.ndx_fl_novela.probe import Probe, Shank, ShanksElectrode


class TestNWBFileReading(unittest.TestCase):

    def read_nwb_without_errors(self):
        start_time = datetime(2017, 4, 3, 11, tzinfo=tzlocal())
        create_date = datetime(2017, 4, 15, 12, tzinfo=tzlocal())
        nwbfile = NWBFile(
            session_description='demonstrate NWBFile basics',
            identifier='NWB123',
            session_start_time=start_time,
            file_create_date=create_date
        )

        nwb_file_handler = NWBHDF5IO('test.nwb', mode='w')
        shanks = Shank(name='shank_1')
        shanks.add_shanks_electrode(ShanksElectrode('n', 1, 2, 3))
        probe = Probe(name='probe', units='asd', id=1, probe_type='ssd', probe_description='2', num_shanks=3, contact_size=1.0,
                      contact_side_numbering=False)
        probe.add_shanks(shanks)
        nwbfile.add_device(probe)
        nwb_file_handler.write(nwbfile)
        nwb_file_handler.close()

        nwb_file_handler = pynwb.NWBHDF5IO('test.nwb', 'r')
        nwb_file = nwb_file_handler.read()

        self.assertTrue(os.path.exists('test.nwb'))
        self.assertIsNotNone(nwb_file)

    def tearDown(self):
        os.remove('test.nwb')
