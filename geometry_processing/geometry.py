import ifcopenshell as ios
import ifcopenshell.geom as geom
import ifcopenshell.util.shape as ios_shape

ifc_file = ios.open('model.ifc')
element  = ifc_file.by_type('IfcWall')[0]

settings = geom.settings()
shape = geom.create_shape(settings, element)

matrix = ios_shape.get_shape_matrix(shape)
verts = shape.geometry.verts
edges = shape.geometry.edges
faces = shape.geometry.faces

grouped_verts = ios_shape.get_vertices(shape.geometry)
grouped_edges = ios_shape.get_edges(shape.geometry)
grouped_faces = ios_shape.get_faces(shape.geometry)

print(grouped_faces)