from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import News

# Create your views here.
# def home(request):
# 	return render(request, 'news/home.html', {'message': 'Hello world news!'})


class IndexView(generic.ListView):
    template_name = 'news/home.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        # return News.objects.order_by('-created_on')[:20]
        return News.objects.select_related('created_by').order_by('-created_on')[:20]

class DetailView(generic.DetailView):
    model = News
    template_name = 'news/detail.html'
    context_object_name = 'news'


class MyView(IndexView):

	def get_queryset(self):
		return News.objects.filter(created_by=self.request.user.id) \
			.order_by('-created_on')[:20]

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(MyView, self).dispatch(*args, **kwargs)	

class NewNewsView(generic.edit.CreateView):
    model = News
    fields = ['text', 'via']
    success_url = "/my/"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(NewNewsView, self).form_valid(form)

class EditNewsView(generic.edit.UpdateView):
    model = News
    fields = ['text', 'via']
    success_url = "/my/"

    def get_queryset(self):
        base_qs = super(EditNewsView, self).get_queryset()
        return base_qs.filter(created_by=self.request.user)    		