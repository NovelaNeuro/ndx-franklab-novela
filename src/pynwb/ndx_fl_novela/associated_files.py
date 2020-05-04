from hdmf.utils import docval, call_docval_func, get_docval
from pynwb import register_class
from pynwb.core import NWBDataInterface
from pynwb.device import Device


@register_class('AssociatedFiles', 'ndx-fl-novela')
class AssociatedFiles(NWBDataInterface):
    """ Representation of associated files in NWB """
    __nwbfields__ = ('file_name', 'description', 'content')

    @docval(*get_docval(NWBDataInterface.__init__) + (
            {'name': 'file_name', 'type': 'str', 'doc': 'file_name'},
            {'name': 'description', 'type': 'str', 'doc': 'description of associated file'},
            {'name': 'content', 'type': 'str', 'doc': 'content of associated file'},
            ))
    def __init__(self, **kwargs):
        super().__init__(**{kwargs_item: kwargs[kwargs_item]
                            for kwargs_item in kwargs.copy()
                            if kwargs_item not in ['file_name', 'description', 'content']
                            })
        call_docval_func(super(AssociatedFiles, self).__init__, kwargs)
        self.file_name = kwargs['file_name']
        self.description = kwargs['description']
        self.content = kwargs['content']

