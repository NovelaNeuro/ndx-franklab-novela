# -*- coding: utf-8 -*-

import os.path

from pynwb.spec import NWBDatasetSpec
from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc="""NovelaNeurotechnologies Namespaces""",
        name="""ndx-fl-novela""",
        version="""0.0.002""",
        author=list(map(str.strip, """NovelaDevops""".split(','))),
        contact=list(map(str.strip, """devops@novelaneuro.com""".split(',')))
    )

    # # as in which namespace they are found
    # this is similar to specifying the Python modules that need to be imported
    # to use your new data types
    ns_builder.include_type('ElectrodeGroup', namespace='core')
    ns_builder.include_type('Device', namespace='core')
    ns_builder.include_type('NWBDataInterface', namespace='core')

    # see https://pynwb.readthedocs.io/en/latest/extensions.html#extending-nwb
    # for more information

    n_trode = NWBGroupSpec(
        doc='A custom ntrode ElectrodesGroup interface',
        neurodata_type_def='NTrode',
        neurodata_type_inc='ElectrodeGroup',
        datasets=[
            NWBDatasetSpec(
                doc='map of ntrodes',
                name='map',
                dtype='int',
                dims=[2],
                shape=[32]),
            NWBDatasetSpec(
                doc='ids of bad channels',
                name='bad_channels',
                dtype='int',
                dims=[1],
                shape=[32])
        ],
        attributes=[
            NWBAttributeSpec(
                name='ntrode_id',
                doc='id of electrode group',
                dtype='int'
            ),
            NWBAttributeSpec(
                name='electrode_group_id',
                doc='id of electrode group',
                dtype='int'
            ),

        ],
    )
    shanks_electrode = NWBGroupSpec(
        neurodata_type_def='ShanksElectrode',
        neurodata_type_inc='NWBDataInterface',
        doc='electrode in the probe',
        attributes=[
            NWBAttributeSpec(
                name='rel_x',
                doc='the rel_x value of this electrode',
                dtype='int'
            ),
            NWBAttributeSpec(
                name='rel_y',
                doc='the rel_y value of this electrode',
                dtype='int'
            ),
            NWBAttributeSpec(
                name='rel_z',
                doc='the rel_z value of this electrode',
                dtype='int'
            ),
        ]
    )

    shank = NWBGroupSpec(
        neurodata_type_def='Shank',
        neurodata_type_inc='NWBDataInterface',
        doc='shank in the probe',
        groups=[
            NWBGroupSpec(
                neurodata_type_inc='ShanksElectrode',
                doc='electrode in the probe',
                quantity='*'
            )
        ],
    )

    probe = NWBGroupSpec(
        doc='A custom Probes interface',
        neurodata_type_def='Probe',
        neurodata_type_inc='Device',
        quantity='*',
        groups=[
            NWBGroupSpec(
                neurodata_type_inc='Shank',
                doc='shank in the probe',
                quantity='*'
            )
        ],
        attributes=[
            NWBAttributeSpec(
                name='id',
                doc='unique id of the probe',
                dtype='int'
            ),
            NWBAttributeSpec(
                name='probe_type',
                doc='type of the probe',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='units',
                doc='units in probe',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='probe_description',
                doc='description of the probe',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='num_shanks',
                doc='number of shanks in probe',
                dtype='int'
            ),
            NWBAttributeSpec(
                name='contact_side_numbering',
                doc='is contact_side_numbering enabled',
                dtype='bool'
            ),
            NWBAttributeSpec(
                name='contact_size',
                doc='value of contact size in float',
                dtype='float'
            ),
        ]
    )

    node = NWBGroupSpec(
        neurodata_type_def='Node',
        neurodata_type_inc='NWBDataInterface',
        doc='nodes in the graph',
        quantity='*',
        attributes=[
            NWBAttributeSpec(
                name='name',
                doc='the name of this node',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='value',
                doc='the value of this node',
                dtype='int'
            ),
            NWBAttributeSpec(
                name='help',
                doc='help doc',
                dtype='text',
                value='Apparatus Node'
            )
        ]
    )

    edge = NWBGroupSpec(
        neurodata_type_def='Edge',
        neurodata_type_inc='NWBDataInterface',
        doc='edges in the graph',
        quantity='*',
        datasets=[
            NWBDatasetSpec(
                doc='names of the nodes this edge connects',
                name='edge_nodes',
                dtype='text',
                dims=['first_node_name|second_node_name'],
                shape=[2]
            )
        ],
        attributes=[
            NWBAttributeSpec(
                name='help',
                doc='help doc',
                dtype='text',
                value='Apparatus Edge')
        ]
    )

    apparatus = NWBGroupSpec(
        neurodata_type_def='Apparatus',
        neurodata_type_inc='NWBDataInterface',
        doc='a graph of nodes and edges',
        quantity='*',
        groups=[node, edge],
        attributes=[
            NWBAttributeSpec(
                name='name',
                doc='the name of this apparatus',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='help',
                doc='help doc',
                dtype='text',
                value='Behavioral Apparatus')
        ]
    )

    associated_files = NWBGroupSpec(
        neurodata_type_def='AssociatedFiles',
        neurodata_type_inc='NWBDataInterface',
        doc='content of files linked with nwb',
        attributes=[
            NWBAttributeSpec(
                name='description',
                doc='description of file',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='content',
                doc='content of file',
                dtype='text'
            )
        ]
    )

    header_device = NWBGroupSpec(
        doc='metadata from global configuration from header',
        neurodata_type_def='HeaderDevice',
        neurodata_type_inc='Device',
        attributes=[
            NWBAttributeSpec(
                name='headstage_serial',
                doc='headstage_serial from global configuration',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='headstage_smart_ref_on',
                doc='headstage_smart_ref_on from global configuration',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='realtime_mode',
                doc='realtime_mode from global configuration',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='headstage_auto_settle_on',
                doc='headstage_auto_settle_on from global configuration',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='timestamp_at_creation',
                doc='timestamp_at_creation from global configuration',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='controller_firmware_version',
                doc='conntroller_firmware_version from global configuration',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='controller_serial',
                doc='controller_serial from global configuration',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='save_displayed_chan_only',
                doc='save_displayed_chan_only from global configuration',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='headstage_firmware_version',
                doc='headstage_firmware_version from global configuration',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='qt_version',
                doc='qt_version_version from global configuration',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='compile_date',
                doc='compile_date_version from global configuration',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='compile_time',
                doc='compile_time_version from global configuration',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='file_prefix',
                doc='file_prefix_version from global configuration',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='headstage_gyro_sensor_on',
                doc='headstage_gyro_sensor_on_version from global configuration',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='headstage_mag_sensor_on',
                doc='headstage_mag_sensor_on_version from global configuration',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='trodes_version',
                doc='trodes_versionversion from global configuration',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='headstage_accel_sensor_on',
                doc='headstage_accel_sensor_on from global configuration',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='commit_head',
                doc='commit_head from global configuration',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='system_time_at_creation',
                doc='system_time_at_creation from global configuration',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='file_path',
                doc='file_path from global configuration',
                dtype='text'
            ),
        ]
    )

    nwb_electrode_group = NWBGroupSpec(
        neurodata_type_def='NwbElectrodeGroup',
        neurodata_type_inc='ElectrodeGroup',
        doc='Custom nwb ElectrodeGroup',
        attributes=[
            NWBAttributeSpec(
                name='targeted_location',
                doc='predicted location',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='targeted_x',
                doc='predicted x coordinates',
                dtype='float'
            ),
            NWBAttributeSpec(
                name='targeted_y',
                doc='predicted y coordinates',
                dtype='float'
            ),
            NWBAttributeSpec(
                name='targeted_z',
                doc='predicted z coordinates',
                dtype='float'
            ),
            NWBAttributeSpec(
                name='units',
                doc='units of fields, possible value: um or mm',
                dtype='text'
            ),
        ]
    )

    new_data_types = [
        n_trode, shanks_electrode, shank, probe, apparatus, header_device, associated_files, nwb_electrode_group
    ]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()
