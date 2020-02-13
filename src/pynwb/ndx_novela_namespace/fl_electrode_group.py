import os

from hdmf import docval
from hdmf.utils import get_docval, call_docval_func
from pynwb import load_namespaces, register_class
from pynwb.ecephys import ElectrodeGroup




@register_class('FLElectrodeGroup', 'ndx-novela-namespace')
class FLElectrodeGroup(ElectrodeGroup):
    __nwbfields__ = ('id', )

    @docval(*get_docval(ElectrodeGroup.__init__) + (
            {'name': 'id', 'type': 'int', 'doc': 'id or electrode group'},
            ))
    def __init__(self, **kwargs):
        super().__init__(**{kwargs_item: kwargs[kwargs_item]
                            for kwargs_item in kwargs.copy()
                            if kwargs_item != 'id'
                            })
        call_docval_func(super(FLElectrodeGroup, self).__init__, kwargs)
        self.id = kwargs['id']
