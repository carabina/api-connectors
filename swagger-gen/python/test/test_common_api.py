# coding: utf-8

"""
    Bybit API

    ## REST API for the Bybit Exchange. Base URI: [https://api.bybit.com]    # noqa: E501

    OpenAPI spec version: 0.2.9
    Contact: support@bybit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.common_api import CommonApi  # noqa: E501
from swagger_client.rest import ApiException

from swagger_client.BybitApiClient import BybitApiClient

class TestCommonApi(unittest.TestCase):
    """CommonApi unit test stubs"""

    def setUp(self):

        bybitClient = swagger_client.BybitApiClient.BybitApiClient()
        self.api = swagger_client.api.common_api.CommonApi(api_client=bybitClient)  # noqa: E501

    def tearDown(self):
        pass

    def test_common_announcements(self):
        """Test case for common_announcements

        Get Bybit OpenAPI announcements in the last 30 days in reverse order.  # noqa: E501
        """

        data = self.api.common_announcements()
        print(data)
        pass

    def test_common_get_lcp(self):
        """Test case for common_get_lcp

        Query LCP info.  # noqa: E501
        """
        pass

    def test_common_get_time(self):
        """Test case for common_get_time

        Get bybit server time.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
