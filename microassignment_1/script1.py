import ifcopenshell as ios

model = ios.open('model.ifc')
spaceElement = model.by_guid('1wJoqPkIP4J8fINgm5A1mP')

for definition in spaceElement.IsDefinedBy:
    if definition.RelatingPropertyDefinition.Name == 'Qto_SpaceBaseQuantities':
        for quantity in definition.RelatingPropertyDefinition.Quantities:
            if quantity.Name == 'GrossFloorArea':
                print(quantity.AreaValue)

    


