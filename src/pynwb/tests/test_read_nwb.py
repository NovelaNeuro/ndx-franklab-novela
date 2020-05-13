import unittest
import os
from unittest.mock import Mock

import pynwb
from pynwb import NWBHDF5IO, ProcessingModule

from datetime import datetime
from dateutil.tz import tzlocal
from pynwb import NWBFile
from pynwb.device import Device

from src.pynwb.ndx_fl_novela.apparatus import Apparatus, Edge, Node
from src.pynwb.ndx_fl_novela.header_device import HeaderDevice
from src.pynwb.ndx_fl_novela.ntrode import NTrode
from src.pynwb.ndx_fl_novela.nwb_electrode_group import NwbElectrodeGroup
from src.pynwb.ndx_fl_novela.probe import Probe, Shank, ShanksElectrode


class TestNWBFileReading(unittest.TestCase):

    def setUp(self):
        start_time = datetime(2017, 4, 3, 11, tzinfo=tzlocal())
        create_date = datetime(2017, 4, 15, 12, tzinfo=tzlocal())
        self.nwb_file_content = NWBFile(
            session_description='demonstrate NWBFile basics',
            identifier='nwb_file',
            session_start_time=start_time,
            file_create_date=create_date
        )

    def test_read_nwb_apparatus_successfully(self):
        node_0 = Node(
            name='node_0',
            value=0
        )
        node_1 = Node(
            name='node_1',
            value=1
        )
        node_2 = Node(
            name='node_2',
            value=2
        )
        node_3 = Node(
            name='node_3',
            value=3
        )
        edge_0 = Edge(
            name='edge_0',
            edge_nodes=[node_0, node_1]
        )
        edge_1 = Edge(
            name='edge_1',
            edge_nodes=[node_2, node_3]
        )
        apparatus = Apparatus(
            name='apparatus',
            edges=[edge_0, edge_1],
            nodes=[node_0, node_1, node_2, node_3]
        )

        processing_module = ProcessingModule('processing_module', 'sample description')
        processing_module.add(apparatus)
        self.nwb_file_content.add_processing_module(processing_module)
        nwb_file_handler = NWBHDF5IO('apparatus.nwb', mode='w')
        nwb_file_handler.write(self.nwb_file_content)
        nwb_file_handler.close()

        self.assertTrue(os.path.exists('apparatus.nwb'))
        with pynwb.NWBHDF5IO('apparatus.nwb', 'r') as nwb_file_handler:
            nwb_file = nwb_file_handler.read()
            self.assertEqual(nwb_file.processing['processing_module'].data_interfaces['apparatus'].name, apparatus.name)

        self.delete_nwb('apparatus')

    def test_read_nwb_ntrode_successfully(self):
        device = Device('device_0')
        self.nwb_file_content.add_device(device)
        ntrode = NTrode(
            name='ntrode_0',
            description='Sample description',
            location='Sample location',
            device=device,
            ntrode_id=1,
            electrode_group_id=1,
            bad_channels=[1, 3],
            map=[[1, 2], [3, 4], [5, 6]]
        )

        self.nwb_file_content.add_electrode_group(ntrode)
        nwb_file_handler = NWBHDF5IO('ntrode.nwb', mode='w')
        nwb_file_handler.write(self.nwb_file_content)
        nwb_file_handler.close()

        self.assertTrue(os.path.exists('ntrode.nwb'))
        with pynwb.NWBHDF5IO('ntrode.nwb', 'r') as nwb_file_handler:
            nwb_file = nwb_file_handler.read()
            self.assertEqual(nwb_file.electrode_groups['ntrode_0'].electrode_group_id, ntrode.electrode_group_id)

        self.delete_nwb('ntrode')

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
            name='shanks_electrode',
            rel_x=1,
            rel_y=2,
            rel_z=3
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
            contact_side_numbering=False,
            # shanks=[shank],
        )
        probe.add_shanks(shank)
        print('Before write')
        print(probe)
        print('Before write: shanks inside probe')
        print(probe.shanks)
        self.nwb_file_content.add_device(probe)

        nwb_file_handler = NWBHDF5IO('probe.nwb', mode='w')
        nwb_file_handler.write(self.nwb_file_content)
        nwb_file_handler.close()

        self.assertTrue(os.path.exists('probe.nwb'))
        with pynwb.NWBHDF5IO('probe.nwb', 'r',  load_namespaces=True) as nwb_file_handler:
            nwb_file = nwb_file_handler.read()
            print('Read')
            print(nwb_file.devices['probe'])
            self.assertEqual(nwb_file.devices['probe'].name, probe.name)
            self.assertEqual(nwb_file.devices['probe'].shanks, probe.shanks)

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
    def delete_nwb(file_name):
        os.remove(file_name + '.nwb')
