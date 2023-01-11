
bl_info = { 
    "name": "N-gon tools",
    "category": "3D View"
}
bl_info = {
    "name": "N-gon tools",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Mesh > N-gon",
    "description": "N-gon tool",
    "category": "Mesh",
}
import bpy

from bpy.types import (
    AddonPreferences,
    Operator,
    Panel,
    PropertyGroup,
)

class Holes (Operator):
    bl_idname       = "holes.ngonoperator";
    bl_label        = "Holes";
    bl_description = "Shows if you have holes"
    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        me = bpy.context.object.data
        if len(me.vertices)+len(me.polygons)-len(me.edges) == 2:
            
            self.report({'INFO'}, 'OK')
        else:
            self.report({'INFO'}, 'You have holes') 
        return {'FINISHED'}
    
class MarkNgonOperator(Operator) :
  bl_idname       = "mark.ngonoperator";
  bl_label        = "Mark N-gons";
  bl_description = "Mark N-gons"
  
  def execute(self, context):
    i=0
    bpy.ops.mesh.select_all(action='SELECT') 
    bpy.ops.mesh.mark_freestyle_face(clear=True) 
    bpy.ops.mesh.select_all(action='DESELECT')
    a = 5
    for i in range(500 - 4): 
        bpy.ops.mesh.select_face_by_sides(number=a) 
        bpy.ops.mesh.mark_freestyle_face() 
        bpy.ops.mesh.select_all(action='DESELECT')
        a = a + 1
    return {'FINISHED'}

class ClearNgonOperator(Operator) :
  bl_idname       = "clear.ngonoperator";
  bl_label        = "Clear N-gons";
  bl_description = "Clear marked N-gons"
  
  def execute(self, context):
    bpy.ops.mesh.select_all(action='SELECT') 
    bpy.ops.mesh.mark_freestyle_face(clear=True) 
    bpy.ops.mesh.select_all(action='DESELECT')
    return {'FINISHED'}

class ShowNgonOperator(bpy.types.Operator) :
  bl_idname       = "show.ngonoperator";
  bl_label        = "Show N-gons";
  bl_description = "Hide all not N-gons"
  
  def execute(self, context):
    i=0
    bpy.ops.mesh.select_all(action='SELECT') 
    bpy.ops.mesh.mark_freestyle_face(clear=True) 
    bpy.ops.mesh.select_all(action='DESELECT')
    a = 5
    for i in range(500 - 4): 
        bpy.ops.mesh.select_face_by_sides(number=a) 
        a = a + 1
    bpy.ops.mesh.select_all(action='INVERT')
    bpy.ops.mesh.hide(unselected=False)
    return {'FINISHED'}
'''
class RevealNgonOperator(bpy.types.Operator) :
  bl_idname       = "reveal.ngonoperator";
  bl_label        = "N-gons";
  
  def execute(self, context):
    bpy.ops.mesh.reveal()
    bpy.ops.mesh.select_all(action='DESELECT')
    return {'FINISHED'}

class PokeNgonOperator(bpy.types.Operator) :
  bl_idname       = "poke.ngonoperator";
  bl_label        = "N-gons";
  
  def execute(self, context):
    i=0
    bpy.ops.mesh.select_all(action='SELECT') 
    bpy.ops.mesh.mark_freestyle_face(clear=True) 
    bpy.ops.mesh.select_all(action='DESELECT')
    a = 5
    for i in range(context.object.num_maxValue - 4): 
        bpy.ops.mesh.select_face_by_sides(number=a) 
        a = a + 1
    bpy.ops.mesh.poke()
    bpy.ops.mesh.select_all(action='DESELECT')
    return {'FINISHED'}

'''
def menu_func(self, context):
    self.layout.operator(Holes.bl_idname)
    self.layout.operator(MarkNgonOperator.bl_idname)
    self.layout.operator(ClearNgonOperator.bl_idname)
    self.layout.operator(ShowNgonOperator.bl_idname)
    
    
def register():	
  bpy.utils.register_class(Holes)
  bpy.utils.register_class(MarkNgonOperator)
  bpy.utils.register_class(ClearNgonOperator)
  bpy.utils.register_class(ShowNgonOperator)
  bpy.types.VIEW3D_MT_edit_mesh.append(menu_func)
  
def unregister():
  bpy.utils.unregister_class(Holes)
  bpy.utils.unregister_class(MarkNgonOperator)
  bpy.utils.unegister_class(ClearNgonOperator)
  bpy.utils.unregister_class(ShowNgonOperator)
  bpy.types.VIEW3D_MT_edit_mesh.append(menu_func)
 

 


if __name__ == "__main__":
  register()