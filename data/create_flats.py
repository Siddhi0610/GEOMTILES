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
create_flat(12, 15, "flat4/flat_4.wkb")
create_flat(16, 19, "flat5/flat_5.wkb")
create_flat(20, 23, "flat6/flat_6.wkb")
create_flat(24, 27, "flat7/flat_7.wkb")
create_flat(28, 31, "flat8/flat_8.wkb")
create_flat(32, 35, "flat9/flat_9.wkb")
create_flat(36, 39, "flat10/flat_10.wkb")
print("Created ten independent flats.")