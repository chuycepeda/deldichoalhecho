from django.conf.urls import patterns, url
from .views import BackendHomeView, InstanceDetailView, CSVUploadView, StyleView, CategoryCreateView, \
    PromiseCreateView, PromiseUpdateView, CreateInstanceView, TemplateUpdateView, CategoryDeleteView


urlpatterns = patterns('',
                       url(r'^/?$', BackendHomeView.as_view(), name='home'),
                       url(r'^/create-instance/?$', CreateInstanceView.as_view(), name='create_instance'),
                       url(r'^detail/(?P<slug>[\w-]+)/?$', InstanceDetailView.as_view(), name='instance'),
                       url(r'^detail/(?P<slug>[\w-]+)/category_create/?$', CategoryCreateView.as_view(), name='create_category'),
                       url(r'^detail/(?P<pk>[\d-]+)/category_confirm_delete/?$', CategoryDeleteView.as_view(), name='delete_category'),
                       url(r'^detail/(?P<slug>[\w-]+)/template_update/?$', TemplateUpdateView.as_view(), name='update_template'),
                       url(r'^detail/(?P<label>[\w-]+)/(?P<category_id>[\w-]+)/promise_create/?$', PromiseCreateView.as_view(), name='create_promise'),
                       url(r'^detail/(?P<pk>[\d-]+)/promise_update/?$', PromiseUpdateView.as_view(), name='update_promise'),
                       url(r'^detail/(?P<slug>[\w-]+)/style/?$', StyleView.as_view(), name='instance_style'),
                       url(r'^detail/(?P<slug>[\w-]+)/upload/?$', CSVUploadView.as_view(), name='csv_upload'),
                       )
