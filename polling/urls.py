# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 16:01:08 2023

@author: Imanethepe
"""

from django.urls import path, re_path
from .views import (
    QuestionList, QuestionDetail,
    QuestionVote, QuestionResult
    )

urlpatterns = [
    path('',
         QuestionList.as_view(),
         name='polling_question_list'),
    re_path(r'question/(?P<pk>\d+)/$',
            QuestionDetail.as_view(),
            name='polling_question_detail'),
    re_path(r'question/(?P<pk>\d+)/vote$',
            QuestionVote.as_view(),
            name='polling_question_vote'),
    re_path(r'question/(?P<pk>\d+)/result$',
            QuestionResult.as_view(),
            name='polling_question_result'),
]
