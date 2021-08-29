# Monitor plugin for Django Rest Framework

## What is it?
....

## How to use it?
### Installation

#### Install the github repository and move the `monitor_plugin` folder to your django project.

#### Add `'monitor_plugin'` to your `INSTALLED_APPS` setting.
```python
INSTALLED_APPS = [
    ...
    'monitor_plugin',
]
```

#### Add `'MONITOR_PROJECT_ID'` to your project settings.
```python
MONITOR_PROJECT_ID = YOUR_MONITOR_PROJECT_ID
```

## Examples
### Example #1 - use `monitor_handle_exception` and Django Rest Framework `exception_handler`

#### Startup up a new project:
```
pip install django
pip install djangorestframework
- install monitor_plugin
django-admin startproject example .
./manage.py migrate
```

#### Now edit the `example/settings.py` module in your project:
```python
INSTALLED_APPS = [
    ...  # Make sure to include the default installed apps here.
    'rest_framework',
    'monitor_plugin'
]

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'monitor_plugin.views.monitor_handle_exception'
}

MONITOR_PROJECT_ID = 1 # Your monitor project ID
```

#### Edit the `example/urls.py` module in your project:
```python
from django.urls import re_path, include
from rest_framework.response import Response
from rest_framework.views import APIView


# Our test API view
class TestApiView(APIView):
    
    def get(self, request):
        
        # Some actions (calling an error)
        test_value_1 = "string"
        test_value_2 = 1
        result = test_value_1 + test_value_2

        # Return a response
        return Response({"result": result})

# Our routes
urlpatterns = [
    re_path(r'^test_route/?$', TestApiView.as_view()),
]
```

#### That's it, we're done!
```
./manage.py runserver
```

#### Now send a `GET` request to `http://localhost:8000/test_route`

## Monitor Plugin Settings
### MONITOR_PROJECT_ID - your project ID
Example:
```python
MONITOR_PROJECT_ID = 1
```
### MONITOR_BASE_API_VIEW - path to your api view
Example:
```python
MONITOR_BASE_API_VIEW = "api.utils.apibase.CustomAPIView"
```
### MONITOR_ASYNC_CALLING - make monitor_plugin asynchronous
Example:
```python
MONITOR_ASYNC_CALLING = True
```
### MONITOR_IGNORE_LIST - list of ignored errors
Example:
```python
MONITOR_IGNORE_LIST   = [
    "ValidationError",
    "TypeError"
]
```