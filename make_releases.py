# ##### BEGIN MIT LICENSE BLOCK #####
#
#    Copyright (c) 2020 Elie Michel
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# ##### END MIT LICENSE BLOCK #####

import os
from os.path import join as P
import shutil

#------------------------------------------------------------
# Config

addon_list = [
    "ImguiExample",
]

#------------------------------------------------------------
# Utils

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, directory):
        self.directory = os.path.expanduser(directory)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.directory)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def ensure_dir(directory):
    os.makedirs(directory, exist_ok=True)

def zip(directory, zipfile):
    """compresses a directory into a zip file"""
    print(f"Zipping {directory} into {zipfile}...")
    directory = os.path.realpath(directory)
    parent = os.path.dirname(directory)
    base = os.path.basename(directory)
    shutil.make_archive(zipfile, 'zip', parent, base)

def get_addon_version(addon_directory):
    """Extract the version of the addon from its init file"""
    with open(P(addon_directory, "__init__.py"), 'r') as f:
        text = f.read()
    bl_info = eval(text[text.find("{"):text.find("}")+1])
    return "{}.{}.{}".format(*bl_info["version"])

def this_scripts_directory():
    return os.path.dirname(os.path.realpath(__file__))

#------------------------------------------------------------
# Main

with cd(this_scripts_directory()):
    ensure_dir("releases")

    for addon in addon_list:
        version = get_addon_version(addon)
        zip(addon, P("releases", f"{addon}-v{version}"))

    print("Done.")
