from shapely.geometry import Polygon, MultiPolygon
from shapely import wkb


def create_flat(z_min, z_max, filename):
    vertices = [
        (0, 0, z_min),
        (10, 0, z_min),
        (10, 10, z_min),
        (0, 10, z_min),

        (0, 0, z_max),
        (10, 0, z_max),
        (10, 10, z_max),
        (0, 10, z_max),
    ]

    bottom = Polygon([
        vertices[0],
        vertices[1],
        vertices[2],
        vertices[3],
        vertices[0]
    ])

    top = Polygon([
        vertices[4],
        vertices[5],
        vertices[6],
        vertices[7],
        vertices[4]
    ])

    front = Polygon([
        vertices[0],
        vertices[1],
        vertices[5],
        vertices[4],
        vertices[0]
    ])

    back = Polygon([
        vertices[3],
        vertices[2],
        vertices[6],
        vertices[7],
        vertices[3]
    ])

    left = Polygon([
        vertices[0],
        vertices[3],
        vertices[7],
        vertices[4],
        vertices[0]
    ])

    right = Polygon([
        vertices[1],
        vertices[2],
        vertices[6],
        vertices[5],
        vertices[1]
    ])

    building = MultiPolygon([
        bottom,
        top,
        front,
        back,
        left,
        right
    ])

    with open(filename, "wb") as f:
        f.write(
            wkb.dumps(
                building,
                output_dimension=3,
                flavor="iso"
            )
        )


create_flat(0, 3, "flat1/flat_1.wkb")
create_flat(3, 6, "flat2/flat_2.wkb")
create_flat(6, 9, "flat3/flat_3.wkb")

print("Created three independent flats.")