from shapely import wkb
from shapely.geometry import Polygon

# Building dimensions
width = 10
depth = 10
height = 5

# Bottom face
bottom = [
    (0, 0, 0),
    (width, 0, 0),
    (width, depth, 0),
    (0, depth, 0),
    (0, 0, 0)
]

# Top face
top = [
    (0, 0, height),
    (width, 0, height),
    (width, depth, height),
    (0, depth, height),
    (0, 0, height)
]

# For now, create the building as individual polygon faces.
faces = [
    Polygon(bottom),
    Polygon(top),
    Polygon([bottom[0], bottom[1], top[1], top[0], bottom[0]]),
    Polygon([bottom[1], bottom[2], top[2], top[1], bottom[1]]),
    Polygon([bottom[2], bottom[3], top[3], top[2], bottom[2]]),
    Polygon([bottom[3], bottom[0], top[0], top[3], bottom[3]])
]

# Save each face as a WKB file
for i, face in enumerate(faces):
    output = f"data/building_{i}.wkb"

    with open(output, "wb") as f:
        f.write(wkb.dumps(face))

    print(f"Created {output}")

print("Building geometry created successfully.")