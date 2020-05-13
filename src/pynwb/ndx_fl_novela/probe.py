from hdmf.utils import docval, call_docval_func, get_docval
from pynwb import register_class, NWBContainer
from pynwb.core import NWBDataInterface, MultiContainerInterface
from pynwb.device import Device


@register_class('ShanksElectrode', 'ndx-fl-novela')
class ShanksElectrode(NWBContainer):
    ''' Representation of ShanksElectrode object in NWB '''

    __nwbfields__ = ('name', 'rel_x', 'rel_y', 'rel_z')

    @docval(*get_docval(NWBContainer.__init__) + (
            {'name': 'rel_x', 'type': int, 'doc': 'the rel_x value of this electrode'},
            {'name': 'rel_y', 'type': int, 'doc': 'the rel_y value of this electrode'},
            {'name': 'rel_z', 'type': int, 'doc': 'the rel_z value of this electrode'},
    ))
    def __init__(self, **kwargs):
        super().__init__(**{kwargs_item: kwargs[kwargs_item]
                            for kwargs_item in kwargs.copy()
                            if kwargs_item != 'rel_x'
                            if kwargs_item != 'rel_y'
                            if kwargs_item != 'rel_z'
                            })
        call_docval_func(super(ShanksElectrode, self).__init__, kwargs)

        self.rel_x = kwargs['rel_x']
        self.rel_y = kwargs['rel_y']
        self.rel_z = kwargs['rel_z']


@register_class('Shank', 'ndx-fl-novela')
class Shank(MultiContainerInterface):
    ''' Representation of Shank object in NWB '''

    @docval(*get_docval(MultiContainerInterface.__init__) + (
            {'name': 'shanks_electrodes', 'type': list, 'doc': 'id of the shank', 'default': list()},
    ))
    def __init__(self, **kwargs):
        super().__init__(**{kwargs_item: kwargs[kwargs_item]
                            for kwargs_item in kwargs.copy()
                            if kwargs_item != 'shanks_electrodes'
                            })
        call_docval_func(super(Shank, self).__init__, kwargs)

        self.shanks_electrodes = []

    __clsconf__ = [
        {
            'attr': 'shanks_electrodes',
            'type': ShanksElectrode,
            'add': 'add_shanks_electrode',
            'get': 'get_shanks_electrode'
        }
    ]


@register_class('Probe', 'ndx-fl-novela')
class Probe(Device, MultiContainerInterface):
    ''' Representation of Probe object in NWB '''

    @docval(
        *get_docval(Device.__init__, 'description', 'manufacturer'),
        *get_docval(MultiContainerInterface.__init__),
        {'name': 'id', 'type': int, 'doc': 'unique id of the probe'},
        {'name': 'probe_type', 'type': 'str', 'doc': 'type of probe'},
        {'name': 'units', 'type': 'str', 'doc': 'units in device'},
        {'name': 'probe_description', 'type': 'str', 'doc': 'description of the probe'},
        {'name': 'num_shanks', 'type': 'int', 'doc': 'number of shanks associated with probe'},
        {'name': 'contact_side_numbering', 'type': 'bool', 'doc': 'is contact_side_numbering enabled'},
        {'name': 'contact_size', 'type': 'float', 'doc': 'value of contact size as float'},
        {'name': 'shanks', 'type': list, 'doc': 'shank in the probe', 'default': list()},

    )
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

    __nwbfields__ = ('id', 'probe_type', 'units', 'probe_description', 'num_shanks', 'contact_side_numbering',
                     'contact_size', 'shanks')

    __clsconf__ = [
        {
            'attr': 'shanks',
            'type': Shank,
            'add': 'add_shanks',
            'get': 'get_shanks'
        }
    ]
