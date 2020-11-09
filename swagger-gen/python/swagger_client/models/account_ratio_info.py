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


class AccountRatioInfo(object):
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
        'buy_ratio': 'int',
        'sell_ratio': 'int',
        'timestamp': 'int',
        'symbol': 'str'
    }

    attribute_map = {
        'buy_ratio': 'buy_ratio',
        'sell_ratio': 'sell_ratio',
        'timestamp': 'timestamp',
        'symbol': 'symbol'
    }

    def __init__(self, buy_ratio=None, sell_ratio=None, timestamp=None, symbol=None):  # noqa: E501
        """AccountRatioInfo - a model defined in Swagger"""  # noqa: E501

        self._buy_ratio = None
        self._sell_ratio = None
        self._timestamp = None
        self._symbol = None
        self.discriminator = None

        if buy_ratio is not None:
            self.buy_ratio = buy_ratio
        if sell_ratio is not None:
            self.sell_ratio = sell_ratio
        if timestamp is not None:
            self.timestamp = timestamp
        if symbol is not None:
            self.symbol = symbol

    @property
    def buy_ratio(self):
        """Gets the buy_ratio of this AccountRatioInfo.  # noqa: E501


        :return: The buy_ratio of this AccountRatioInfo.  # noqa: E501
        :rtype: int
        """
        return self._buy_ratio

    @buy_ratio.setter
    def buy_ratio(self, buy_ratio):
        """Sets the buy_ratio of this AccountRatioInfo.


        :param buy_ratio: The buy_ratio of this AccountRatioInfo.  # noqa: E501
        :type: int
        """

        self._buy_ratio = buy_ratio

    @property
    def sell_ratio(self):
        """Gets the sell_ratio of this AccountRatioInfo.  # noqa: E501


        :return: The sell_ratio of this AccountRatioInfo.  # noqa: E501
        :rtype: int
        """
        return self._sell_ratio

    @sell_ratio.setter
    def sell_ratio(self, sell_ratio):
        """Sets the sell_ratio of this AccountRatioInfo.


        :param sell_ratio: The sell_ratio of this AccountRatioInfo.  # noqa: E501
        :type: int
        """

        self._sell_ratio = sell_ratio

    @property
    def timestamp(self):
        """Gets the timestamp of this AccountRatioInfo.  # noqa: E501


        :return: The timestamp of this AccountRatioInfo.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this AccountRatioInfo.


        :param timestamp: The timestamp of this AccountRatioInfo.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def symbol(self):
        """Gets the symbol of this AccountRatioInfo.  # noqa: E501


        :return: The symbol of this AccountRatioInfo.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this AccountRatioInfo.


        :param symbol: The symbol of this AccountRatioInfo.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

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
        if issubclass(AccountRatioInfo, dict):
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
        if not isinstance(other, AccountRatioInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
