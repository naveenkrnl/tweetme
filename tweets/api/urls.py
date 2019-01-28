from django.urls import path
from django.views.generic.base import RedirectView
from .views import TweetListAPIView,TweetCreateAPIView
app_name='tweet'

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', RedirectView.as_view(url='/')),
    path('', TweetListAPIView.as_view() ,name='list'),
    path('create/', TweetCreateAPIView.as_view() ,name='create'),
    # path('<pk>/update/', TweetUpdateView.as_view() ,name='create'),
    # path('<pk>/delete/', TweetDeleteView.as_view() ,name='delete'),
    # path('<pk>/', TweetDetailView.as_view() ,name='detail'),


]