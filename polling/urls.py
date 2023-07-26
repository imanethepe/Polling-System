# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 16:01:08 2023

@author: Imanethepe
"""

from django.urls import path
from .views import QuestionList

urlpatterns = [
    path('',
         QuestionList.as_view(),
         name='polling_question_list'),
]
