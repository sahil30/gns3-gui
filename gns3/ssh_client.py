# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gns3.http_client import HTTPClient
from gns3.tunnel.endpoint import Endpoint
import paramiko


class SSHClient(HTTPClient):
    """
    SSH client.

    It's create an SSH tunnel and run HTTP query inside the tunnel

    :param url: URL to connect to the server
    :param network_manager: A QT network manager
    """

    def __init__(self, url, network_manager):
        url = url.replace("ssh://", "http://")
        super().__init__(url, network_manager)

        self.transport = paramiko.Transport((self.host(), self.port(), ))
        self.transport.set_keepalive(30)
        with open("/Users/noplay/code/gns3/gns3-vagrant/.vagrant/machines/default/virtualbox/private_key") as f:
            self.transport.connect(username="vagrant", pkey=paramiko.RSAKey.from_private_key(f))
        self._endpoint = Endpoint(("127.0.0.1", 2224), ("127.0.0.1", 8003), self.transport)
        self._endpoint.enable()
        self._http_host = "127.0.0.1"
        self._http_port = 2224

    def protocol(self):
        return "ssh"

