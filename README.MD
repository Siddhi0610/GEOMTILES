In Last project i.e. TILEGEN , i converted a lidar scan stored in .las file into .pnts using py3dtiles & then tileset.json described how these .pnts are going to be organised and then streamed on web browser using cesiumjs. e streamed 3d tiles was the point cloud

In this project , GEOMTILES , i am going to convert 3d geometry stored in the form of .WKB file into 3D tile dataset containing tile content stored in .b3dm / .glTF files . then tileset.json will describe how .b3dm is organised & then it will we visualised using cesium.js & streamed on browser

phase 1 - 8/9/26 - converted one .wkb file into .b3dm file hence converting geometry into 3dtile via py3d tiles and then streamed it on browser. saw a small rectangle box, on browser , this was visualised using cesiumjs

now phase 2 - 9/9/26 - taking three apartment flats of a building , storing each of their 3d geometries in a .wkb file. converting this 3d geometry into 3d tiles and storing it in .b3dm file. then streaming these three .b3dm files over browser. its  like segmenting a building into its flats , storing the segmented flats individually, then streaming the flats one by one to reassemble the building. 

phase 2 deviation - i planned 3 .wkb files will get converted into three .b3dm files. but py3dtiles considered the 3 diff .wkb file into one tile and generated only one .b3dm file. i decided to keep it , stream it and see how it looks. 