# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 11:11:30 2023

@author: Imanethepe
"""

from django.shortcuts import redirect


def redirect_root(request):
    return redirect('polling_question_list')
