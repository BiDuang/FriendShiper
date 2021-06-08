"""
本模块为预置模块

提供一些实用函数
"""
from typing import Any


def negative_int_to_long(num: int) -> int:
    """
    将负整数转为正长整数

    在易语言函数长整数返回值出问题时可以使用

    比如群消息数据的self_qq sender_qq等

    :param num: 要转换的数值
    :return: 转换后的数值，如果数值为正则不转换
    """
    ...


def process_negative_int_obj(obj: Any) -> Any:
    """
    将含负整数的对象里的负整数转为正长整数，如果数值为正则不转换

    在易语言函数长整数返回值出问题时可以使用

    比如群消息数据的self_qq sender_qq等

    仅支持 int, list, tuple, dict，其他对象不转换

    :param obj: 要转换的对象
    :return: 转换后的对象
    """
    ...
