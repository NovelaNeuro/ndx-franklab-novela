from hdmf.utils import docval, call_docval_func, get_docval
from pynwb import register_class
from pynwb.device import Device


@register_class('CameraDevice', 'ndx-franklab-novela')
class CameraDevice(Device):
    """Represented as CameraDevice in NWB"""

    __nwbfields__ = ('meters_per_pixel',)

    @docval(*get_docval(Device.__init__) + (
            {'name': 'meters_per_pixel', 'type': float, 'doc': 'meters per pixel'},
            ))
    def __init__(self, **kwargs):
        super().__init__(**{kwargs_item: kwargs[kwargs_item]
                            for kwargs_item in kwargs.copy()
                            if kwargs_item != 'meters_per_pixel'
                            })
        call_docval_func(super(CameraDevice, self).__init__, kwargs)
        self.meters_per_pixel = kwargs['meters_per_pixel']

