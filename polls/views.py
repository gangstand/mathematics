from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from polls.models import Profile, Question, Answer


class PollsListView(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = 'polls_list'
    template_name = 'polls/list_polls.html'
    login_url = 'login'


class PoolsDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    context_object_name = 'polls'
    template_name = 'polls/detail_polls.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(PoolsDetailView, self).get_context_data(**kwargs)
        context['Question'] = Question.objects.all()
        context['Answer'] = Answer.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            answer = request.POST.getlist('answer')
            print(answer)
            print(answer.count('False'))
            profile = Profile.objects.all()
            return render(request, 'polls/result.html', {"answer": answer.count('True'), "profile": profile})
