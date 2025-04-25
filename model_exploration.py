import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element

model = ifcopenshell.open('./models/model.ifc')
walls = model.by_type('IfcWall')
wall = walls[0]
p_sets = ifcopenshell.util.element.get_psets(wall)
print(model.traverse(wall))