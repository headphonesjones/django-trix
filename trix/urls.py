# from django.conf.urls import include, url
# from .views import AttachmentView


# urlpatterns = [
#     url(r'^attachment/$', AttachmentView.as_view()),
# ]

from django.urls import re_path, include
from .views import AttachmentView

urlpatterns = [
    re_path('attachment/', AttachmentView.as_view()),
]