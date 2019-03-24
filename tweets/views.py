from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Tweet
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.views import View
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
# Create your views here.
class RetweetView(View):
    def get(self, request, pk, *args, **kwargs):
        tweet= get_object_or_404(Tweet, pk=pk)
        if request.user.is_authenticated:
            new_tweet=Tweet.objects.retweet(request.user, tweet)
            return HttpResponseRedirect("/")
        return HttpResponseRedirect(tweet.get_absolute_url)
#CREATE

class TweetCreateView(FormUserNeededMixin, CreateView):
    # queryset=Tweet.objects.all()
    form_class=TweetModelForm
    template_name="tweets/create_view.html"
    # success_url='/tweet/'
#UPDATE

class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset=Tweet.objects.all()
    form_class=TweetModelForm
    template_name="tweets/update_view.html"
    success_url='/tweet/'
    # login_url='admin/'
    

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model=Tweet
    template_name='tweets/delete_confirm.html'
    success_url=reverse_lazy('tweet:list')

class TweetDetailView(DetailView):
    template_name= "tweets/detail_view.html"
    queryset=Tweet.objects.all()
    
    # def get_object(self):
    #     pk=self.kwargs.get("pk")
    #     return Tweet.objects.get(id=pk)


class TweetListView(ListView):
    template_name= "tweets/list_view.html"
    # queryset=Tweet.objects.all()
    def get_queryset(self, *args, **kwargs):
        qs=Tweet.objects.all()
        query=self.request.GET.get("q",None)
        if query is not None:
            qs=qs.filter(
                Q(content__icontains=query)|
                Q(user__username__icontains=query) # complex Q lookups                
                )
        return qs

    def get_context_data(self, *args, **kwargs):
        context=super(TweetListView, self).get_context_data(*args, **kwargs)
        context['create_form']= TweetModelForm()
        context['create_url']=reverse_lazy("tweet:create")
        return context
# REtrieve
# def tweet_detail_view(request,id=1):
#     obj=Tweet.objects.get(id=id)
#     context={
#         "object":obj
#     }
#     return render(request, "tweets/detail_view.html",context)

# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     context={
#         "object_list": queryset
#     }
#     return render(request, "tweets/list_view.html",context)