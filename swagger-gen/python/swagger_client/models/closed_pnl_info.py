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


class ClosedPnlInfo(object):
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
        'user_id': 'int',
        'symbol': 'str',
        'order_id': 'str',
        'side': 'str',
        'qty': 'int',
        'order_price': 'int',
        'order_type': 'str',
        'exec_type': 'str',
        'closed_size': 'int',
        'cum_entry_value': 'float',
        'avg_entry_price': 'int',
        'cum_exit_value': 'float',
        'avg_exit_price': 'int',
        'closed_pnl': 'float',
        'fill_count': 'int',
        'leverage': 'int',
        'created_at': 'int'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'user_id',
        'symbol': 'symbol',
        'order_id': 'order_id',
        'side': 'side',
        'qty': 'qty',
        'order_price': 'order_price',
        'order_type': 'order_type',
        'exec_type': 'exec_type',
        'closed_size': 'closed_size',
        'cum_entry_value': 'cum_entry_value',
        'avg_entry_price': 'avg_entry_price',
        'cum_exit_value': 'cum_exit_value',
        'avg_exit_price': 'avg_exit_price',
        'closed_pnl': 'closed_pnl',
        'fill_count': 'fill_count',
        'leverage': 'leverage',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, user_id=None, symbol=None, order_id=None, side=None, qty=None, order_price=None, order_type=None, exec_type=None, closed_size=None, cum_entry_value=None, avg_entry_price=None, cum_exit_value=None, avg_exit_price=None, closed_pnl=None, fill_count=None, leverage=None, created_at=None):  # noqa: E501
        """ClosedPnlInfo - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._user_id = None
        self._symbol = None
        self._order_id = None
        self._side = None
        self._qty = None
        self._order_price = None
        self._order_type = None
        self._exec_type = None
        self._closed_size = None
        self._cum_entry_value = None
        self._avg_entry_price = None
        self._cum_exit_value = None
        self._avg_exit_price = None
        self._closed_pnl = None
        self._fill_count = None
        self._leverage = None
        self._created_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if symbol is not None:
            self.symbol = symbol
        if order_id is not None:
            self.order_id = order_id
        if side is not None:
            self.side = side
        if qty is not None:
            self.qty = qty
        if order_price is not None:
            self.order_price = order_price
        if order_type is not None:
            self.order_type = order_type
        if exec_type is not None:
            self.exec_type = exec_type
        if closed_size is not None:
            self.closed_size = closed_size
        if cum_entry_value is not None:
            self.cum_entry_value = cum_entry_value
        if avg_entry_price is not None:
            self.avg_entry_price = avg_entry_price
        if cum_exit_value is not None:
            self.cum_exit_value = cum_exit_value
        if avg_exit_price is not None:
            self.avg_exit_price = avg_exit_price
        if closed_pnl is not None:
            self.closed_pnl = closed_pnl
        if fill_count is not None:
            self.fill_count = fill_count
        if leverage is not None:
            self.leverage = leverage
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this ClosedPnlInfo.  # noqa: E501


        :return: The id of this ClosedPnlInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClosedPnlInfo.


        :param id: The id of this ClosedPnlInfo.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this ClosedPnlInfo.  # noqa: E501


        :return: The user_id of this ClosedPnlInfo.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ClosedPnlInfo.


        :param user_id: The user_id of this ClosedPnlInfo.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def symbol(self):
        """Gets the symbol of this ClosedPnlInfo.  # noqa: E501


        :return: The symbol of this ClosedPnlInfo.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this ClosedPnlInfo.


        :param symbol: The symbol of this ClosedPnlInfo.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def order_id(self):
        """Gets the order_id of this ClosedPnlInfo.  # noqa: E501


        :return: The order_id of this ClosedPnlInfo.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ClosedPnlInfo.


        :param order_id: The order_id of this ClosedPnlInfo.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def side(self):
        """Gets the side of this ClosedPnlInfo.  # noqa: E501


        :return: The side of this ClosedPnlInfo.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this ClosedPnlInfo.


        :param side: The side of this ClosedPnlInfo.  # noqa: E501
        :type: str
        """

        self._side = side

    @property
    def qty(self):
        """Gets the qty of this ClosedPnlInfo.  # noqa: E501


        :return: The qty of this ClosedPnlInfo.  # noqa: E501
        :rtype: int
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this ClosedPnlInfo.


        :param qty: The qty of this ClosedPnlInfo.  # noqa: E501
        :type: int
        """

        self._qty = qty

    @property
    def order_price(self):
        """Gets the order_price of this ClosedPnlInfo.  # noqa: E501


        :return: The order_price of this ClosedPnlInfo.  # noqa: E501
        :rtype: int
        """
        return self._order_price

    @order_price.setter
    def order_price(self, order_price):
        """Sets the order_price of this ClosedPnlInfo.


        :param order_price: The order_price of this ClosedPnlInfo.  # noqa: E501
        :type: int
        """

        self._order_price = order_price

    @property
    def order_type(self):
        """Gets the order_type of this ClosedPnlInfo.  # noqa: E501


        :return: The order_type of this ClosedPnlInfo.  # noqa: E501
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this ClosedPnlInfo.


        :param order_type: The order_type of this ClosedPnlInfo.  # noqa: E501
        :type: str
        """

        self._order_type = order_type

    @property
    def exec_type(self):
        """Gets the exec_type of this ClosedPnlInfo.  # noqa: E501


        :return: The exec_type of this ClosedPnlInfo.  # noqa: E501
        :rtype: str
        """
        return self._exec_type

    @exec_type.setter
    def exec_type(self, exec_type):
        """Sets the exec_type of this ClosedPnlInfo.


        :param exec_type: The exec_type of this ClosedPnlInfo.  # noqa: E501
        :type: str
        """

        self._exec_type = exec_type

    @property
    def closed_size(self):
        """Gets the closed_size of this ClosedPnlInfo.  # noqa: E501


        :return: The closed_size of this ClosedPnlInfo.  # noqa: E501
        :rtype: int
        """
        return self._closed_size

    @closed_size.setter
    def closed_size(self, closed_size):
        """Sets the closed_size of this ClosedPnlInfo.


        :param closed_size: The closed_size of this ClosedPnlInfo.  # noqa: E501
        :type: int
        """

        self._closed_size = closed_size

    @property
    def cum_entry_value(self):
        """Gets the cum_entry_value of this ClosedPnlInfo.  # noqa: E501


        :return: The cum_entry_value of this ClosedPnlInfo.  # noqa: E501
        :rtype: float
        """
        return self._cum_entry_value

    @cum_entry_value.setter
    def cum_entry_value(self, cum_entry_value):
        """Sets the cum_entry_value of this ClosedPnlInfo.


        :param cum_entry_value: The cum_entry_value of this ClosedPnlInfo.  # noqa: E501
        :type: float
        """

        self._cum_entry_value = cum_entry_value

    @property
    def avg_entry_price(self):
        """Gets the avg_entry_price of this ClosedPnlInfo.  # noqa: E501


        :return: The avg_entry_price of this ClosedPnlInfo.  # noqa: E501
        :rtype: int
        """
        return self._avg_entry_price

    @avg_entry_price.setter
    def avg_entry_price(self, avg_entry_price):
        """Sets the avg_entry_price of this ClosedPnlInfo.


        :param avg_entry_price: The avg_entry_price of this ClosedPnlInfo.  # noqa: E501
        :type: int
        """

        self._avg_entry_price = avg_entry_price

    @property
    def cum_exit_value(self):
        """Gets the cum_exit_value of this ClosedPnlInfo.  # noqa: E501


        :return: The cum_exit_value of this ClosedPnlInfo.  # noqa: E501
        :rtype: float
        """
        return self._cum_exit_value

    @cum_exit_value.setter
    def cum_exit_value(self, cum_exit_value):
        """Sets the cum_exit_value of this ClosedPnlInfo.


        :param cum_exit_value: The cum_exit_value of this ClosedPnlInfo.  # noqa: E501
        :type: float
        """

        self._cum_exit_value = cum_exit_value

    @property
    def avg_exit_price(self):
        """Gets the avg_exit_price of this ClosedPnlInfo.  # noqa: E501


        :return: The avg_exit_price of this ClosedPnlInfo.  # noqa: E501
        :rtype: int
        """
        return self._avg_exit_price

    @avg_exit_price.setter
    def avg_exit_price(self, avg_exit_price):
        """Sets the avg_exit_price of this ClosedPnlInfo.


        :param avg_exit_price: The avg_exit_price of this ClosedPnlInfo.  # noqa: E501
        :type: int
        """

        self._avg_exit_price = avg_exit_price

    @property
    def closed_pnl(self):
        """Gets the closed_pnl of this ClosedPnlInfo.  # noqa: E501


        :return: The closed_pnl of this ClosedPnlInfo.  # noqa: E501
        :rtype: float
        """
        return self._closed_pnl

    @closed_pnl.setter
    def closed_pnl(self, closed_pnl):
        """Sets the closed_pnl of this ClosedPnlInfo.


        :param closed_pnl: The closed_pnl of this ClosedPnlInfo.  # noqa: E501
        :type: float
        """

        self._closed_pnl = closed_pnl

    @property
    def fill_count(self):
        """Gets the fill_count of this ClosedPnlInfo.  # noqa: E501


        :return: The fill_count of this ClosedPnlInfo.  # noqa: E501
        :rtype: int
        """
        return self._fill_count

    @fill_count.setter
    def fill_count(self, fill_count):
        """Sets the fill_count of this ClosedPnlInfo.


        :param fill_count: The fill_count of this ClosedPnlInfo.  # noqa: E501
        :type: int
        """

        self._fill_count = fill_count

    @property
    def leverage(self):
        """Gets the leverage of this ClosedPnlInfo.  # noqa: E501


        :return: The leverage of this ClosedPnlInfo.  # noqa: E501
        :rtype: int
        """
        return self._leverage

    @leverage.setter
    def leverage(self, leverage):
        """Sets the leverage of this ClosedPnlInfo.


        :param leverage: The leverage of this ClosedPnlInfo.  # noqa: E501
        :type: int
        """

        self._leverage = leverage

    @property
    def created_at(self):
        """Gets the created_at of this ClosedPnlInfo.  # noqa: E501


        :return: The created_at of this ClosedPnlInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ClosedPnlInfo.


        :param created_at: The created_at of this ClosedPnlInfo.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

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
        if issubclass(ClosedPnlInfo, dict):
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
        if not isinstance(other, ClosedPnlInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
