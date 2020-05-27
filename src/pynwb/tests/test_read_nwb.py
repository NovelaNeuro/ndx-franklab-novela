import os

import pynwb
from pynwb import NWBHDF5IO

from datetime import datetime
from dateutil.tz import tzlocal
from pynwb import NWBFile
from pynwb.device import Device
from pynwb.testing import TestCase

from src.pynwb.ndx_franklab_novela.header_device import HeaderDevice
from src.pynwb.ndx_franklab_novela.nwb_electrode_group import NwbElectrodeGroup
from src.pynwb.ndx_franklab_novela.probe import Probe, Shank, ShanksElectrode


class TestNWBFileReading(TestCase):

    def setUp(self):
        start_time = datetime(2017, 4, 3, 11, tzinfo=tzlocal())
        create_date = datetime(2017, 4, 15, 12, tzinfo=tzlocal())
        self.nwb_file_content = NWBFile(
            session_description='demonstrate NWBFile basics',
            identifier='nwb_file',
            session_start_time=start_time,
            file_create_date=create_date
        )

    def test_read_nwb_header_device_successfully(self):
        header_device = HeaderDevice(
            name='header_device',
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

        self.nwb_file_content.add_device(header_device)
        nwb_file_handler = NWBHDF5IO('header_device.nwb', mode='w')
        nwb_file_handler.write(self.nwb_file_content)
        nwb_file_handler.close()

        self.assertTrue(os.path.exists('header_device.nwb'))
        with pynwb.NWBHDF5IO('header_device.nwb', 'r') as nwb_file_handler:
            nwb_file = nwb_file_handler.read()
            self.assertEqual(nwb_file.devices['header_device'].commit_head, header_device.commit_head)

        self.delete_nwb('header_device')

    def test_read_nwb_probe_successfully(self):
        shanks_electrode = ShanksElectrode(
            name='electrode_shank',
            rel_x=1.0,
            rel_y=2.0,
            rel_z=3.0
        )
        shank = Shank(name='shank')
        shank.add_shanks_electrode(shanks_electrode)
        probe = Probe(
            name='probe',
            units='mm',
            id=1,
            probe_type='type_1',
            probe_description='2',
            num_shanks=3,
            contact_size=1.0,
            contact_side_numbering=False
        )
        probe.add_shank(shank)
        self.nwb_file_content.add_device(probe)

        nwb_file_handler = NWBHDF5IO('probe.nwb', mode='w')
        nwb_file_handler.write(self.nwb_file_content)
        nwb_file_handler.close()

        self.assertTrue(os.path.exists('probe.nwb'))
        with pynwb.NWBHDF5IO('probe.nwb', 'r',  load_namespaces=True) as nwb_file_handler:
            nwb_file = nwb_file_handler.read()
            self.assertContainerEqual(nwb_file.devices['probe'], probe)

        self.delete_nwb('probe')

    def test_read_nwb_nwb_electrode_group_successfully(self):
        device = Device('device_0')
        self.nwb_file_content.add_device(device)
        nwb_electrode_group = NwbElectrodeGroup(
            name='nwb_electrode_group_0',
            description='Sample description',
            location='Sample location',
            device=device,
            targeted_location='predicted location',
            targeted_x=1.0,
            targeted_y=2.0,
            targeted_z=3.0,
            units='um'
        )

        self.nwb_file_content.add_electrode_group(nwb_electrode_group)
        nwb_file_handler = NWBHDF5IO('nwb_electrode_group.nwb', mode='w')
        nwb_file_handler.write(self.nwb_file_content)
        nwb_file_handler.close()

        self.assertTrue(os.path.exists('nwb_electrode_group.nwb'))
        with pynwb.NWBHDF5IO('nwb_electrode_group.nwb', 'r') as nwb_file_handler:
            nwb_file = nwb_file_handler.read()
            self.assertEqual(nwb_file.electrode_groups['nwb_electrode_group_0'].name, nwb_electrode_group.name)
            self.assertEqual(nwb_file.electrode_groups['nwb_electrode_group_0'].targeted_location,
                             nwb_electrode_group.targeted_location)

        self.delete_nwb('nwb_electrode_group')

    @staticmethod
    def delete_nwb(filename):
        os.remove(filename + '.nwb')
