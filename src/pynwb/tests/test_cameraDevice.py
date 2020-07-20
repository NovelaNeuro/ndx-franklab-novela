from unittest import TestCase

from src.pynwb.ndx_franklab_novela.camera_device import CameraDevice


class TestCameraDevice(TestCase):

    def test_cameraDevice_created_successfully(self):

        cam_1 = CameraDevice(
            name='1',
            meters_per_pixel=0.20,
            camera_name='test name',
            model='ndx2000',
            lens='500dpt',
            manufacturer='sony'
        )

        self.assertEqual(cam_1.name, '1')
        self.assertEqual(cam_1.camera_name, 'test name')
        self.assertEqual(cam_1.model, 'ndx2000')
        self.assertEqual(cam_1.lens, '500dpt')
        self.assertEqual(cam_1.manufacturer, 'sony')
