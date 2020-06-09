from unittest import TestCase

from src.pynwb.ndx_franklab_novela.camera_device import CameraDevice


class TestCameraDevice(TestCase):

    def test_cameraDevice_created_successfully(self):

        cam_1 = CameraDevice(
            name='1',
            meter_per_pixel=0.20
        )

        self.assertEqual(cam_1.name, '1')
        self.assertEqual(cam_1.meter_per_pixel, 0.20)
