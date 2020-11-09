# coding: utf-8

"""
    Bybit API

    ## REST API for the Bybit Exchange. Base URI: [https://api.bybit.com]    # noqa: E501

    OpenAPI spec version: 0.2.9
    Contact: support@bybit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.linear_list_stop_order_result import LinearListStopOrderResult  # noqa: F401,E501


class LinearStopOrderRecordsResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'current_page': 'int',
        'last_page': 'int',
        'data': 'list[LinearListStopOrderResult]'
    }

    attribute_map = {
        'current_page': 'current_page',
        'last_page': 'last_page',
        'data': 'data'
    }

    def __init__(self, current_page=None, last_page=None, data=None):  # noqa: E501
        """LinearStopOrderRecordsResponse - a model defined in Swagger"""  # noqa: E501

        self._current_page = None
        self._last_page = None
        self._data = None
        self.discriminator = None

        if current_page is not None:
            self.current_page = current_page
        if last_page is not None:
            self.last_page = last_page
        if data is not None:
            self.data = data

    @property
    def current_page(self):
        """Gets the current_page of this LinearStopOrderRecordsResponse.  # noqa: E501


        :return: The current_page of this LinearStopOrderRecordsResponse.  # noqa: E501
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this LinearStopOrderRecordsResponse.


        :param current_page: The current_page of this LinearStopOrderRecordsResponse.  # noqa: E501
        :type: int
        """

        self._current_page = current_page

    @property
    def last_page(self):
        """Gets the last_page of this LinearStopOrderRecordsResponse.  # noqa: E501


        :return: The last_page of this LinearStopOrderRecordsResponse.  # noqa: E501
        :rtype: int
        """
        return self._last_page

    @last_page.setter
    def last_page(self, last_page):
        """Sets the last_page of this LinearStopOrderRecordsResponse.


        :param last_page: The last_page of this LinearStopOrderRecordsResponse.  # noqa: E501
        :type: int
        """

        self._last_page = last_page

    @property
    def data(self):
        """Gets the data of this LinearStopOrderRecordsResponse.  # noqa: E501


        :return: The data of this LinearStopOrderRecordsResponse.  # noqa: E501
        :rtype: list[LinearListStopOrderResult]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this LinearStopOrderRecordsResponse.


        :param data: The data of this LinearStopOrderRecordsResponse.  # noqa: E501
        :type: list[LinearListStopOrderResult]
        """

        self._data = data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(LinearStopOrderRecordsResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LinearStopOrderRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
