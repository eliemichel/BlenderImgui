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

from bpy.types import VIEW3D_PT_gizmo_display

from . import operators as ops

# -------------------------------------------------------------------

def VIEW3D_MT_show_imgui_example_overlay(self, context):
    col = self.layout.column()
    col.label(text="Other")
    col.prop(context.scene, 'show_imgui_example_overlay')
    col.operator(ops.ImguiExample.bl_idname)

def register():
    VIEW3D_PT_gizmo_display.append(VIEW3D_MT_show_imgui_example_overlay)

def unregister():
    VIEW3D_PT_gizmo_display.remove(VIEW3D_MT_show_imgui_example_overlay)
