#-----------------------------------------------------------
# 
# Point Sampling Tool
#
# A QGIS plugin for collecting polygon attributes and raster values from multiple layers at specified sampling points
#
# Copyright (C) 2008-2011  Borys Jurgiel
# based on Carson Farmer's PointsInPoly plugin, Copyright (C) 2008 Carson Farmer
#
#-----------------------------------------------------------
# 
# licensed under the terms of GNU GPL 2
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# 
#---------------------------------------------------------------------

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

import resources
import doPointSamplingTool

class pointSamplingTool:

 def __init__(self, iface):
  self.iface = iface


 def initGui(self):
  # create action 
  self.action = QAction(QIcon(":/plugins/pointSamplingTool/pointSamplingToolIcon.png"), "Point sampling tool", self.iface.mainWindow())
  self.action.setWhatsThis("Collects polygon attributes and raster values from multiple layers at specified sampling points")
  QObject.connect(self.action, SIGNAL("triggered()"), self.run)
  # add toolbar button and menu item
  self.iface.addToolBarIcon(self.action)
  self.iface.addPluginToMenu("&Analyses", self.action)


 def unload(self):
  # remove the plugin menu item and icon
  self.iface.removePluginMenu("&Analyses",self.action)
  self.iface.removeToolBarIcon(self.action)


 def run(self):
  # create and show a configuration dialog or something similar
  dialoga = doPointSamplingTool.Dialog(self.iface)
  dialoga.exec_()
