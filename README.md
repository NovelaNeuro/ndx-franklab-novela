# ndx-fllab-novela Extension for NWB

# About
ndx-fllab-novela is a python package containing NWB custom extensions.

# Extensions

### Edge
An undirected edge connecting two nodes in a graph. <br>
**Attributes:** <br>
**name**  `string`: name of this segement node <br>
**edge_nodes**  `array_data`, `data`: the names of the two nodes in this undirected edge' <br>

#### Node
A generic graph node. Subclass for more specific types of nodes. <br>
**Attributes:** <br>
    **name**  `string`: name of this node <br>
    **value**  `int`: value of this node' <br>

#### Apparatus
Topological graph representing connected components of a behavioral apparatus. <br>
**Attributes:** <br>
    **name**  `string`: name of apparatus <br>
    **nodes**  `list`: Node objects contained in this apparatus <br>
    **edges**  `list`: Edge objects contained in this apparatus <br>


#### HeaderDevice
Representation of HeaderDevice in NWB. <br>
**Attributes:** <br>
    **headstage_serial**  `string`: headstage_serial from header global configuration <br>
    **headstage_smart_ref_on**  `string`: headstage_smart_ref_on from header global configuration <br>
    **realtime_mode**  `string`: realtime_mode from header global configuration <br>
    **headstage_auto_settle_on**  `string`: headstage_auto_settle_on from header global configuration <br>
    **timestamp_at_creation**  `string`: timestamp_at_creation from header global configuration <br>
    **controller_firmware_version**  `string`: conntroller_firmware_version from header global configuration <br>
    **controller_serial**  `string`: conntroller_serial from header global configuration <br>
    **save_displayed_chan_only**  `string`: save_displayed_chan_only from header global configuration <br>
    **headstage_firmware_version**  `string`: headstage_firmware_version from header global configuration <br>
    **qt_version**  `string`: qt_version from header global configuration <br>
    **compile_date**  `string`: compile_date from header global configuration <br>
    **compile_time**  `string`: compile_time from header global configuration <br>
    **file_prefix**  `string`: file_prefix from header global configuration <br>
    **headstage_gyro_sensor_on**  `string`: headstage_gyro_sensor_on from header global configuration <br>
    **headstage_mag_sensor_on**  `string`: headstage_mag_sensor_on from header global configuration <br>
    **trodes_version**  `string`: trodes_version from header global configuration <br>
    **headstage_accel_sensor_on**  `string`: headstage_accel_sensor_on from header global configuration <br>
    **commit_head**  `string`: commit_head from header global configuration <br>
    **system_time_at_creation**  `string`: system_time_at_creation from header global configuration <br>
    **file_path**  `string`: file_path from header global configuration <br>

#### NTrode
Representation of NTrode object in NWB <br>
**Attributes:** <br>
    **ntrode_id**  `int`: id of electrode group <br>
    **electrode_group_id**  `int`: id of electrode group<br>
    **bad_channels**  `array_data`: ids of bad channel <br>
    **map**  `array_data`: map of ntrode <br>
    
#### Probe
Representation of Probe object in NWB <br>
**Attributes:** <br>
    **id**  `int`: unique id of the probe <br>
    **probe_type**  `string`: type of probe <br>
    **units**  `string`: units in device <br>
    **probe_description**  `string`: probe_description of probe <br>
    **num_shanks**  `int`: number of shanks associated with probe <br>
    **contact_side_numbering**  `bool`: is contact_side_numbering enabled <br>
    **contact_size**  `float`: value of contact size as float <br>
    **shanks**  `object`: shanks in the probe <br>

This extension was created using [ndx-template](https://github.com/nwb-extensions/ndx-template).
