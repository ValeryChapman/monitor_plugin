# -*- coding: utf-8 -*-
import requests
import json
import threading
from monitor_plugin.config import config
from .checkers import *


class Request:

    def __init__(self):

        # server api route
        self.SERVER_ROUTE = config.MONITOR_ROUTE
        
    # method: GET —> Request
    def Get(self, route: str) -> bool:

        # request url
        url = f"{self.SERVER_ROUTE}{route}"

        # check url
        if not service_on(url):
            return
        
        # send a request and get response data
        response = requests.request("GET", url)

        # check status code
        if response.status_code != 200:
            return False

        # convert response data to JSON format
        response = response.json()

        # return status
        return True if response.get("status", None) == "OK" else False

    # method: POST —> Request
    def Post(self, route: str, data: dict) -> bool:

        # request url
        url = f"{self.SERVER_ROUTE}{route}"

        # check url
        if not service_on(url):
            return

        # request body
        payload = json.dumps(data)
        
        # request headers
        headers = {
            'Content-Type': 'application/json'
        }

        # send a request and get response data
        response = requests.request("POST", url, headers=headers, data=payload)

        # check status code
        if response.status_code != 200:
            return False

        # convert response data to JSON format
        response = response.json()
        
        # return status
        return True if response.get("status", None) == "OK" else False


class MonitorRequest:

    def __init__(self):

        # project id
        self.PROJECT = config.MONITOR_PROJECT_ID if is_integer(config.MONITOR_PROJECT_ID) else None
        
        # async calling
        self.MONITOR_ASYNC_CALLING = config.MONITOR_ASYNC_CALLING if isinstance(config.MONITOR_ASYNC_CALLING, bool) else False
    
    # error —> create —> request
    def Error(self, name: str, text: str) -> None:

        # request route
        route = "/errors/create"
        
        # formatting the request data
        data = {
            "name":    name, 
            "text":    text,
            "project": self.PROJECT
        }

        # async calling
        if self.MONITOR_ASYNC_CALLING:
            threading.Thread(target=Request().Post, args=[route, data]).start()
            return
        
        Request().Post(route, data)