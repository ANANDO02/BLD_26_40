import ifcopenshell


# Open the BEFORE model
before_model = ifcopenshell.open(
    "models/26-09-D-STR.ifc"
)

# Open the AFTER model
after_model = ifcopenshell.open(
    "models/prøv den her ifc for kode.ifc"
)


print("Both models opened successfully!")
print()


# IFC element types to compare
types_to_compare = [
    "IfcWall",
    "IfcDoor",
    "IfcWindow",
    "IfcSlab",
    "IfcColumn",
    "IfcBeam"
]


# Compare the two models
for ifc_type in types_to_compare:

    before_elements = before_model.by_type(ifc_type)
    after_elements = after_model.by_type(ifc_type)

    # GlobalId is the unique IFC ID of each element
    before_ids = {element.GlobalId for element in before_elements}
    after_ids = {element.GlobalId for element in after_elements}

    # Find retained, removed and added elements
    retained = before_ids & after_ids
    removed = before_ids - after_ids
    added = after_ids - before_ids

    print("-----", ifc_type, "-----")
    print("Before:", len(before_elements))
    print("After:", len(after_elements))
    print("Retained:", len(retained))
    print("Removed:", len(removed))
    print("Added:", len(added))
    print()