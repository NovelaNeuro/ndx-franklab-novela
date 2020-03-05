from unittest import TestCase

from src.pynwb.ndx_fllab_novela.header_device import HeaderDevice


class TestHeaderDevice(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.header_device = HeaderDevice(
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

    def test_successfulNodeCreation_true(self):
        self.assertIsInstance(self.header_device, HeaderDevice)

    def test_checkNodeCorrectValue_true(self):
        self.assertEqual(self.header_device.name, 'HeaderDevice1')
        self.assertEqual(self.header_device.headstage_serial, 'Sample headstage_serial')
        self.assertEqual(self.header_device.headstage_smart_ref_on, 'Sample headstage_smart_ref_on')
        self.assertEqual(self.header_device.realtime_mode, 'Sample realtime_mode')
        self.assertEqual(self.header_device.headstage_auto_settle_on, 'Sample headstage_auto_settle_on')
        self.assertEqual(self.header_device.timestamp_at_creation, 'Sample timestamp_at_creation')
        self.assertEqual(self.header_device.controller_firmware_version, 'Sample controller_firmware_version')
        self.assertEqual(self.header_device.controller_serial, 'Sample controller_serial')
        self.assertEqual(self.header_device.save_displayed_chan_only, 'Sample save_displayed_chan_only')
        self.assertEqual(self.header_device.headstage_firmware_version, 'Sample headstage_firmware_version')
        self.assertEqual(self.header_device.qt_version, 'Sample qt_version')
        self.assertEqual(self.header_device.compile_date, 'Sample compile_date')
        self.assertEqual(self.header_device.compile_time, 'Sample compile_time')
        self.assertEqual(self.header_device.file_prefix, 'Sample file_prefix')
        self.assertEqual(self.header_device.headstage_gyro_sensor_on, 'Sample headstage_gyro_sensor_on')
        self.assertEqual(self.header_device.headstage_mag_sensor_on, 'Sample headstage_mag_sensor_on')
        self.assertEqual(self.header_device.trodes_version, 'Sample trodes_version')
        self.assertEqual(self.header_device.headstage_accel_sensor_on, 'Sample headstage_accel_sensor_on')
        self.assertEqual(self.header_device.commit_head, 'Sample commit_head')
        self.assertEqual(self.header_device.system_time_at_creation, 'Sample system_time_at_creation')
        self.assertEqual(self.header_device.file_path, 'Sample file_path')

    def test_checkNodeCorrectType_true(self):
        self.assertEqual(self.header_device.name, 'HeaderDevice1')
        self.assertIsInstance(self.header_device.headstage_serial, str)
        self.assertIsInstance(self.header_device.headstage_smart_ref_on, str)
        self.assertIsInstance(self.header_device.realtime_mode, str)
        self.assertIsInstance(self.header_device.headstage_auto_settle_on, str)
        self.assertIsInstance(self.header_device.timestamp_at_creation, str)
        self.assertIsInstance(self.header_device.controller_firmware_version, str)
        self.assertIsInstance(self.header_device.controller_serial, str)
        self.assertIsInstance(self.header_device.save_displayed_chan_only, str)
        self.assertIsInstance(self.header_device.headstage_firmware_version, str)
        self.assertIsInstance(self.header_device.qt_version, str)
        self.assertIsInstance(self.header_device.compile_date, str)
        self.assertIsInstance(self.header_device.compile_time, str)
        self.assertIsInstance(self.header_device.file_prefix, str)
        self.assertIsInstance(self.header_device.headstage_gyro_sensor_on, str)
        self.assertIsInstance(self.header_device.headstage_mag_sensor_on, str)
        self.assertIsInstance(self.header_device.trodes_version, str)
        self.assertIsInstance(self.header_device.headstage_accel_sensor_on, str)
        self.assertIsInstance(self.header_device.commit_head, str)
        self.assertIsInstance(self.header_device.system_time_at_creation, str)
        self.assertIsInstance(self.header_device.file_path, str)
