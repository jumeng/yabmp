# Copyright 2015 Cisco Systems, Inc.
# All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

""" message queue config """

import os

from oslo_config import cfg

CONF = cfg.CONF

rabbit_mq = [
    cfg.StrOpt('rabbit_url',
               default=os.environ.get('RABBITMQ_URL', 'amqp://guest:guest@localhost:5672/%2F'),
               help='The RabbitMQ connection url')
]
