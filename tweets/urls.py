from django.urls import path
from django.views.generic.base import RedirectView
from .views import TweetDetailView , TweetListView, TweetCreateView , TweetUpdateView, TweetDeleteView, RetweetView
app_name='tweet'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/')),
    path('search/', TweetListView.as_view() ,name='list'),
    path('create/', TweetCreateView.as_view() ,name='create'),
    path('<pk>/update/', TweetUpdateView.as_view() ,name='create'),
    path('<pk>/delete/', TweetDeleteView.as_view() ,name='delete'),
    path('<pk>/', TweetDetailView.as_view() ,name='detail'),
    path('<pk>/retweet/', RetweetView.as_view() ,name='retweet'),


]