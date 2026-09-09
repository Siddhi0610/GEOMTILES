import struct
import json
from pygltflib import GLTF2


def color_b3dm(input_file, output_file, color):
    with open(input_file, "rb") as f:
        data = f.read()

    # Read B3DM header
    magic = data[0:4]
    version = struct.unpack("<I", data[4:8])[0]
    tile_byte_length = struct.unpack("<I", data[8:12])[0]

    feature_json_length = struct.unpack("<I", data[12:16])[0]
    feature_bin_length = struct.unpack("<I", data[16:20])[0]
    batch_json_length = struct.unpack("<I", data[20:24])[0]
    batch_bin_length = struct.unpack("<I", data[24:28])[0]

    # Find embedded GLB
    glb_start = (
        28
        + feature_json_length
        + feature_bin_length
        + batch_json_length
        + batch_bin_length
    )

    glb_data = data[glb_start:]

    # Save temporary GLB
    temp_glb = "temp.glb"

    with open(temp_glb, "wb") as f:
        f.write(glb_data)

    # Load GLB
    gltf = GLTF2().load(temp_glb)

    # Add color to every material
    for material in gltf.materials:

        if material.pbrMetallicRoughness is None:
            continue

        material.pbrMetallicRoughness.baseColorFactor = [
            color[0],
            color[1],
            color[2],
            1.0
        ]

        material.pbrMetallicRoughness.metallicFactor = 0.0
        material.pbrMetallicRoughness.roughnessFactor = 0.7

    # Save modified GLB
    gltf.save(temp_glb)

    with open(temp_glb, "rb") as f:
        new_glb = f.read()

    # Replace old GLB with modified GLB
    new_b3dm = data[:glb_start] + new_glb

    # Update tile byte length
    new_b3dm = (
        new_b3dm[:8]
        + struct.pack("<I", len(new_b3dm))
        + new_b3dm[12:]
    )

    with open(output_file, "wb") as f:
        f.write(new_b3dm)


# Flat 1 = Red
color_b3dm(
    "flat1/tileset/tiles/1.b3dm",
    "flat1/tileset/tiles/1_colored.b3dm",
    (1.0, 0.0, 0.0)
)

# Flat 2 = Green
color_b3dm(
    "flat2/tileset/tiles/1.b3dm",
    "flat2/tileset/tiles/1_colored.b3dm",
    (0.0, 1.0, 0.0)
)

# Flat 3 = Blue
color_b3dm(
    "flat3/tileset/tiles/1.b3dm",
    "flat3/tileset/tiles/1_colored.b3dm",
    (0.0, 0.0, 1.0)
)

print("Created colored B3DM files.")
