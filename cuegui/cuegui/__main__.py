#!/usr/bin/env python

#  Copyright Contributors to the OpenCue Project
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


"""Entrypoint for the CueGUI application."""


from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import sys

import cuegui.Main


def main():
    """Entrypoint for the CueGUI/CueCommmander application."""
    cuegui.Main.cuecommander(sys.argv)


def cuetopia():
    """Entrypoint for the Cuetopia application."""
    cuegui.Main.cuetopia(sys.argv)


if __name__ == '__main__':
    main()
