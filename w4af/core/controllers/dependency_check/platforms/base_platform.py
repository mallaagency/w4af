"""
platform.py

Copyright 2014 Andres Riancho

This file is part of w4af, https://w4af.net/ .

w4af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w4af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w4af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""
from ..requirements import CORE
from ..external.retirejs import retirejs_is_installed


class Platform(object):
    """
    Simple base class for defining platforms/operating systems for dependency
    checks.
    """
    SYSTEM_PACKAGES = {CORE: []}

    @staticmethod
    def is_current_platform():
        raise NotImplementedError

    @staticmethod
    def os_package_is_installed(package_name):
        raise NotImplementedError

    @staticmethod
    def after_hook():
        pass

    @staticmethod
    def get_missing_external_commands():
        instructions = []

        for handler in Platform.EXTERNAL_COMMAND_HANDLERS:
            instructions.extend(handler.__func__())

        return instructions

    @staticmethod
    def retirejs_handler():
        if retirejs_is_installed():
            return []

        return ['npm install -g retire@3.0.6',
                'npm update -g retire']

    EXTERNAL_COMMAND_HANDLERS = [retirejs_handler]
