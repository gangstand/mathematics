from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from polls.models import Profile, Question, Answer, Result
from users.models import CustomUser


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
            answer = request.POST.getlist('answer').count('True')
            print(request.POST.getlist('answer'))
            users = CustomUser.objects.all().values_list('last_name', flat=True)
            profile = Profile.objects.all()
            profileid = profile.values_list('name', flat=True)

            Result.objects.create(profileid=profileid, rating=answer, username=users)
            return render(request, 'polls/result.html', {"answer": answer, "profile": profile})
