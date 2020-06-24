import unittest

from src.pynwb.ndx_franklab_novela.data_acq_device import DataAcqDevice


class TestDataAcqDevice(unittest.TestCase):

    def test_data_acq_device_successfully_created_with_optional_data(self):

        data_acq_device = DataAcqDevice(
            name='DataAcqDevice1',
            system='System1',
            amplifier='Amplifier1',
            adc_circuit='adc_circuit1',
        )

        self.assertIsInstance(data_acq_device, DataAcqDevice)

        self.assertIsInstance(data_acq_device.name, str)
        self.assertIsInstance(data_acq_device.system, str)
        self.assertIsInstance(data_acq_device.amplifier, str)
        self.assertIsInstance(data_acq_device.adc_circuit, str)

        self.assertEqual(data_acq_device.name, 'DataAcqDevice1')
        self.assertEqual(data_acq_device.system, 'System1')
        self.assertEqual(data_acq_device.amplifier, 'Amplifier1')
        self.assertEqual(data_acq_device.adc_circuit, 'adc_circuit1')

    def test_data_acq_device_successfully_created_without_optional_data(self):

        data_acq_device = DataAcqDevice(
            name='DataAcqDevice1',
            system='System1'
        )

        self.assertIsInstance(data_acq_device, DataAcqDevice)
        
        self.assertIsInstance(data_acq_device.name, str)
        self.assertIsInstance(data_acq_device.system, str)
        self.assertIsInstance(data_acq_device.amplifier, str)
        self.assertIsInstance(data_acq_device.adc_circuit, str)

        self.assertEqual(data_acq_device.name, 'DataAcqDevice1')
        self.assertEqual(data_acq_device.system, 'System1')
        self.assertEqual(data_acq_device.amplifier, '')
        self.assertEqual(data_acq_device.adc_circuit, '')

