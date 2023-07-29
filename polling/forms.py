# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:49:22 2023

@author: Imanethepe
"""

from django import forms
from .models import Question, Choice


class QuestionForm(forms.ModelForm):
    """Attributes similar to model"""

    class Meta:
        model = Question
        ﬁelds = '__all__'

    def clean_question_text(self):
        return self.cleaned_data['question_text'].lower()


class ChoiceForm(forms.ModelForm):
    """Attributes similar to model"""

    class Meta:
        model = Choice
        ﬁelds = '__all__'

    def clean_choice_text(self):
        return self.cleaned_data['choice_text'].lower()
