#!/usr/bin/env python
# state file generated using paraview version 5.11.1
import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *


# create a new 'CSV Reader'
pegasusvtu = XMLUnstructuredGridReader(FileName=["../pegasus.vtu"])

# create a new 'Mask Points'
maskPoints1 = MaskPoints(Input=pegasusvtu)
maskPoints1.OnRatio = 50
maskPoints1.MaximumNumberofPoints = 8000
maskPoints1.GenerateVertices = 1


# create a new 'Calculator'
calculator1 = Calculator(Input=maskPoints1)
calculator1.ResultArrayName = 'X'
calculator1.Function = 'coordsX'

# create a new 'Calculator'
calculator2 = Calculator(Input=calculator1)
calculator2.ResultArrayName = 'Y'
calculator2.Function = 'coordsY'

# create a new 'Calculator'
calculator3 = Calculator(Input=calculator2)
calculator3.ResultArrayName = 'Z'
calculator3.Function = 'coordsZ'

# create a new 'Elevation'
elevation1 = Elevation(Input=calculator3)
elevation1.LowPoint = [-40.400081634521484, -75.79019165039062, -1167.939453125]
elevation1.HighPoint = [63.30849838256836, 60.25925064086914, -1068.4969482421875]

# create a new 'TTK DataSetToTable'
tTKDataSetToTable1 = TTKDataSetToTable(Input=elevation1)
tTKDataSetToTable1.DataAssociation = 'Point'

# create a new 'TTK TableDistanceMatrix'
tTKTableDistanceMatrix1 = TTKTableDistanceMatrix(Input=tTKDataSetToTable1)
tTKTableDistanceMatrix1.InputColumns = ['X', 'Y', 'Z']

# create a new 'TTK RipsComplex'
tTKRipsComplex1 = TTKRipsComplex(Input=tTKTableDistanceMatrix1)
tTKRipsComplex1.SelectFieldswithaRegexp = 1
tTKRipsComplex1.Regexp = 'Dist.*'
tTKRipsComplex1.OutputDimension = 1
tTKRipsComplex1.Diameterepsilon = 6.0
tTKRipsComplex1.XColumn = 'X'
tTKRipsComplex1.YColumn = 'Y'
tTKRipsComplex1.ZColumn = 'Z'

# create a new 'TTK Mapper'
tTKMapper1 = TTKMapper(registrationName='TTKMapper1', Input=tTKRipsComplex1)
tTKMapper1.ScalarField = ['POINTS', 'Elevation']
tTKMapper1.NumberofBuckets = 35
tTKMapper1.ReEmbedMapper = 1
tTKMapper1.SelectMatrixWithRegexp = 1
tTKMapper1.DistanceMatrixRegexp = 'Dist.*'
tTKMapper1.LowerDimension = '2D'

SaveData("OutputMapperPegasus.csv", tTKMapper1)
