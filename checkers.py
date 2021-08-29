# -*- coding: utf-8 -*-
import requests


def service_on(url: str) -> bool:
    try:
        requests.head(url)
        return True
    except:
        return False


def is_integer(num: int) -> bool:
    return str(num).isdigit()
