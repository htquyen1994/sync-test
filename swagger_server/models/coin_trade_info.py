# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CoinTradeInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, coin: str=None, amount: str=None, price: int=None):  # noqa: E501
        """CoinTradeInfo - a model defined in Swagger

        :param coin: The coin of this CoinTradeInfo.  # noqa: E501
        :type coin: str
        :param amount: The amount of this CoinTradeInfo.  # noqa: E501
        :type amount: str
        :param price: The price of this CoinTradeInfo.  # noqa: E501
        :type price: int
        """
        self.swagger_types = {
            'coin': str,
            'amount': str,
            'price': int
        }

        self.attribute_map = {
            'coin': 'coin',
            'amount': 'amount',
            'price': 'price'
        }

        self._coin = coin
        self._amount = amount
        self._price = price

    @classmethod
    def from_dict(cls, dikt) -> 'CoinTradeInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CoinTradeInfo of this CoinTradeInfo.  # noqa: E501
        :rtype: CoinTradeInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def coin(self) -> str:
        """Gets the coin of this CoinTradeInfo.

        Coin  # noqa: E501

        :return: The coin of this CoinTradeInfo.
        :rtype: str
        """
        return self._coin

    @coin.setter
    def coin(self, coin: str):
        """Sets the coin of this CoinTradeInfo.

        Coin  # noqa: E501

        :param coin: The coin of this CoinTradeInfo.
        :type coin: str
        """

        self._coin = coin

    @property
    def amount(self) -> str:
        """Gets the amount of this CoinTradeInfo.

        User name  # noqa: E501

        :return: The amount of this CoinTradeInfo.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount: str):
        """Sets the amount of this CoinTradeInfo.

        User name  # noqa: E501

        :param amount: The amount of this CoinTradeInfo.
        :type amount: str
        """

        self._amount = amount

    @property
    def price(self) -> int:
        """Gets the price of this CoinTradeInfo.

        long  # noqa: E501

        :return: The price of this CoinTradeInfo.
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price: int):
        """Sets the price of this CoinTradeInfo.

        long  # noqa: E501

        :param price: The price of this CoinTradeInfo.
        :type price: int
        """

        self._price = price
