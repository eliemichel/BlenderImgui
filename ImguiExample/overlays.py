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

from .blender_imgui import BlenderImguiOverlay, register_overlay, unregister_overlay
import imgui

# -------------------------------------------------------------------

class ImguiExampleOverlay(BlenderImguiOverlay):
    # Make sure this does not conflict with other addons
    bl_idname = "imgui_example_overlay"

    def draw(self, context):
        if not context.scene.show_imgui_example_overlay:
            return
        # This is where you can use any code from pyimgui's doc
        # see https://pyimgui.readthedocs.io/en/latest/

        # recommended flags for overlay windows (since they don't
        # receive user input events):
        flags = (
            imgui.WINDOW_NO_RESIZE
            | imgui.WINDOW_NO_MOVE
            | imgui.WINDOW_NO_COLLAPSE
            | imgui.WINDOW_NO_TITLE_BAR
            | imgui.WINDOW_ALWAYS_AUTO_RESIZE
        )
        imgui.begin("", closable=False, flags=flags)
        imgui.text("An ImGui Overlay!")
        imgui.text("Overlays cannot be interacted with.")
        imgui.end()

# -------------------------------------------------------------------

def register():
    register_overlay(ImguiExampleOverlay)
    
def unregister():
    unregister_overlay(ImguiExampleOverlay)
