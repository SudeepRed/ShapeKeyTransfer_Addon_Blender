bl_info = {
    "name": "ShapeKey Transfer Toll",
    "author": "Sudeep Reddy",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Tools",
    "description": "Transfers all the ShapeKeys from Source to Destination",
    "warning": "Transfer the wieghts beforehand",
    "doc_url": "",
    "category": "Tools",
}



import bpy

def get_Items(self, context):
    source=[]
    for ob in bpy.context.scene.objects:
        if ob.type == 'MESH':
            source.append((ob.name_full,ob.name_full,"Mesh"))
            print (ob.name_full)
    return source

class CustomProp(bpy.types.PropertyGroup):
    source_mesh:bpy.props.EnumProperty(
        name="Source",
        description="Select Source",
        items=get_Items
    )
    destination_mesh:bpy.props.EnumProperty(
        name="Destination",
        description="Select Source",
        items=get_Items
    )

class ShapeKeyTransfer(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "ShapeKey Transfer Tool"
    bl_idname = "SKT_Tool"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'
    
    def draw(self, context):
        layout = self.layout
        
        scene=context.scene
        skt_tool=scene.SKT_Prop
        layout.prop(skt_tool,"source_mesh")
        
        row = layout.row()
        layout.prop(skt_tool,"destination_mesh")
                
        row = layout.row()        
        row.operator("skt.tool")
        
        
        
    
class SKT_Tool_OP(bpy.types.Operator):
    
    bl_label="Transfer!"
    bl_idname="skt.tool"
    
    
        
    def execute(self, context):
        s=bpy.context.scene.SKT_Prop.source_mesh
        d=bpy.context.scene.SKT_Prop.destination_mesh
        obj=bpy.data.objects[d]
        obj2=bpy.data.objects[s]
        shapeKey=obj2.data.shape_keys
        if(s!=d and shapeKey!=None):
            obj=bpy.data.objects[d]
            obj2=bpy.data.objects[s]
            for i in obj2.data.shape_keys.key_blocks:
                if(i.name!='Basis'):
                    i.value=i.slider_min
                    obj.modifiers.new(name=i.name,type='SURFACE_DEFORM')
                    obj.modifiers[i.name].target=obj2
                    bpy.ops.object.surfacedeform_bind(modifier=i.name)
                    i.value=i.slider_max
                    bpy.ops.object.modifier_apply(apply_as='SHAPE', modifier=i.name)
                    i.value=i.slider_min
        elif(s==d):
            self.report({'ERROR'},"Source and Destination cannot be the same")
        elif(shapeKey==None):
            self.report({'INFO'},"Source has no Shape Keys to transfer")
        return{'FINISHED'}
    

    
classes=[CustomProp, ShapeKeyTransfer, SKT_Tool_OP]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
        bpy.types.Scene.SKT_Prop=bpy.props.PointerProperty(type=CustomProp)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        del bpy.types.Scene.SKT_Prop

if __name__ == "__main__":
    register() 
