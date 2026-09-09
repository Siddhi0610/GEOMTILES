from shapely import wkb
from shapely.geometry import MultiPolygon, Polygon


WIDTH = 10
DEPTH = 10
FLOOR_HEIGHT = 3


def create_flat(z_start):
    z_end = z_start + FLOOR_HEIGHT

    bottom = [
        (0, 0, z_start),
        (WIDTH, 0, z_start),
        (WIDTH, DEPTH, z_start),
        (0, DEPTH, z_start),
        (0, 0, z_start),
    ]

    top = [
        (0, 0, z_end),
        (WIDTH, 0, z_end),
        (WIDTH, DEPTH, z_end),
        (0, DEPTH, z_end),
        (0, 0, z_end),
    ]

    faces = [
        Polygon(bottom),
        Polygon(top),

        Polygon([
            bottom[0],
            bottom[1],
            top[1],
            top[0],
            bottom[0],
        ]),

        Polygon([
            bottom[1],
            bottom[2],
            top[2],
            top[1],
            bottom[1],
        ]),

        Polygon([
            bottom[2],
            bottom[3],
            top[3],
            top[2],
            bottom[2],
        ]),

        Polygon([
            bottom[3],
            bottom[0],
            top[0],
            top[3],
            bottom[3],
        ]),
    ]

    return MultiPolygon(faces)


flats = {
    "flat_1": 0,
    "flat_2": 3,
    "flat_3": 6,
}


for name, z_start in flats.items():

    geometry = create_flat(z_start)

    output_path = f"data/{name}.wkb"

    with open(output_path, "wb") as f:
        f.write(
            wkb.dumps(
                geometry,
                output_dimension=3,
                flavor="iso",
            )
        )

    print(f"Created {output_path}")