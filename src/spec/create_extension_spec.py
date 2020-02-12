# -*- coding: utf-8 -*-

import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec
from pynwb.spec import NWBDatasetSpec, NWBLinkSpec, NWBDtypeSpec, NWBRefSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc="""NovelaNeurotechnologies Namespaces""",
        name="""ndx-novela-namespace""",
        version="""0.1.0""",
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
    fl_electrode_group = NWBGroupSpec(
        doc='A custom ElectrodesGroup interface',
        neurodata_type_def='FLElectrodeGroup',
        neurodata_type_inc='ElectrodeGroup',
        attributes=[
            NWBAttributeSpec(
                name='id',
                doc='id of electrode group',
                dtype='int'
            ),
        ],
    )

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
                shape=[32])],
        attributes=[
            NWBAttributeSpec(
                name='ntrode_id',
                doc='id of electrode group',
                dtype='int'
            ),
            NWBAttributeSpec(
                name='probe_id',
                doc='id of probe',
                dtype='int'
            ),

        ],
    )

    probe = NWBGroupSpec(
        doc='A custom Probes interface',
        neurodata_type_def='Probe',
        neurodata_type_inc='Device',
        attributes=[
            NWBAttributeSpec(
                name='id',
                doc='unique id of the probe',
                dtype='int'
            ),
            NWBAttributeSpec(
                name='contact_size',
                doc='value of contact size in float',
                dtype='float'
            ),
            NWBAttributeSpec(
                name='probe_type',
                doc='type of the probe',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='num_shanks',
                doc='number of shanks in probe',
                dtype='int'
            ),
        ]
    )

    node = NWBGroupSpec(
        neurodata_type_def='Node',
        neurodata_type_inc='NWBDataInterface',
        doc='nodes in the graph',
        quantity='*',
        attributes=[NWBAttributeSpec(name='name',
                                     doc='the name of this node',
                                     dtype='text'),
                    NWBAttributeSpec(name='value',
                                     doc='the value of this node',
                                     dtype='int'),
                    NWBAttributeSpec(name='help',
                                     doc='help doc',
                                     dtype='text',
                                     value='Apparatus Node')])

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
                shape=[2])],
        attributes=[
            NWBAttributeSpec(
                name='help',
                doc='help doc',
                dtype='text',
                value='Apparatus Edge')])

    apparatus = NWBGroupSpec(
        neurodata_type_def='Apparatus',
        neurodata_type_inc='NWBDataInterface',
        doc='a graph of nodes and edges',
        quantity='*',
        groups=[node, edge],
        attributes=[
            NWBAttributeSpec(name='name',
                             doc='the name of this apparatus',
                             dtype='text'),
            NWBAttributeSpec(name='help',
                             doc='help doc',
                             dtype='text',
                             value='Behavioral Apparatus')])

    # ToDo check if edge, node is added properly
    new_data_types = [fl_electrode_group, n_trode, probe, apparatus]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()
