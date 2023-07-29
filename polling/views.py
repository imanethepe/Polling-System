from django.http import HttpResponseRedirect
from django.shortcuts import (
    render, get_object_or_404,
    )
from django.views.generic import View
from django.urls import reverse_lazy, reverse
from .models import Question, Choice
from .forms import QuestionForm


class QuestionList(View):
    """Get of the five last items of the list of questions"""

    model = Question
    template_name = 'polling/question_list.html'

    def get(self, request):
        latest_question_list = self.model.objects.order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, self.template_name, context)


class QuestionDetail(View):
    """Get of the question"""

    model = Question
    template_name = 'polling/question_detail.html'

    def get(self, request, pk):
        question = get_object_or_404(self.model, pk=pk)
        return render(
          request,
          self.template_name,
          {'question': question}
        )


class QuestionVote(View):
    """Get and post of voting choice"""

    form_class = QuestionForm
    model = Question
    template_name = 'polling/question_form_vote.html'

    def get(self, request, pk):
        question = get_object_or_404(
            self.model, pk=pk)
        context = {
            'form': self.form_class(instance=question),
            'question': question,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        question = get_object_or_404(
            self.model, pk=pk)

        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(
                request,
                self.template_name,
                {'question': question,
                 'error_message': "You didn't select a choice."},
            )
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(
                reverse('polling_question_result', kwargs={'pk': pk}))
            # return HttpResponseRedirect(
            #     reverse_lazy('polling_question_list'))


class QuestionResult(View):
    """Get of voting result for a question"""

    model = Question
    template_name = 'polling/question_result.html'

    def get(self, request, pk):
        question = get_object_or_404(
            self.model, pk=pk)
        return render(
            request,
            self.template_name,
            {'question': question}
            )
