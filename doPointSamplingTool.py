# -*- coding: utf-8 -*-

# ***************************************************************************
# Point Sampling Tool
#
# A QGIS plugin for collecting polygon attributes and raster values
# from multiple layers at specified sampling points
#
# Copyright (C) 2008 Borys Jurgiel
# based on Carson Farmer's PointsInPoly plugin, Copyright (C) 2008 Carson Farmer
#
# ***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# ***************************************************************************

import os
from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

Ui_Dialog = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'pointSamplingToolUi.ui'))[0]

class Dialog(QDialog, Ui_Dialog):

 sampItems = {}  # {name1 : [layer1, [field_src,field_dsn,Active?], [field_src,field_dsn,Active?], ...] , name2 : [layer2, ...] }
 polyItems = {}  # {name1 : [layer1, [field_src,field_dsn,Active?], [field_src,field_dsn,Active?], ...] , name2 : [layer2, ...] }
 rastItems = {}  # {name1 : [layer1, [band_name,field_dsn,Active?], [band_name,field_dsn,Active?], ...] , name2 : [layer2, ...] }
 fields = []     # [[type,layer,field],[type,layer,field],[type,layer,field]...] list of adresses of output fields

 def __init__(self, iface):
  QDialog.__init__(self)
  self.iface = iface
  self.setupUi(self)
  self.outButton.clicked.connect(self.outFile)
  self.inSample.currentIndexChanged.connect(self.updateFieldsList)
  self.inData.itemSelectionChanged.connect(self.updateFieldsTable)
  self.fieldsTable.cellChanged.connect(self.fieldNameChanged)
  self.addToToc.setCheckState(Qt.Checked)
  mapCanvas = self.iface.mapCanvas()
  # init dictionaries of items:
  self.sampItems = {}
  self.polyItems = {}
  self.rastItems = {}
  for i in range(mapCanvas.layerCount()):
   layer = mapCanvas.layer(i)
   if ( layer.type() == layer.VectorLayer ) and ( layer.geometryType() == QGis.Point ):
    # read point layers
    provider = layer.dataProvider()
    fields = provider.fields()
    theItem = [layer]
    for j in fields:
     theItem += [[unicode(j.name()), unicode(j.name()), False]]
    self.sampItems[unicode(layer.name())] = theItem
    self.inSample.addItem(layer.name())
   elif ( layer.type() == layer.VectorLayer ) and ( layer.geometryType() == QGis.Polygon ):
    # read polygon layers
    provider = layer.dataProvider()
    fields = provider.fields()
    theItem = [layer]
    for j in fields:
     theItem += [[unicode(j.name()), unicode(j.name()), False]]
    self.polyItems[unicode(layer.name())] = theItem
   elif layer.type() == layer.RasterLayer:
    # read raster layers
    theItem = [layer]
    for j in range(layer.bandCount()):
     if layer.bandCount() == 1:
      name1 = layer.bandName(j+1)
      name2 = layer.name()[:10]
     else:
      name1 = layer.bandName(j+1)
      name2 = layer.name()[:8] + "_" + unicode(j+1)
     theItem += [[name1, name2, False]]
    self.rastItems[unicode(layer.name())] = theItem
  self.updateFieldsList()


 def updateFieldsList(self):
  self.inData.clear()
  if not self.inSample.count(): return
  i = self.inSample.currentText()
  for j in range(1, len(self.sampItems[i])):
    #clear previously enabled fields (as they aren't selected in the widget)
    self.sampItems[i][j][2] = False
    self.inData.addItem(self.sampItems[i][0].name() + " : " + self.sampItems[i][j][0] + " (source point)")
#NOT YET FINISHED - to be switched to tree rather
#  self.inData.addItem(str(self.sampItems[i][0].name()) + " (X coordinate)")
#  self.inData.addItem(str(self.sampItems[i][0].name()) + " (Y coordinate)")

  for i in self.polyItems:
   for j in range(1, len(self.polyItems[i])):
    self.inData.addItem(unicode(self.polyItems[i][0].name()) + " : " + unicode(self.polyItems[i][j][0]) + " (polygon)")
  for i in self.rastItems:
   for j in range(1, len(self.rastItems[i])):
    self.inData.addItem(unicode(self.rastItems[i][0].name()) + " : "+ unicode(self.rastItems[i][j][0]) + " (raster)")
  self.updateFieldsTable()
  self.repaint()




 def updateFieldsTable(self): # called after selection changing
  # mark selected point items
  n=0
  i = self.inSample.currentText()
  for j in range(1, len(self.sampItems[i])):
    if self.inData.isItemSelected(self.inData.item(n)):
      self.sampItems[i][j][2] = True
    else:
      self.sampItems[i][j][2] = False
    n += 1
  # mark selected polygon items
  for i in self.polyItems:
   for j in range(1, len(self.polyItems[i])):
    if self.inData.isItemSelected(self.inData.item(n)):
     self.polyItems[i][j][2] = True
    else:
     self.polyItems[i][j][2] = False
    n += 1
  # mark selected raster items (don't zero n; it's one list)
  for i in self.rastItems:
   for j in range(1, len(self.rastItems[i])):
    if self.inData.isItemSelected(self.inData.item(n)):
     self.rastItems[i][j][2] = True
    else:
     self.rastItems[i][j][2] = False
    n += 1
  # fill the fieldsTable with point, then polygon and then raster items:
  self.fields = []
  n = 0
  self.fieldsTable.setRowCount(0)
  i = self.inSample.currentText()
  for j in range(1, len(self.sampItems[i])):
   if self.sampItems[i][j][2]:
    self.fields += [["point",i,j]]
    self.fieldsTable.setRowCount(n+1)
    cell = QTableWidgetItem(unicode(self.sampItems[i][0].name()) + " : " + unicode(self.sampItems[i][j][0]))
    cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
    self.fieldsTable.setItem(n,0,cell)
    self.fieldsTable.setItem(n,1,QTableWidgetItem(unicode(self.sampItems[i][j][1])))
    n += 1
  for i in self.polyItems:
   for j in range(1, len(self.polyItems[i])):
    if self.polyItems[i][j][2]:
     self.fields += [["poly",i,j]]
     self.fieldsTable.setRowCount(n+1)
     cell = QTableWidgetItem(unicode(self.polyItems[i][0].name()) + " : " + unicode(self.polyItems[i][j][0]))
     cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
     self.fieldsTable.setItem(n,0,cell)
     self.fieldsTable.setItem(n,1,QTableWidgetItem(unicode(self.polyItems[i][j][1])))
     n += 1
  for i in self.rastItems:
   for j in range(1, len(self.rastItems[i])):
    if self.rastItems[i][j][2]:
     self.fields += [["rast",i,j]]
     self.fieldsTable.setRowCount(n+1)
     cell = QTableWidgetItem(unicode(self.rastItems[i][0].name()) + " : " + unicode(self.rastItems[i][j][0]))
     cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
     self.fieldsTable.setItem(n,0,cell)
     self.fieldsTable.setItem(n,1,QTableWidgetItem(unicode(self.rastItems[i][j][1])))
     n += 1
  self.fieldsTable.resizeColumnsToContents()



 def fieldNameChanged(self, n): # called when any cell of the fieldsTable was modyfied
  # exit when false alarm
  if len(self.fields) == 0: return 0
  if self.fieldsTable.rowCount() == 0: return 0
  updatedItem = self.fieldsTable.item(n,1)
  if updatedItem == None: return 0
  # update items dictionaries
  updatedText = unicode(updatedItem.text())
  if self.fields[n][0] == "point":
   self.sampItems[self.fields[n][1]][self.fields[n][2]][1] = updatedText[:10]
  elif self.fields[n][0] == "poly":
   self.polyItems[self.fields[n][1]][self.fields[n][2]][1] = updatedText[:10]
  else:
   self.rastItems[self.fields[n][1]][self.fields[n][2]][1] = updatedText[:10]
  # cut to 10 characters if exceed
  if len(updatedText) > 10:
   self.updateFieldsTable()
   QMessageBox.information(self, "Point Sampling Tool", "Name length can't exceed 10 chars, so it has been truncated.")
   # This message box may to make some confusion, if user press OK while "too long name" is still under edition.
   # In this case, the message box pops up (correctly) and then the OK button becomes pressed, but the self.accept method is not called.
   # This pressed button with no action may to look like a hang up.
   # I've no idea either
   #  how to pull this button up, or
   #  how to forse execution the self.accept method, or
   #  how to don't allow user to exceed 10 chars limit in QTableWidget cell. (THIS OPTION WOULD BE THE BEST!)
  self.fieldsTable.resizeColumnsToContents()



 def outFile(self): # by Carson Farmer 2008
  # display file dialog for output shapefile
  self.outShape.clear()
  fileDialog = QFileDialog()
  fileDialog.setConfirmOverwrite(False)
  outName = fileDialog.getSaveFileName(self, "Output Shapefile",".", "Shapefiles (*.shp)")
  outPath = QFileInfo(outName).absoluteFilePath()
  if not outPath.upper().endswith(".SHP"):
   outPath = outPath + ".shp"
  if outName:
   self.outShape.clear()
   self.outShape.insert(outPath)



 def accept(self): # Called when "OK" button pressed (based on the Carson Farmer's PointsInPoly Plugin, 2008)
  # check if all fields are filled up
  self.statusLabel.setText("Check input values, please!")
  nothingSelected = True
  for i in self.polyItems:
   for j in range(1, len(self.polyItems[i])):
    if self.polyItems[i][j][2]:
     nothingSelected = False
  for i in self.rastItems:
   for j in range(1, len(self.rastItems[i])):
    if self.rastItems[i][j][2]:
     nothingSelected = False

  if self.inSample.currentText() == "":
   self.tabWidget.setCurrentIndex(0)
   QMessageBox.information(self, "Point Sampling Tool", "Please select vector layer containing the sampling points")
   return
  if nothingSelected:
   self.tabWidget.setCurrentIndex(0)
   QMessageBox.information(self, "Point Sampling Tool", "Please select at least one polygon attribute or raster band")
   return
  if self.outShape.text() == "":
   self.tabWidget.setCurrentIndex(0)
   QMessageBox.information(self, "Point Sampling Tool", "Please specify output shapefile name")
   return
  # check if destination field names are unique
  if not self.testFieldsNames(self.fields):
   self.updateFieldsTable()
   self.tabWidget.setCurrentIndex(1)
   QMessageBox.warning(self, "Point Sampling Tool", "At least two field names are the same!\nPlease type unique names.")
   return

  # Check if there a CRS mismatch
  pointLayerSrid = self.sampItems.values()[0][0].crs().postgisSrid()
  msg = u'''<html>All layers must have the same coordinate refere system. The <b>%s</b> layer seems to have different CRS id (<b>%d</b>)
            than the point layer (<b>%d</b>). If they are two different CRSes, you need to reproject one of the layers first,
            otherwise results will be wrong.<br/>
            However, if you are sure both CRSes are the same, and they are just improperly recognized, you can safely continue.
            Do you want to continue?</html>'''
  for i in self.polyItems:
   for j in range(1, len(self.polyItems[i])):
    if self.polyItems[i][j][2]:
     layerSrid = self.polyItems[i][0].crs().postgisSrid()
     if layerSrid != pointLayerSrid:
      if QMessageBox.question(self, "Point Sampling Tool: layer CRS mismatch!", msg % (i, layerSrid, pointLayerSrid), QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
       return
  for i in self.rastItems:
   for j in range(1, len(self.rastItems[i])):
    if self.rastItems[i][j][2]:
     layerSrid = self.rastItems[i][0].crs().postgisSrid()
     if layerSrid != pointLayerSrid:
      if QMessageBox.question(self, "Point Sampling Tool: layer CRS mismatch!", msg % (i, layerSrid, pointLayerSrid), QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
       return

  if True:
   # all tests passed! Let's go on
   self.statusLabel.setText("Processing the output file name...")
   self.repaint()
   outPath = self.outShape.text()
   outPath = outPath.replace("\\","/")
   outName = QFileInfo(outPath).fileName()
   if outName.upper().endswith(".SHP"):
    outName = outName[:-4]
   else:
    outPath = outPath + ".shp" # When only layer name is given, create it in current folder instead of in individual folders.
   oldFile = QFile(outPath)
   if oldFile.exists():
    QMessageBox.warning(self, "Point Sampling Tool", "Cannot overwrite existing shapefile.")
    # return to filling the input fields
    self.outShape.clear()
    self.statusLabel.setText("Fill up the input fields, please.")
    self.repaint()
   else:
    self.statusLabel.setText("Processing...")
    self.repaint()
    # execute main function
    self.sampling(outPath)
    self.outShape.clear()
    # add to the TOC if desired and possible ;)
    if self.addToToc.checkState() == Qt.Checked:
     self.vlayer = QgsVectorLayer(outPath, unicode(outName), "ogr")
     if self.vlayer.isValid():
      if hasattr( QgsMapLayerRegistry.instance(), 'addMapLayers' ):
            QgsMapLayerRegistry.instance().addMapLayers([self.vlayer])
      else:
            QgsMapLayerRegistry.instance().addMapLayer(self.vlayer)  # QPI <= 1.8
      self.statusLabel.setText("OK. The new layer has been added to the TOC.")
     else:
      self.statusLabel.setText("Error loading the created layer")
      QMessageBox.warning(self, "Point Sampling Tool", "The new layer seems to be created, but is invalid.\nIt won't be loaded.")



 def sampling(self, outPath): # main process
    # open sampling points layer
    pointLayer = self.sampItems[unicode(self.inSample.currentText())][0]
    pointProvider = pointLayer.dataProvider()
    allAttrs = pointProvider.attributeIndexes()
    sRs = pointProvider.crs()
    # create destination layer: first create list of selected fields
    fieldList = QgsFields()
    for i in range(len(self.fields)):
        if self.fields[i][0] == "point": #copying fields from source layer
            field = pointProvider.fields()[pointProvider.fieldNameIndex(self.sampItems[self.fields[i][1]][self.fields[i][2]][0])]
            field.setName(self.sampItems[self.fields[i][1]][self.fields[i][2]][1])
        elif self.fields[i][0] == "poly": #copying fields from polygon layers
            polyLayer = self.polyItems[self.fields[i][1]][0]
            polyProvider = polyLayer.dataProvider()
            field = polyProvider.fields()[polyProvider.fieldNameIndex(self.polyItems[self.fields[i][1]][self.fields[i][2]][0])]
            field.setName(self.polyItems[self.fields[i][1]][self.fields[i][2]][1])
        else: #creating fields for raster layers
            field = QgsField(self.rastItems[self.fields[i][1]][self.fields[i][2]][1], QVariant.Double, "real", 20, 5, "")
            ##### Better data type fit will be implemented in next versions
        fieldList.append(field)
    # create destination layer
    writer = QgsVectorFileWriter(outPath, "UTF-8", fieldList, pointProvider.geometryType(), sRs)
    self.statusLabel.setText("Writing data to the new layer...")
    self.repaint()
    # process point after point...
    pointFeat = QgsFeature()
    np = 0
    snp = pointProvider.featureCount()
    for pointFeat in pointProvider.getFeatures():
        np += 1
        if snp<100 or ( snp<5000 and ( np // 10.0 == np / 10.0 ) ) or ( np // 100.0 == np / 100.0 ): # display each or every 10th or every 100th point:
            self.statusLabel.setText("Processing point %s of %s" % (np, snp))
            self.repaint()
        # convert multipoint[0] to point
        pointGeom = pointFeat.geometry()
        if pointGeom.wkbType() == QGis.WKBMultiPoint:
            pointPoint = pointGeom.asMultiPoint()[0]
        else:
            pointPoint = pointGeom.asPoint()
        outFeat = QgsFeature()
        outFeat.setGeometry(pointGeom)
        # ...and next loop inside: field after field
        bBox = QgsRectangle(pointPoint.x()-0.001,pointPoint.y()-0.001,pointPoint.x()+0.001,pointPoint.y()+0.001) # reuseable rectangle buffer around the point feature
        previousPolyLayer = None  # reuse previous feature if it's still the same layer
        previousPolyFeat = None   # reuse previous feature if it's still the same layer
        previousRastLayer = None  # reuse previous raster multichannel sample if it's still the same layer
        previousRastSample = None # reuse previous raster multichannel sample if it's still the same layer
        attrs = []
        for i in range(len(self.fields)):
            field = self.fields[i]
            if field[0] == "point":
                attr = pointFeat.attributes()[pointProvider.fieldNameIndex(self.sampItems[field[1]][field[2]][0])]
                attrs += [attr]
            elif field[0] == "poly":
                polyLayer = self.polyItems[field[1]][0]
                polyProvider = polyLayer.dataProvider()
                if polyLayer == previousPolyLayer:
                    polyFeat = previousPolyFeat
                else:
                    polyFeat = None
                    pointGeom = QgsGeometry().fromPoint(pointPoint)
                    for iFeat in polyProvider.getFeatures(QgsFeatureRequest().setFilterRect(bBox)):
                        if pointGeom.intersects(iFeat.geometry()):
                            polyFeat = iFeat
                if polyFeat:
                    attr = polyFeat.attributes()[polyProvider.fieldNameIndex(self.polyItems[field[1]][field[2]][0])]
                else:
                    attr = None
                attrs += [attr] #only last one if more polygons overlaps!! This way we avoid attribute list overflow
                previousPolyLayer = polyLayer
                previousPolyFeat = polyFeat
            else: # field source is raster
                rastLayer = self.rastItems[field[1]][0]
                if rastLayer == previousRastLayer:
                    rastSample = previousRastSample
                else:
                    rastSample = rastLayer.dataProvider().identify(pointPoint, QgsRaster.IdentifyFormatValue).results()
                try:
                    #bandName = self.rastItems[field[1]][field[2]][0] #depreciated
                    bandNo = field[2]
                    attr = float(rastSample[bandNo]) ##### !! float() - I HAVE TO IMPLEMENT RASTER TYPE HANDLING!!!!
                except: # point is out of raster extent
                    attr = None
                attrs += [attr]
                previousRastLayer = rastLayer
                previousRastSample = rastSample
        outFeat.initAttributes(len(attrs))
        outFeat.setAttributes(attrs)
        writer.addFeature(outFeat)

    del writer
    self.statusLabel.setText("The new layer has been created.")



 def testFieldsNames(self, fields): #tests uniquity of field names
  ok = True
  if len(fields) > 1:
   for field1 in fields:
    for field2 in fields:
     if field1[0] == "point": name1 = self.sampItems[field1[1]][field1[2]][1]
     elif field1[0] == "poly": name1 = self.polyItems[field1[1]][field1[2]][1]
     else: name1 = self.rastItems[field1[1]][field1[2]][1]
     if field2[0] == "point": name2 = self.sampItems[field2[1]][field2[2]][1]
     elif field2[0] == "poly": name2 = self.polyItems[field2[1]][field2[2]][1]
     else: name2 = self.rastItems[field2[1]][field2[2]][1]
     if (name1 == name2) and (field1 != field2):
      ok = False
  return ok

