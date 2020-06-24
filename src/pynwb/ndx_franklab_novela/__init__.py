import os

from pynwb import load_namespaces

# Set path of the namespace.yaml file to the expected install location
from src.pynwb.ndx_franklab_novela.associated_files import AssociatedFiles
from src.pynwb.ndx_franklab_novela.camera_device import CameraDevice
from src.pynwb.ndx_franklab_novela.data_acq_device import DataAcqDevice
from src.pynwb.ndx_franklab_novela.header_device import HeaderDevice
from src.pynwb.ndx_franklab_novela.nwb_electrode_group import NwbElectrodeGroup
from src.pynwb.ndx_franklab_novela.nwb_image_series import NwbImageSeries
from src.pynwb.ndx_franklab_novela.probe import Probe

ndx_franklab_novela_specpath = os.path.join(
    os.path.dirname(__file__),
    'spec',
    'ndx-franklab-novela.namespace.yaml'
)

# If the extension has not been installed yet but we are running directly from
# the git repo
if not os.path.exists(ndx_franklab_novela_specpath):
    ndx_franklab_novela_specpath = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..', '..', '..',
        'spec',
        'ndx-franklab-novela.namespace.yaml'
    ))

# Load the namespace
load_namespaces(ndx_franklab_novela_specpath)


