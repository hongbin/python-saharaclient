# Copyright (c) 2013 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from savannaclient.api import base


class DataSources(base.Resource):
    resource_name = 'DataSource'


class DataSourceManager(base.ResourceManager):
    resource_class = DataSources

    def list(self):
        return self._list('/data-sources', "data_sources")

    def delete(self, data_source_id):
        return self._delete('/data-sources/%s' % data_source_id)

    def get(self, data_source_id):
        return self._get('/data-sources/%s' % data_source_id)

    def create(self, name, description, data_source_type, url, credentials):
        data = {
            'name': name,
            'description': description,
            'type': data_source_type,
            'url': url,
            'credentials': credentials
        }

        return self._create('/data-sources', data)
