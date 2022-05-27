# Copyright (C) 2012 Yaco Sistemas (http://www.yaco.es)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#            http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls import include
from django.urls import re_path
from django.contrib import admin

from djangosaml2 import views


urlpatterns = [
    re_path(r'^login/$', views.login, name='saml2_login'),
    re_path(r'^acs/$', views.assertion_consumer_service, name='saml2_acs'),
    re_path(r'^logout/$', views.logout, name='saml2_logout'),
    re_path(r'^ls/$', views.logout_service, name='saml2_ls'),
    re_path(r'^ls/post/$', views.logout_service_post, name='saml2_ls_post'),
    re_path(r'^metadata/$', views.metadata, name='saml2_metadata'),

    # this is needed for the tests
    re_path(r'^admin/', include(admin.site.urls)),
]
