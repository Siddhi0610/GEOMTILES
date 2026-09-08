from shapely import wkb
from shapely.geometry import MultiPolygon, Polygon

width = 10
depth = 10
height = 5

bottom = [
    (0, 0, 0),
    (width, 0, 0),
    (width, depth, 0),
    (0, depth, 0),
    (0, 0, 0)
]

top = [
    (0, 0, height),
    (width, 0, height),
    (width, depth, height),
    (0, depth, height),
    (0, 0, height)
]

faces = [
    Polygon(bottom),
    Polygon(top),
    Polygon([bottom[0], bottom[1], top[1], top[0], bottom[0]]),
    Polygon([bottom[1], bottom[2], top[2], top[1], bottom[1]]),
    Polygon([bottom[2], bottom[3], top[3], top[2], bottom[2]]),
    Polygon([bottom[3], bottom[0], top[0], top[3], bottom[3]])
]

building = MultiPolygon(faces)

with open("data/building.wkb", "wb") as f:
    f.write(wkb.dumps(building, output_dimension=3,  flavor="iso"))

print("Created data/building.wkb")
print(f"Number of faces: {len(faces)}")