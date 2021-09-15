# Copyright 2020 kubeflow.org.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    KFServing

    Python SDK for KFServing  # noqa: E501

    The version of the OpenAPI document: v0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kfserving
from kfserving.models.v1beta1_predictors_config import V1beta1PredictorsConfig  # noqa: E501
from kfserving.rest import ApiException

class TestV1beta1PredictorsConfig(unittest.TestCase):
    """V1beta1PredictorsConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1PredictorsConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kfserving.models.v1beta1_predictors_config.V1beta1PredictorsConfig()  # noqa: E501
        if include_optional :
            return V1beta1PredictorsConfig(
                onnx = kfserving.models.v1beta1_predictor_config.V1beta1PredictorConfig(
                    default_gpu_image_version = '0', 
                    default_image_version = '0', 
                    image = '0', 
                    supported_frameworks=['0'] ), 
                pytorch = kfserving.models.v1beta1_predictor_config.V1beta1PredictorConfig(
                    default_gpu_image_version = '0', 
                    default_image_version = '0', 
                    image = '0',
                    supported_frameworks=['0'] ), 
                sklearn = kfserving.models.v1beta1_predictor_config.V1beta1PredictorConfig(
                    default_gpu_image_version = '0', 
                    default_image_version = '0', 
                    image = '0',
                    supported_frameworks=['0'] ), 
                tensorflow = kfserving.models.v1beta1_predictor_config.V1beta1PredictorConfig(
                    default_gpu_image_version = '0', 
                    default_image_version = '0', 
                    image = '0',
                    supported_frameworks=['0'] ), 
                triton = kfserving.models.v1beta1_predictor_config.V1beta1PredictorConfig(
                    default_gpu_image_version = '0', 
                    default_image_version = '0', 
                    image = '0',
                    supported_frameworks=['0'] ),
                xgboost = kfserving.models.v1beta1_predictor_config.V1beta1PredictorConfig(
                    default_gpu_image_version = '0', 
                    default_image_version = '0', 
                    image = '0',
                    supported_frameworks=['0'] ),
            )
        else :
            return V1beta1PredictorsConfig(
        )

    def testV1beta1PredictorsConfig(self):
        """Test V1beta1PredictorsConfig"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()