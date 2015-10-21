from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysql_json.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','json_data.views.home'),
    url(r'^test/$', include('totest.urls')),
    url(r'(?P<card_id>\w+)/$','json_data.views.index'),
]
