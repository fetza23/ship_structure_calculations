import FreeCAD as App
import Part

distance = [0.0, 3.5, 7.0, 14.0, 21.0, 28.0, 35.0, 42.0, 49.0, 56.0, 63.0, 66.5, 70.0]
p0 = [0.0000, 0.0000, 0.000, 0.000, 0.000, 0.920, 2.560, 3.608]
p0_5 = [0.1808, 0.6360, 0.872, 1.080, 1.688, 3.416, 4.912, 5.808]
p1 = [0.6776, 1.7048, 2.264, 2.920, 3.904, 5.280, 6.352, 7.000]
p2 = [2.7112, 4.2808, 5.336, 6.248, 6.904, 7.368, 7.664, 7.896]
p3 = [5.0616, 6.5152, 7.400, 7.808, 7.920, 7.968, 8.000, 8.000]
p4 = [6.3592, 7.5152, 7.992, 8.000, 8.000, 8.000, 8.000, 8.000]
p5 = [6.4560, 7.5760, 8.000, 8.000, 8.000, 8.000, 8.000, 8.000]
p6 = [6.4560, 7.5760, 8.000, 8.000, 8.000, 8.000, 8.000, 8.000]
p7 = [6.3208, 7.4472, 7.952, 7.992, 7.992, 8.000, 8.000, 8.000]
p8 = [4.5192, 6.0608, 6.960, 7.288, 7.440, 7.544, 7.632, 7.696]
p9 = [1.5168, 3.0760, 4.032, 4.480, 4.680, 4.864, 5.112, 5.520]
p9_5 = [0.4328, 1.3640, 2.008, 2.208, 2.320, 2.432, 2.704, 3.224]
p10 = [0.0000, 0.0000, 0.000, 0.000, 0.000, 0.000, 0.200, 0.496]
postalar = [p0, p0_5, p1, p2, p3, p4, p5, p6, p7, p8, p9, p9_5, p10]
height = [0, 0.355, 1.1833333333333333, 2.3666666666666667, 3.5499999999999994, 4.733333333333333, 5.916666666666667,
          7.1]
App.newDocument()
App.activeDocument().addObject('PartDesign::Body', 'Body')
App.ActiveDocument.getObject('Body').Label = 'Body'

App.ActiveDocument.recompute()
yg = []
height_yg = []

for x, post in enumerate(postalar):
    App.activeDocument().addObject('Sketcher::SketchObject', 'Sketch' + str(x))
    sketch = App.activeDocument().getObject('Sketch' + str(x))
    sketch.Support = (App.activeDocument().getObject('XZ_Plane'), [''])
    sketch.MapMode = 'FlatFace'

    filtered_points = []
    height_subset = []

    for i in range(len(height)):
        if post[i] == 0 and not any(p == 0 for p in filtered_points):
            filtered_points.append(post[i])
        elif post[i] != 0:
            filtered_points.append(post[i])

        height_subset = height[-len(filtered_points):]

    yg.append(filtered_points)
    height_yg.append(height_subset)
    if not 0 in yg[x]:
        coord_origin = (0, 0, distance[x])

    for i in range(len(yg[x])):
        coord = (yg[x][i], height_yg[x][i], distance[x])
        sketch.addGeometry(Part.Point(App.Vector(coord)))
        if not 0 in yg[x]:
            coord_origin = (0, 0, distance[x])
            all_points = [App.Vector(coord_origin)] + [App.Vector(yg[x][i], height_yg[x][i], distance[x]) for i in
                                                       range(len(yg[x]))]
            sketch.addGeometry(Part.BSplineCurve(all_points))
        else:
            all_points = [App.Vector(yg[x][i], height_yg[x][i], distance[x]) for i in range(len(yg[x]))]
            sketch.addGeometry(Part.BSplineCurve(all_points))

    App.activeDocument().getObject('Sketch' + str(x)).AttachmentOffset = App.Placement(App.Vector(0, 0, distance[x]),
                                                                                       App.Rotation(App.Vector(0, 0, 1),
                                                                                                    0))

App.ActiveDocument.recompute()
