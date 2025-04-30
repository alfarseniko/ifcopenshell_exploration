import ifcopenshell as ios

model = ios.open('model.ifc')

entities = model.by_type('IfcBuildingElementProxy')

for entity in entities:
    print(entity.id())
    print(entity.GlobalId)
    print(entity.Name)
    print(entity.Description)
    print(entity.ObjectType)
    print('\n')
    print('\n')