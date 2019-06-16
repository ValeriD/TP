from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', views.BookView)
router.register('authors', views.AuthorView)
router.register('members', views.MemberView)

urlpatterns = [
    url('', include(router.urls))
]
