from django.urls import path
from .views import TweetDetailView , TweetListView, TweetCreateView , TweetUpdateView, TweetDeleteView
app_name='tweet'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', TweetListView.as_view() ,name='list'),
    path('create/', TweetCreateView.as_view() ,name='create'),
    path('<pk>/update/', TweetUpdateView.as_view() ,name='create'),
    path('<pk>/delete/', TweetDeleteView.as_view() ,name='delete'),
    path('<pk>/', TweetDetailView.as_view() ,name='detail'),


]