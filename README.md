# ShapeKeyTransfer_Addon_Blender
An Addon to Transfer ShapeKeys between a Source Object and a Destination Object

## How to Install?
    1. Download the zip from Github. Extract the .py file
    2. In blender Go to Edit-> Preferences-> Install-> Select the ShapeKeyTransferTool.py file.
    3. Enable the Addon by checking the tick box.
## How To use?
   1. **Transfer weights** from **souce obj** to **destination obj** the naming ( of weights) should be the same.
   2. **Place the destination obj close to (almost overlap) the source obj**.
   3. Then use the addon to transfer shapekeys.
### Example
Suppose you want to transfer shapekeys from a humanoid mesh to its clothing asset. 
First transfer weights from the humanoid mesh to the cloth mesh. Then place the cloth onto the humoid mesh and use the addon to transfer the shapkeys.
## Where is the Addon Located?
    In the 3D viewport under the "Tools" section.
    If you can't find the "Tools" section press 'N' on your keyboard.
    
### Tested on Blender 2.8+
