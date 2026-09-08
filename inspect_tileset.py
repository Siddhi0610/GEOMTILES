import json


def inspect_tile(tile, level=0):
    indent = "  " * level

    print(f"{indent}Tile level: {level}")
    print(f"{indent}Geometric error: {tile.get('geometricError')}")
    print(f"{indent}Refine: {tile.get('refine')}")
    print(f"{indent}Bounding volume: {tile.get('boundingVolume')}")
    print(f"{indent}Content: {tile.get('content')}")

    children = tile.get("children", [])

    print(f"{indent}Children: {len(children)}")

    for child in children:
        inspect_tile(child, level + 1)


with open("output/tileset.json", "r") as f:
    tileset = json.load(f)

print("=== TILESET ===")
print("Asset:")
print(tileset["asset"])

print("\n=== TILE HIERARCHY ===")

inspect_tile(tileset["root"])