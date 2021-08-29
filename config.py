# -*- coding: utf-8 -*-
from django.conf import settings
import importlib
from monitor_plugin.defaults import default_monitor_route, base_api_view


class Settings:
    
    @property
    def MONITOR_ROUTE(self):
        return getattr(settings, "MONITOR_ROUTE", default_monitor_route)

    @property
    def MONITOR_PROJECT_ID(self):
        return getattr(settings, "MONITOR_PROJECT_ID", None)

    @property
    def MONITOR_ASYNC_CALLING(self):
        return getattr(settings, "MONITOR_ASYNC_CALLING", False)

    @property
    def MONITOR_IGNORE_LIST(self):
        return getattr(settings, "MONITOR_IGNORE_LIST", [])
    
    @property
    def MONITOR_BASE_API_VIEW(self):
        class_string = getattr(settings, "MONITOR_BASE_API_VIEW", base_api_view)

        # dir path to api class
        dir_path = ""
        dir_path = ".".join(class_string.split(".")[:-1])

        return getattr(importlib.import_module(dir_path), class_string.split(".")[-1])


config = Settings()
