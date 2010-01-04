# Licensed to libcloud.org under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# libcloud.org licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from libcloud.types import Provider
from libcloud.providers import get_driver

GoGrid = get_driver(Provider.GOGRID)

driver = GoGrid('key','secret')

nodes = driver.list_nodes()
images = driver.list_images() 
sizes = driver.list_sizes()
ip = driver.get_first_ip()

print images
print nodes
print sizes
print ip

new_node = driver.create_node('newTestNode',images[0],sizes[0])

# grab the node named "test"
node = filter(lambda x: x.name == 'newTestNode', nodes)[0]

# reboot "test"
node.reboot()
