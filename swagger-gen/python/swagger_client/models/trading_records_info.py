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


class TradingRecordsInfo(object):
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
        'id': 'int',
        'symbol': 'str',
        'price': 'float',
        'qty': 'float',
        'side': 'str',
        'time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'symbol': 'symbol',
        'price': 'price',
        'qty': 'qty',
        'side': 'side',
        'time': 'time'
    }

    def __init__(self, id=None, symbol=None, price=None, qty=None, side=None, time=None):  # noqa: E501
        """TradingRecordsInfo - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._symbol = None
        self._price = None
        self._qty = None
        self._side = None
        self._time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if symbol is not None:
            self.symbol = symbol
        if price is not None:
            self.price = price
        if qty is not None:
            self.qty = qty
        if side is not None:
            self.side = side
        if time is not None:
            self.time = time

    @property
    def id(self):
        """Gets the id of this TradingRecordsInfo.  # noqa: E501


        :return: The id of this TradingRecordsInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TradingRecordsInfo.


        :param id: The id of this TradingRecordsInfo.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def symbol(self):
        """Gets the symbol of this TradingRecordsInfo.  # noqa: E501


        :return: The symbol of this TradingRecordsInfo.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this TradingRecordsInfo.


        :param symbol: The symbol of this TradingRecordsInfo.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def price(self):
        """Gets the price of this TradingRecordsInfo.  # noqa: E501


        :return: The price of this TradingRecordsInfo.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this TradingRecordsInfo.


        :param price: The price of this TradingRecordsInfo.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def qty(self):
        """Gets the qty of this TradingRecordsInfo.  # noqa: E501


        :return: The qty of this TradingRecordsInfo.  # noqa: E501
        :rtype: float
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this TradingRecordsInfo.


        :param qty: The qty of this TradingRecordsInfo.  # noqa: E501
        :type: float
        """

        self._qty = qty

    @property
    def side(self):
        """Gets the side of this TradingRecordsInfo.  # noqa: E501


        :return: The side of this TradingRecordsInfo.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this TradingRecordsInfo.


        :param side: The side of this TradingRecordsInfo.  # noqa: E501
        :type: str
        """

        self._side = side

    @property
    def time(self):
        """Gets the time of this TradingRecordsInfo.  # noqa: E501


        :return: The time of this TradingRecordsInfo.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this TradingRecordsInfo.


        :param time: The time of this TradingRecordsInfo.  # noqa: E501
        :type: str
        """

        self._time = time

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
        if issubclass(TradingRecordsInfo, dict):
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
        if not isinstance(other, TradingRecordsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
