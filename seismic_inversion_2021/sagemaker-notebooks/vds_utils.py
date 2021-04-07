"""
Copyright 2021 Data Science and ML Geosciences Group

This module includes data query convenience functions for OpenVDS+ data.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import openvds


def print_channel_info(layout):
    print("ChannelCount: {}".format(layout.getChannelCount()))
    for i in range(layout.getChannelCount()):
        print("  Channel Name: {}".format(layout.getChannelName(i)))
        print("    Value range: {} - {}".format(layout.getChannelValueRangeMin(i), layout.getChannelValueRangeMax(i)))

    print("Dimensionality: {}".format(layout.getDimensionality()))
    for i in range(layout.getDimensionality()):
        print("  Dimension name: {}".format(layout.getDimensionName(i)))
        print("    Number of samples: {}".format(layout.getDimensionNumSamples(i)))
        print("    Coordinate min max {} - {}".format(layout.getDimensionMin(i), layout.getDimensionMax(i)))


def print_crs_metadata(layout):
    if layout.isMetadataDoubleVector2Available("SurveyCoordinateSystem", "Origin"):
        print("SurveyCoordinateSystem::Origin: {}".format(
            layout.getMetadataDoubleVector2("SurveyCoordinateSystem", "Origin")))
    if layout.isMetadataDoubleVector2Available("SurveyCoordinateSystem", "InlineSpacing"):
        print("SurveyCoordinateSystem::InlineSpacing: {}".format(
            layout.getMetadataDoubleVector2("SurveyCoordinateSystem", "InlineSpacing")))
    if layout.isMetadataDoubleVector2Available("SurveyCoordinateSystem", "CrosslineSpacing"):
        print("SurveyCoordinateSystem::CrosslineSpacing: {}".format(
            layout.getMetadataDoubleVector2("SurveyCoordinateSystem", "CrosslineSpacing")))


def get_slice(access_manager, layout, slice_type, slice_coordinate, lod=0):
    slice_type = slice_type.lower()

    if slice_type in ['inline', 'iline', 'il']:
        slice_dim = 2
        dimensions_nd = openvds.DimensionsND.Dimensions_01
    elif slice_type in ['crossline', 'xline', 'xl']:
        slice_dim = 1
        dimensions_nd = openvds.DimensionsND.Dimensions_02
    elif slice_type in ['timeslice', 'twt', 'time', 'depthslice', 'z', 'depth']:
        slice_dim = 0
        dimensions_nd = openvds.DimensionsND.Dimensions_12
    else:
        slice_dim = -1

    slice_descriptor = layout.getAxisDescriptor(slice_dim)

    dim_min, dim_max = slice_descriptor.getCoordinateMin(), slice_descriptor.getCoordinateMax()

    if slice_coordinate < dim_min  or slice_coordinate > dim_max:
        raise IndexError(f"Slice coordinate {slice_coordinate} out of range. {slice_type} range: {dim_min, dim_max}")

    slice_index = slice_descriptor.coordinateToSampleIndex(slice_coordinate)

    min_slice = tuple(slice_index + 0 if dim == slice_dim else 0 for dim in range(6))
    max_slice = tuple(slice_index + 1 if dim == slice_dim else layout.getDimensionNumSamples(dim) for dim in range(6))

    req = access_manager.requestVolumeSubset(min_slice, max_slice,
                                             format=openvds.VolumeDataChannelDescriptor.Format.Format_R32,
                                             dimensionsND=dimensions_nd)

    height = max_slice[0] if slice_dim != 0 else max_slice[1]
    width = max_slice[2] if slice_dim != 2 else max_slice[1]

    data = req.data.reshape(width, height)

    return data


def get_minicube(access_manager, layout, il_range, xl_range, z_range):
    query_ranges = {
        0: z_range,
        1: xl_range,
        2: il_range,
    }

    min_slice = ()
    max_slice = ()

    # Work on z, il, xl ranges
    for dim in range(3):
        slice_descriptor = layout.getAxisDescriptor(dim)
        dim_min, dim_max = slice_descriptor.getCoordinateMin(), slice_descriptor.getCoordinateMax()

        # Compare if min/max out of range, raise error if it is.
        if query_ranges[dim][0] < dim_min or query_ranges[dim][1] > dim_max:
            raise IndexError(f"Dimension {dim} Slice {query_ranges[dim]} out of range. {dim} range: {dim_min, dim_max}")

        dim_index_min = slice_descriptor.coordinateToSampleIndex(query_ranges[dim][0])
        dim_index_max = slice_descriptor.coordinateToSampleIndex(query_ranges[dim][1]) + 1

        min_slice += (dim_index_min,)
        max_slice += (dim_index_max,)

    # Insert last 3 dimension ranges
    min_slice += (0, 0, 0)
    max_slice += (1, 1, 1)

    req = access_manager.requestVolumeSubset(min_slice, max_slice,
                                             format=openvds.VolumeDataChannelDescriptor.Format.Format_R32,
                                             dimensionsND=openvds.DimensionsND.Dimensions_012)

    height = max_slice[2] - min_slice[2]
    width = max_slice[1] - min_slice[1]
    depth = max_slice[0] - min_slice[0]

    data = req.data.reshape(height, width, depth)

    return data
