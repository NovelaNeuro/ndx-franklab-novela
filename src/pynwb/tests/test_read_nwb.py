import unittest
import os

import pynwb
from pynwb import NWBHDF5IO

from datetime import datetime
from dateutil.tz import tzlocal
from pynwb import NWBFile

from src.pynwb.ndx_fl_novela.header_device import HeaderDevice
from src.pynwb.ndx_fl_novela.probe import Probe, Shank, ShanksElectrode


class TestNWBFileReading(unittest.TestCase):

    def setUp(self):

        header_device = HeaderDevice(
            name='HeaderDevice1',
            headstage_serial='Sample headstage_serial',
            headstage_smart_ref_on='Sample headstage_smart_ref_on',
            realtime_mode='Sample realtime_mode',
            headstage_auto_settle_on='Sample headstage_auto_settle_on',
            timestamp_at_creation='Sample timestamp_at_creation',
            controller_firmware_version='Sample controller_firmware_version',
            controller_serial='Sample controller_serial',
            save_displayed_chan_only='Sample save_displayed_chan_only',
            headstage_firmware_version='Sample headstage_firmware_version',
            qt_version='Sample qt_version',
            compile_date='Sample compile_date',
            compile_time='Sample compile_time',
            file_prefix='Sample file_prefix',
            headstage_gyro_sensor_on='Sample headstage_gyro_sensor_on',
            headstage_mag_sensor_on='Sample headstage_mag_sensor_on',
            trodes_version='Sample trodes_version',
            headstage_accel_sensor_on='Sample headstage_accel_sensor_on',
            commit_head='Sample commit_head',
            system_time_at_creation='Sample system_time_at_creation',
            file_path='Sample file_path',
        )

        start_time = datetime(2017, 4, 3, 11, tzinfo=tzlocal())
        create_date = datetime(2017, 4, 15, 12, tzinfo=tzlocal())
        nwbfile = NWBFile(
            session_description='demonstrate NWBFile basics',
            identifier='NWB123',
            session_start_time=start_time,
            file_create_date=create_date
        )

        nwb_file_handler = NWBHDF5IO('test.nwb', mode='w')
        shank = Shank(name='1')
        shank.add_shanks_electrode(ShanksElectrode(name='0'))
        probe = Probe(name='probe', units='asd', id=1, probe_type='ssd', probe_description='2', num_shanks=3,
                      contact_size=1.0,
                      contact_side_numbering=False)

        probe.add_shank(shank)
        nwbfile.add_device(probe)
        nwbfile.add_device(header_device)
        nwb_file_handler.write(nwbfile)
        nwb_file_handler.close()

    def test_read_nwb_without_errors(self):
        with pynwb.NWBHDF5IO('test.nwb', 'r') as nwb_file_handler:
            nwb_file = nwb_file_handler.read()

        self.assertTrue(os.path.exists('test.nwb'))
        self.assertIsNotNone(nwb_file)
        self.assertIsNotNone(nwb_file.devices['HeaderDevice1'])

    def tearDown(self):
        os.remove('test.nwb')
