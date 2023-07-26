from django.shortcuts import render
from django.views.generic import View
from .models import Question


class QuestionList(View):
    """Get of the five last items of the list of questions"""

    def get(self, request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, 'polling/question_list.html', context)
