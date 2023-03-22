"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from authentication import views as auth_views
from website import views as website_views
from network import views as network_views
from creation import views as creation_views
from delete import views as delete_views

app_name = 'litreview'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginPage.as_view(), name='login'),
    path('signup/', auth_views.SignUpPage.as_view(), name='signup'),
    path('logout/', auth_views.logout_user, name='logout'),
    path('feed/', website_views.feed, name='feed'),
    path('<slug:username>/', include('network.urls', namespace='network')),
    path('<slug:username>/posts', creation_views.userPostHistory.as_view(), name='user_posts'),
    path('<slug:username>/subscription/', network_views.UserNetwork.as_view(), name='subscription'),
    path('<slug:username>/unfollow/', network_views.UnfollowUser.as_view(), name='unfollow'),
    path('<slug:username>/newticket/', creation_views.creationTicketView.as_view(), name='create_ticket'),
    path('<slug:username>/newreview/', creation_views.creationReviewView.as_view(), name='create_review'),
    path('<slug:username>/addreview/', creation_views.addReviewView.as_view(), name='add_review'),
    path('<slug:username>/review/<int:post_id>/update/', creation_views.updateReviewView.as_view(), name='update_review'),
    path('<slug:username>/ticket/<int:post_id>/update/', creation_views.updateTicketView.as_view(), name='update_ticket'),
    path('<slug:username>/review/<int:post_id>/delete/', delete_views.reviewDeletion.as_view(), name='delete_review'),
    path('<slug:username>/ticket/<int:post_id>/delete/', delete_views.ticketDeletion.as_view(), name='delete_ticket'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
