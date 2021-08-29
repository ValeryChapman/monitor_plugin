# -*- coding: utf-8 -*-
from .server import MonitorRequest
from monitor_plugin.config import config


class MonitorAPIView(config.MONITOR_BASE_API_VIEW):

    def handle_exception(self, exc: Exception) -> (config.MONITOR_BASE_API_VIEW, None):

        # get error class
        exception_class = exc.__class__.__name__

        # check the error in the list of ignored errors
        if exception_class in config.MONITOR_IGNORE_LIST:
            return super().handle_exception(exc)
        
        # get error text
        exception_text = str(exc)

        # send error to monitor
        MonitorRequest().Error(exception_class, exception_text)

        # return base ApiView
        return super().handle_exception(exc)
    

def monitor_handle_exception(exc: Exception, context: dict):

    # get error class
    exception_class = exc.__class__.__name__
    
    # check the error in the list of ignored errors
    if exception_class in config.MONITOR_IGNORE_LIST:
        return
    
    # get error text
    exception_text = str(exc)

    # send error to monitor
    MonitorRequest().Error(exception_class, exception_text)
