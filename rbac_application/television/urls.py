from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TelevisionList

urlpatterns = [
    path('', TelevisionList.as_view()),
    path('edit', TelevisionList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)