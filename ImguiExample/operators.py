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

import bpy
from bpy.types import Operator

from .blender_imgui import ImguiBasedOperator
import imgui

# -------------------------------------------------------------------

class ImguiExample(Operator,ImguiBasedOperator):
    """Example of modal operator using ImGui"""
    bl_idname = "object.imgui_example"
    bl_label = "Imgui Example"
    
    def draw(self, context):
        # This is where you can use any code from pyimgui's doc
        # see https://pyimgui.readthedocs.io/en/latest/
        imgui.begin("Your first window!", True)
        imgui.text("Hello world!")
        imgui.text("Another line!")
        imgui.text("And yet another")
        changed, self.color = imgui.color_edit3("Pick a color: Color", *self.color)
        changed, self.message = imgui.input_text_multiline(
            'Message:',
            self.message,
            2056
        )
        imgui.text_colored(self.message, *self.color)
        imgui.end()
    
    def invoke(self, context, event):
        self.color = (1.,.5,0.)
        self.message = "Type something here!"
        # Call init_imgui() at the beginning
        self.init_imgui(context)
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        context.area.tag_redraw()

        # Handle the event as you wish here, as in any modal operator
        if event.type in {'RIGHTMOUSE', 'ESC'}:
            # Call shutdown_imgui() any time you'll return {'CANCELLED'} or {'FINISHED'}
            self.shutdown_imgui()
            return {'CANCELLED'}

        # Don't forget to call parent's modal:
        self.modal_imgui(context, event)
        return {'RUNNING_MODAL'}

# -------------------------------------------------------------------

classes = (
    ImguiExample,
)

register, unregister = bpy.utils.register_classes_factory(classes)
