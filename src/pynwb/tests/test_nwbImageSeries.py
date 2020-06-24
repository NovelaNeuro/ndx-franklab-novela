from unittest import TestCase
from unittest.mock import Mock

from pynwb.device import Device

from src.pynwb.ndx_franklab_novela.nwb_image_series import NwbImageSeries


class TestNwbImageSeries(TestCase):

    def test_nwb_image_series_created_successfully(self):
        mock_device_1 = Mock(spec=Device)
        mock_device_2 = Mock(spec=Device)
        mock_timestamps = [1, 2, 3]
        mock_external_file = []

        nwb_image_series = NwbImageSeries(
            name='NwbImageSeries1',
            timestamps=mock_timestamps,
            external_file=mock_external_file,
            devices=[mock_device_1, mock_device_2]
        )

        self.assertEqual(nwb_image_series.name, 'NwbImageSeries1')
        self.assertEqual(nwb_image_series.timestamps, mock_timestamps)
        self.assertEqual(nwb_image_series.external_file, mock_external_file)
        self.assertEqual(nwb_image_series.devices, {
            mock_device_1.name: mock_device_1,
            mock_device_2.name: mock_device_2
        })
