import os
from datetime import datetime

import pynwb
from dateutil.tz import tzlocal
from pynwb import NWBFile
from pynwb import NWBHDF5IO, ProcessingModule
from pynwb.behavior import BehavioralEvents
from pynwb.device import Device
from pynwb.testing import TestCase

from src.pynwb.ndx_franklab_novela import CameraDevice, AssociatedFiles
from src.pynwb.ndx_franklab_novela import DataAcqDevice
from src.pynwb.ndx_franklab_novela import HeaderDevice
from src.pynwb.ndx_franklab_novela import NwbElectrodeGroup
from src.pynwb.ndx_franklab_novela import NwbImageSeries
from src.pynwb.ndx_franklab_novela import Probe, Shank, ShanksElectrode


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

    def test_read_nwb_data_acq_device_successfully(self):
        data_acq_device = DataAcqDevice(
            name='DataAcqDevice1',
            system='System1',
            amplifier='Amplifier1',
            adc_circuit='adc_circuit1'
        )
        self.nwb_file_content.add_device(data_acq_device)

        nwb_file_handler = NWBHDF5IO('data_acq_device.nwb', mode='w')
        nwb_file_handler.write(self.nwb_file_content)
        nwb_file_handler.close()

        self.assertTrue(os.path.exists('data_acq_device.nwb'))
        with pynwb.NWBHDF5IO('data_acq_device.nwb', 'r',  load_namespaces=True) as nwb_file_handler:
            nwb_file = nwb_file_handler.read()
            self.assertContainerEqual(nwb_file.devices['DataAcqDevice1'], data_acq_device)

        self.delete_nwb('data_acq_device')

    def test_read_nwb_camera_device_successfully(self):
        camera_device = CameraDevice(
            name='CameraDevice1',
            meters_per_pixel=0.20,
            camera_name='test name',
            model='ndx2000',
            lens='500dpt',
            manufacturer='sony'
        )
        self.nwb_file_content.add_device(camera_device)

        nwb_file_handler = NWBHDF5IO('camera_device.nwb', mode='w')
        nwb_file_handler.write(self.nwb_file_content)
        nwb_file_handler.close()

        self.assertTrue(os.path.exists('camera_device.nwb'))
        with pynwb.NWBHDF5IO('camera_device.nwb', 'r',  load_namespaces=True) as nwb_file_handler:
            nwb_file = nwb_file_handler.read()
            self.assertContainerEqual(nwb_file.devices['CameraDevice1'], camera_device)

        self.delete_nwb('camera_device')

    def test_read_nwb_nwb_image_series_successfully(self):
        device_1 = Device('device1')
        device_2 = Device('device2')
        mock_timestamps = [1, 2, 3]
        mock_external_file = ['some file']

        nwb_image_series = NwbImageSeries(
            name='NwbImageSeries1',
            timestamps=mock_timestamps,
            external_file=mock_external_file,
            devices=[device_1, device_2]
        )

        behavioral_time_series = BehavioralEvents(name="BehavioralTimeSeries")
        behavioral_time_series.add_timeseries(nwb_image_series)
        processing_module = ProcessingModule(name='ProcessingModule', description='')
        processing_module.add_data_interface(behavioral_time_series)
        self.nwb_file_content.add_processing_module(processing_module)

        self.nwb_file_content.add_stimulus_template(nwb_image_series)

        nwb_file_handler = NWBHDF5IO('nwb_image_series.nwb', mode='w')
        nwb_file_handler.write(self.nwb_file_content)
        nwb_file_handler.close()

        self.assertTrue(os.path.exists('nwb_image_series.nwb'))
        with pynwb.NWBHDF5IO('nwb_image_series.nwb', 'r', load_namespaces=True) as nwb_file_handler:
            nwb_file = nwb_file_handler.read()
            self.assertContainerEqual(nwb_file.stimulus_template['NwbImageSeries1'], nwb_image_series)
            self.assertContainerEqual(
                nwb_file.processing['ProcessingModule'].data_interfaces['BehavioralTimeSeries'].
                    time_series['NwbImageSeries1'],
                nwb_image_series
            )

        self.delete_nwb('nwb_image_series')

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

    def test_read_nwb_associated_files_successfully(self):
        associated_files = AssociatedFiles(
                name='file1',
                description='description of file1',
                content='1 2 3 content of file test',
                task_epochs='1, 2'
        )
        self.nwb_file_content.add_processing_module(ProcessingModule('associated_files', 'description_of_associaed_files'))
        self.nwb_file_content.processing['associated_files'].add(associated_files)

        nwb_file_handler = NWBHDF5IO('associated_files.nwb', mode='w')
        nwb_file_handler.write(self.nwb_file_content)
        nwb_file_handler.close()

        self.assertTrue(os.path.exists('associated_files.nwb'))
        with pynwb.NWBHDF5IO('associated_files.nwb', 'r') as nwb_file_handler:
            nwb_file = nwb_file_handler.read()

            self.assertIsInstance(nwb_file.processing['associated_files']['file1'], AssociatedFiles)
            self.assertEqual('file1', nwb_file.processing['associated_files']['file1'].name)
            self.assertEqual('description of file1', nwb_file.processing['associated_files']['file1'].fields['description'])
            self.assertEqual('1 2 3 content of file test', nwb_file.processing['associated_files']['file1'].fields['content'])
            self.assertEqual('1, 2', nwb_file.processing['associated_files']['file1'].fields['task_epochs'])

        self.delete_nwb('associated_files')

    @staticmethod
    def delete_nwb(filename):
        os.remove(filename + '.nwb')
