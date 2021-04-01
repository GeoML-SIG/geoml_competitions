"""
Copyright 2021 Data Science and ML Geosciences Group

This module includes plotting convenience functions for the competition.

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

import unittest
import openvds


class TestAPI(unittest.TestCase):
    def setUp(self):
        """ export valid keys to run this."""
        from os import getenv
        
        region = 'us-east-1'

        # you can code your credentials here, not best practice though.
        aws_key = getenv('AWS_ACCESS_KEY_ID')
        aws_secret = getenv('AWS_SECRET_ACCESS_KEY')

        region_config = f"Region={region}"
        key_config = f"AccessKeyId={aws_key}"
        secret_config = f"SecretKey={aws_secret}"

        self.aws_config = ';'.join([
            region_config,
            key_config,
            secret_config,
        ])
        
        self.vds_url = 's3://geophysics-on-cloud/poseidon/seismic/vds/psdn11_TbsdmF_full_w_AGC_Nov11/'

    def test_connection(self):
        """Test out the dimensions of things. Use this to check the install."""
        vds_handle = openvds.open(
            url=self.vds_url,
            connectionString=self.aws_config,
        )

        layout = openvds.getLayout(vds_handle)

        self.assertEqual(layout.getChannelCount(), 3)

        self.assertEqual(layout.getChannelName(0), 'Amplitude')
        self.assertEqual(layout.getChannelValueRangeMin(0), -15334.1142578125)        
        self.assertEqual(layout.getChannelValueRangeMax(0),  15334.1142578125)        

        self.assertEqual(layout.getChannelName(1), 'Trace')
        self.assertEqual(layout.getChannelValueRangeMin(1), 0.0)        
        self.assertEqual(layout.getChannelValueRangeMax(1), 256.0)        

        self.assertEqual(layout.getChannelName(2), 'SEGYTraceHeader')
        self.assertEqual(layout.getChannelValueRangeMin(2), 0.0)        
        self.assertEqual(layout.getChannelValueRangeMax(2), 256.0)

        self.assertEqual(layout.getDimensionality(), 3)

        self.assertEqual(layout.getDimensionName(0), "Sample")
        self.assertEqual(layout.getDimensionNumSamples(0), 1501)
        self.assertEqual(layout.getDimensionMin(0), 0.0)
        self.assertEqual(layout.getDimensionMax(0), 6000.0)

        self.assertEqual(layout.getDimensionName(1), "Crossline")        
        self.assertEqual(layout.getDimensionNumSamples(1), 5053)
        self.assertEqual(layout.getDimensionMin(1), 504.0)
        self.assertEqual(layout.getDimensionMax(1), 5556.0)

        self.assertEqual(layout.getDimensionName(2), "Inline")        
        self.assertEqual(layout.getDimensionNumSamples(2), 3437)
        self.assertEqual(layout.getDimensionMin(2), 983.0)
        self.assertEqual(layout.getDimensionMax(2), 4419.0)

        access_manager = openvds.VolumeDataAccessManager(vds_handle)

        layout = openvds.getLayout(vds_handle)
        
        axis_descriptors = [layout.getAxisDescriptor(dim) for dim in range(layout.getDimensionality())]
        names = [print(axis.getName()) for axis in axis_descriptors]
    
        openvds.close(vds_handle)
