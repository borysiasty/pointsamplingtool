#-----------------------------------------------------------
#
# Point Sampling Tool
#
# A QGIS plugin for collecting polygon attributes and raster values from multiple layers at specified sampling points
#
# Copyright (C) 2008-2012  Borys Jurgiel
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

def name():
    return 'Point sampling tool'

def description():
    return 'Samples polygon attributes and raster values from multiple layers at specified sampling points'

def version():
    return 'Version 0.3.8'

def qgisMinimumVersion():
    return '1.0'

def icon():
    return "pointSamplingToolIcon.png"

def authorName():
    return 'Borys Jurgiel'

def author():
    return auhorName()

def homepage():
    return 'http://hub.qgis.org/projects/pointsamplingtool'

def email():
    return 'qgis (at) borysjurgiel (dot) pl'

def classFactory(iface):
    from pointSamplingTool import pointSamplingTool
    return pointSamplingTool(iface)
