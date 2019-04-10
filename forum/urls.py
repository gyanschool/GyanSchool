from django.urls import path,include
from .views import *

urlpatterns = [
    path('all', index),
    path('question/<int:qid>/<slug:qslug>', viewquestion),
    path('ask-question', askquestion),
    path('ajax-answer-question', ajaxanswerquestion)
]
