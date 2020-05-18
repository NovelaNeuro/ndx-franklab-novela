from hdmf.utils import docval, call_docval_func, get_docval
from pynwb import register_class, NWBContainer
from pynwb.core import NWBDataInterface, MultiContainerInterface
from pynwb.device import Device


@register_class('Electrode', 'ndx-fl-novela')
class Electrode(NWBContainer):
    ''' Representation of custom Electrode object in NWB '''

    @docval(
        {'name': 'name', 'type': str, 'doc': 'name of the shank'},
        {'name': 'rel_x', 'type': float, 'doc': 'the rel_x value of this electrode'},
        {'name': 'rel_y', 'type': float, 'doc': 'the rel_y value of this electrode'},
        {'name': 'rel_z', 'type': float, 'doc': 'the rel_z value of this electrode'},
    )
    def __init__(self, **kwargs):
        super(Electrode, self).__init__(name=kwargs['name'])
        self.rel_x = kwargs['rel_x']
        self.rel_y = kwargs['rel_y']
        self.rel_z = kwargs['rel_z']


@register_class('Shank', 'ndx-fl-novela')
class Shank(MultiContainerInterface):
    ''' Representation of Shank object in NWB '''

    @docval(
        {'name': 'name', 'type': str, 'doc': 'name of the shank'},
        {'name': 'electrode', 'type': (list, tuple), 'doc': 'electrodes in shank', 'default': list()}
    )
    def __init__(self, **kwargs):
        super(Shank, self).__init__(name=kwargs['name'])
        self.electrodes = kwargs['electrode']

    __clsconf__ = [
        {
            'attr': 'electrodes',
            'type': Electrode,
            'add': 'add_electrode',
            'get': 'get_electrode'
        }
    ]


@register_class('Probe', 'ndx-fl-novela')
class Probe(Device, MultiContainerInterface):
    ''' Representation of Probe object in NWB '''

    @docval(*get_docval(Device.__init__) + (
            {'name': 'id', 'type': 'int', 'doc': 'unique id of the probe'},
            {'name': 'probe_type', 'type': 'str', 'doc': 'type of probe'},
            {'name': 'units', 'type': 'str', 'doc': 'units in device'},
            {'name': 'probe_description', 'type': 'str', 'doc': 'description of the probe'},
            {'name': 'num_shanks', 'type': 'int', 'doc': 'number of shanks associated with probe'},
            {'name': 'contact_side_numbering', 'type': 'bool', 'doc': 'is contact_side_numbering enabled'},
            {'name': 'contact_size', 'type': 'float', 'doc': 'value of contact size as float'},
            {'name': 'shanks', 'type': (list, tuple), 'doc': 'shanks in probe', 'default': list()}
    ))
    def __init__(self, **kwargs):
        super().__init__(**{kwargs_item: kwargs[kwargs_item]
                            for kwargs_item in kwargs.copy()
                            if kwargs_item != 'id'
                            if kwargs_item != 'probe_type'
                            if kwargs_item != 'units'
                            if kwargs_item != 'probe_description'
                            if kwargs_item != 'num_shanks'
                            if kwargs_item != 'contact_side_numbering'
                            if kwargs_item != 'contact_size'
                            if kwargs_item != 'shanks'
                            })
        call_docval_func(super(Probe, self).__init__, kwargs)
        self.id = kwargs['id']
        self.probe_type = kwargs['probe_type']
        self.units = kwargs['units']
        self.probe_description = kwargs['probe_description']
        self.num_shanks = kwargs['num_shanks']
        self.contact_side_numbering = kwargs['contact_side_numbering']
        self.contact_size = kwargs['contact_size']
        self.shanks = kwargs['shanks']

    __nwbfields__ = ('id', 'probe_type', 'units', 'probe_description', 'num_shanks', 'contact_side_numbering',
                     'contact_size')

    __clsconf__ = [
        {
            'attr': 'shanks',
            'type': Shank,
            'add': 'add_shank',
            'get': 'get_shank'
        }
    ]
