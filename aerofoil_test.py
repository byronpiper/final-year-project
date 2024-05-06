
# Delete Objects
selection = Selection.Create(GetRootPart().GetChildren[IDocObject]()[-1])
result = Delete.Execute(selection)
# EndBlock

# Insert From File
importOptions = ImportOptions.Create()
DocumentInsert.Execute(r"C:\Users\SirHoneyBadger\Documents\Ansys\Workspaces\final-year-project\aerofoils.txt", importOptions, GetMaps("abbfc9e1"))
# EndBlock

# Simplify Object
result = FixSimplify.FixSpecific(Selection.Create(GetRootPart().Curves[0]))
# EndBlock

# Fill
selection = Selection.Create(GetRootPart().Curves[0])
secondarySelection = Selection.Empty()
options = FillOptions()
result = Fill.Execute(selection, secondarySelection, options, FillMode.ThreeD, None)
# EndBlock

# Set Sketch Plane
sectionPlane = Plane.PlaneXY
result = ViewHelper.SetSketchPlane(sectionPlane, None)
# EndBlock


# Sketch Line
start = Point2D.Create(M(-0.999537606596146), M(1.00505541389406E-16))
end = Point2D.Create(M(-0.999537606596146), M(5))
result = SketchLine.Create(start, end)

baseSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[0].GetChildren[ICurvePoint]()[0])
targetSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].GetChildren[IDatumLine]()[0])

result = Constraint.CreateCoincident(baseSel, targetSel)

baseSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[0])
targetSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].GetChildren[IDatumLine]()[0])

result = Constraint.CreatePerpendicular(baseSel, targetSel)
# EndBlock

# Sketch Point
point = Point2D.Create(M(-0.999537606596146), M(5))
result = SketchPoint.Create(point)
# EndBlock

# Delete Selection
selection = Selection.Create(GetRootPart().DatumPlanes[0].Curves[0])
result = Delete.Execute(selection)
# EndBlock

# Sketch Line
start = Point2D.Create(M(-0.999537606596146), M(5))
end = Point2D.Create(M(-5.99953760659615), M(5))
result = SketchLine.Create(start, end)
# EndBlock

# Sketch Line
start = Point2D.Create(M(-5.99953760659615), M(5))
end = Point2D.Create(M(-5.99953760659615), M(-5))
result = SketchLine.Create(start, end)

baseSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[2].GetChildren[ICurvePoint]()[0])
targetSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[1].GetChildren[ICurvePoint]()[1])

result = Constraint.CreateCoincident(baseSel, targetSel)

baseSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[2])
targetSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[1])

result = Constraint.CreatePerpendicular(baseSel, targetSel)
# EndBlock

# Sketch Line
start = Point2D.Create(M(-5.99953760659615), M(-5))
end = Point2D.Create(M(9.00046239340385), M(-5.00000000000001))
result = SketchLine.Create(start, end)

baseSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[3])
targetSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].GetChildren[IDatumLine]()[1])

result = Constraint.CreatePerpendicular(baseSel, targetSel)

baseSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[3].GetChildren[ICurvePoint]()[0])
targetSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[2].GetChildren[ICurvePoint]()[1])

result = Constraint.CreateCoincident(baseSel, targetSel)

baseSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[3])
targetSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[2])

result = Constraint.CreatePerpendicular(baseSel, targetSel)

baseSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[3])
targetSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[1])

result = Constraint.CreateParallel(baseSel, targetSel)
# EndBlock

# Sketch Line
start = Point2D.Create(M(9.00046239340385), M(-5.00000000000001))
end = Point2D.Create(M(9.00046239340386), M(4.99999999999999))
result = SketchLine.Create(start, end)

baseSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[4])
targetSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].GetChildren[IDatumLine]()[0])

result = Constraint.CreatePerpendicular(baseSel, targetSel)

baseSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[4].GetChildren[ICurvePoint]()[0])
targetSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[3].GetChildren[ICurvePoint]()[1])

result = Constraint.CreateCoincident(baseSel, targetSel)

baseSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[4])
targetSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[3])

result = Constraint.CreatePerpendicular(baseSel, targetSel)

curveSelList = Selection.Create(GetRootPart().DatumPlanes[0].Curves[4])
result = Constraint.CreateVertical(curveSelList)
# EndBlock

# Sketch Line
start = Point2D.Create(M(9.00046239340386), M(4.99999999999999))
end = Point2D.Create(M(-0.999537606596146), M(5))
result = SketchLine.Create(start, end)

baseSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[5].GetChildren[ICurvePoint]()[1])
targetSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[1].GetChildren[ICurvePoint]()[0])

result = Constraint.CreateCoincident(baseSel, targetSel)

baseSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[5])
targetSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[1])

result = Constraint.CreateParallel(baseSel, targetSel)

baseSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[5])
targetSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].GetChildren[IDatumLine]()[1])

result = Constraint.CreatePerpendicular(baseSel, targetSel)

baseSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[5].GetChildren[ICurvePoint]()[0])
targetSel = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[4].GetChildren[ICurvePoint]()[1])

result = Constraint.CreateCoincident(baseSel, targetSel)
# EndBlock

# Fill
selection = Selection.Create([GetRootPart().DatumPlanes[0].Curves[5],
	GetRootPart().DatumPlanes[0].Curves[1],
	GetRootPart().DatumPlanes[0].Curves[2],
	GetRootPart().DatumPlanes[0].Curves[3],
	GetRootPart().DatumPlanes[0].Curves[4]])
secondarySelection = Selection.Empty()
options = FillOptions()
result = Fill.Execute(selection, secondarySelection, options, FillMode.Layout, None)
# EndBlock

# Fill
selection = Selection.Create([GetRootPart().DatumPlanes[0].Curves[5],
	GetRootPart().DatumPlanes[0].Curves[1],
	GetRootPart().DatumPlanes[0].Curves[2],
	GetRootPart().DatumPlanes[0].Curves[3],
	GetRootPart().DatumPlanes[0].Curves[4],
	GetRootPart().DatumPlanes[0].Curves[6]])
secondarySelection = Selection.Empty()
options = FillOptions()
result = Fill.Execute(selection, secondarySelection, options, FillMode.Layout, None)
# EndBlock

# Solidify Sketch
mode = InteractionMode.Solid
result = ViewHelper.SetViewMode(mode, None)
# EndBlock

# Delete Selection
selection = FaceSelection.Create(GetRootPart().Bodies[0].Faces[0])
result = Delete.Execute(selection)
# EndBlock

# Delete Selection
selection = FaceSelection.Create(GetRootPart().Bodies[0].Faces[0])
result = Delete.Execute(selection)
# EndBlock

# Delete Selection
selection = FaceSelection.Create(GetRootPart().Bodies[0].Faces[0])
result = Delete.Execute(selection)
# EndBlock

# Delete Selection
selection = FaceSelection.Create(GetRootPart().Bodies[1].Faces[0])
result = Delete.Execute(selection)
# EndBlock

# Extrude 1 Face
selection = FaceSelection.Create(GetRootPart().Bodies[0].Faces[0])
options = ExtrudeFaceOptions()
options.ExtrudeType = ExtrudeType.Add
result = ExtrudeFaces.Execute(selection, M(0.01), options)
# EndBlock

# Create Named Selection Group
primarySelection = FaceSelection.Create([GetRootPart().Bodies[0].Faces[6],
	GetRootPart().Bodies[0].Faces[5],
	GetRootPart().Bodies[0].Faces[3]])
secondarySelection = Selection.Empty()
result = NamedSelection.Create(primarySelection, secondarySelection, "Inlet")
# EndBlock

# Create Named Selection Group
primarySelection = FaceSelection.Create(GetRootPart().Bodies[0].Faces[4])
secondarySelection = Selection.Empty()
result = NamedSelection.Create(primarySelection, secondarySelection, "Outlet")
# EndBlock

# Create Named Selection Group
primarySelection = BodySelection.Create(GetRootPart().Bodies[0])
secondarySelection = Selection.Empty()
result = NamedSelection.Create(primarySelection, secondarySelection, "Freeflow")
# EndBlock

# Save File
options = ExportOptions.Create()
DocumentSave.Execute(r"C:\Users\SirHoneyBadger\Documents\Ansys\Workspaces\final-year-project\aerofoil.scdocx", options)
# EndBlock
