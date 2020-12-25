# ##### BEGIN GPL LICENSE BLOCK #####
#
#    Copyright (c) 2020 Elie Michel
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "ImGui Examples",
    "author": "Élie Michel <elie.michel@exppad.com>",
    "version": (1, 0, 0),
    "blender": (2, 90, 0),
    "location": "View3D > Overlays",
    "description": "Examples of how to use ImGui in Blender",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "https://github.com/eliemichel/BlenderImgui",
    "support": "COMMUNITY",
    "category": "3D view",
}

# -------------------------------------------------------------------

import bpy

from . import properties
from . import operators
from . import panels
from . import overlays

submodules = (
    properties,
    operators,
    panels,
    overlays,
)

def register():
    for m in submodules:
        m.register()

def unregister():
    for m in submodules[::-1]:
        m.unregister()

loaded = True
