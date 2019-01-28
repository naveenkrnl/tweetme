from django.urls import path
from django.views.generic.base import RedirectView
from .views import UserDetailView, UserFollowView
app_name='accounts'

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', RedirectView.as_view(url='/')),
    # path('search/', TweetListView.as_view() ,name='list'),
    # path('create/', TweetCreateView.as_view() ,name='create'),
    # path('<pk>/update/', TweetUpdateView.as_view() ,name='create'),
    # path('<pk>/delete/', TweetDeleteView.as_view() ,name='delete'),
    path('<username>/', UserDetailView.as_view() ,name='detail'),
    path('<username>/follow/', UserFollowView.as_view() ,name='follow'),
]