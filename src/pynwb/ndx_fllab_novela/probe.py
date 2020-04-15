from hdmf.utils import docval, call_docval_func, get_docval
from pynwb import register_class
from pynwb.device import Device


@register_class('Probe', 'ndx-fllab-novela')
class Probe(Device):
    ''' Representation of Probe object in NWB '''

    @docval(*get_docval(Device.__init__) + (
            {'name': 'id', 'type': 'int', 'doc': 'unique id of the probe'},
            {'name': 'probe_type', 'type': 'str', 'doc': 'type of probe'},
            {'name': 'units', 'type': 'str', 'doc': 'units in device'},
            {'name': 'num_shanks', 'type': 'int', 'doc': 'number of shanks associated with probe'},
            {'name': 'contact_side_numbering', 'type': 'bool', 'doc': 'is contact_side_numbering enabled'},
            {'name': 'contact_size', 'type': 'float', 'doc': 'value of contact size as float'},
            ))
    def __init__(self, **kwargs):
        super().__init__(**{kwargs_item: kwargs[kwargs_item]
                            for kwargs_item in kwargs.copy()
                            if kwargs_item != 'id'
                            if kwargs_item != 'probe_type'
                            if kwargs_item != 'units'
                            if kwargs_item != 'num_shanks'
                            if kwargs_item != 'contact_side_numbering'
                            if kwargs_item != 'contact_size'
                            })
        call_docval_func(super(Probe, self).__init__, kwargs)
        self.id = kwargs['id']
        self.probe_type = kwargs['probe_type']
        self.units = kwargs['units']
        self.num_shanks = kwargs['num_shanks']
        self.contact_side_numbering = kwargs['contact_side_numbering']
        self.contact_size = kwargs['contact_size']

    __nwbfields__ = ('id', 'probe_type', 'units', 'num_shanks', 'contact_side_numbering', 'contact_size')
