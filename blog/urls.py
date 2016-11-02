from django.conf.urls import include, url
from . import views
from blog.views import ReceberIdView

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<slug>[\w_-]+)/$', views.post_detail, name='post_detail'),
    url(r'^categoria/(?P<slug>[\w_-]+)/$', views.category_posts, name='category_posts'),
    url(r'^receber/id/$', ReceberIdView.as_view(),name='teste_formulario'),
]