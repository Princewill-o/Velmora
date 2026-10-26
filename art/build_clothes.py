"""Original Velmora concept garments. Run with Blender --background --python."""
import bpy, math, os
from mathutils import Vector

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL=os.path.join(ROOT,'public','models')
RENDER=os.path.join(ROOT,'art','renders')
os.makedirs(MODEL,exist_ok=True);os.makedirs(RENDER,exist_ok=True)
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)

def material(name,color,roughness=.5,metallic=.02):
 m=bpy.data.materials.new(name);m.diffuse_color=(*color,1);m.use_nodes=True
 p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*color,1);p.inputs['Roughness'].default_value=roughness;p.inputs['Metallic'].default_value=metallic
 p.inputs['Sheen Weight'].default_value=.25;p.inputs['Sheen Roughness'].default_value=.4
 p.inputs['Coat Weight'].default_value=.03
 return m
satin=material('Velmora_Oxblood_Satin',(.11,.012,.025))
lining=material('Velmora_Inner_Fabric',(.12,.013,.028),.6)
gold=material('Brushed_Brass',(.52,.34,.15),.24,.8)

def mesh(name,vertices,faces,mat,parent=None,solid=True):
 data=bpy.data.meshes.new(name);data.from_pydata(vertices,[],faces);data.update()
 obj=bpy.data.objects.new(name,data);bpy.context.collection.objects.link(obj);obj.data.materials.append(mat);obj.parent=parent
 for f in obj.data.polygons:f.use_smooth=True
 if solid:
  mod=obj.modifiers.new('Fabric thickness','SOLIDIFY');mod.thickness=.007;mod.offset=0
 return obj
def curve(name,points,mat,parent,radius=.006):
 c=bpy.data.curves.new(name,'CURVE');c.dimensions='3D';c.resolution_u=4;c.bevel_depth=radius;c.bevel_resolution=3
 s=c.splines.new('BEZIER');s.bezier_points.add(len(points)-1)
 for b,co in zip(s.bezier_points,points):b.co=co;b.handle_left_type='AUTO';b.handle_right_type='AUTO'
 obj=bpy.data.objects.new(name,c);bpy.context.collection.objects.link(obj);obj.data.materials.append(mat);obj.parent=parent
 return obj
def root(name):
 obj=bpy.data.objects.new(name,None);bpy.context.collection.objects.link(obj);return obj
def smooth_profile(t,keys):
 for i in range(len(keys)-1):
  a,ra=keys[i];b,rb=keys[i+1]
  if a<=t<=b:
   v=(t-a)/(b-a);v=v*v*(3-2*v);return ra+(rb-ra)*v
 return keys[-1][1]

def gown(name,aline=False):
 parent=root(name);N=144;M=112;verts=[];faces=[]
 profile=[(0,.43),(.10,.48),(.23,.31),(.37,.46),(.50,.53),(.75,.67 if not aline else .89),(1,.85 if not aline else 1.23)]
 for i in range(N+1):
  t=i/N;z=1.48-t*3.65;r=smooth_profile(t,profile)
  for j in range(M+1):
   a=2*math.pi*j/M;folds=(math.sin(a*12+t*4)+.35*math.sin(a*21-t*3))*(.009+.055*max(0,(t-.3)/.7)**1.3)
   radius=r+folds
   # Lower front neckline and soft cowl drape; a continuous sewn tube with a hollow interior.
   front=max(0,-math.sin(a));neck=-.23*front**2*max(0,1-t/.14)**2 if not aline else .045*math.cos(a*2)*max(0,1-t/.08)
   drape=.025*math.sin(a*3+t*24)*front*math.exp(-((t-.11)/.10)**2) if not aline else .006*math.sin(a*8)
   zz=z+neck+drape+.022*math.sin(a*7)*t**5
   verts.append((math.cos(a)*radius,math.sin(a)*radius*.64,zz))
 for i in range(N):
  for j in range(M):
   a=i*(M+1)+j;b=a+M+1;faces.append((a,b,b+1,a+1))
 obj=mesh(name+'_Body',verts,faces,satin,parent)
 # Delicate real straps and collar-edge stitching.
 if not aline:
  for x in [-.34,.34]:curve(name+'_Strap',[(x,-.18,1.39),(x*1.04,-.10,1.79),(x*1.03,.09,1.79),(x,.2,1.47)],satin,parent,.013)
 for side in [-1,1]:
  points=[]
  for i in range(100):
   t=i/99;r=smooth_profile(t,profile);points.append((side*(r+.006),0,1.48-t*3.65))
  curve(name+'_Side_Seam',points,lining,parent,.0025)
 for label,t in [('Hem',.995),('Neckline',0)]:
  points=[]
  for j in range(M+1):
   index=(N if t>.9 else 0)*(M+1)+j;v=verts[index];points.append((v[0]*1.002,v[1]*1.002,v[2]+.004))
  curve(name+'_'+label,points,satin,parent,.0035)
 return parent

def jacket():
 parent=root('Evening_Blazer');N=70;M=100;verts=[];faces=[]
 for i in range(N+1):
  t=i/N;z=1.55-t*1.95;r=smooth_profile(t,[(0,.47),(.2,.53),(.58,.34),(1,.48)])
  for j in range(M+1):
   # Front opening is wide at lapels, narrowing at the single fastening.
   opening=.75*max(0,1-t/.65)+.06
   a=-math.pi/2+opening+(2*math.pi-2*opening)*j/M
   rad=r+.009*math.sin(a*12+t*15)
   verts.append((math.cos(a)*rad,math.sin(a)*rad*.63,z-.12*abs(math.cos(a))**8*max(0,1-t/.2)))
 for i in range(N):
  for j in range(M):
   a=i*(M+1)+j;b=a+M+1;faces.append((a,b,b+1,a+1))
 mesh('Blazer_Body',verts,faces,satin,parent)
 for side in [-1,1]:
  v=[];f=[]
  for i in range(65):
   t=i/64;z=1.39-t*1.77;cx=side*(.52+.29*t);cy=.03+.03*math.sin(t*math.pi);r=.175-.048*t
   for j in range(49):
    a=j/48*2*math.pi;pleat=.012*math.sin(a*7+t*19)*math.sin(math.pi*t);v.append((cx+math.cos(a)*(r+pleat),cy+math.sin(a)*(r+pleat),z))
  for i in range(64):
   for j in range(48):
    a=i*49+j;b=a+49;f.append((a,b,b+1,a+1))
  mesh('Blazer_Sleeve',v,f,satin,parent)
  cv=[];cf=[]
  for u in range(17):
   r=(u+.01)/16.01
   for j in range(49):
    a=j/48*2*math.pi
    cv.append((side*(.52+.178*r*math.cos(a)),.03+.178*r*math.sin(a),1.39+.10*math.sqrt(max(0,1-r*r))))
  for u in range(16):
   for j in range(48):
    k=u*49+j;cf.append((k,k+49,k+50,k+1))
  mesh('Blazer_Shoulder',cv,cf,satin,parent)
  # Folded notched lapels, lifted away from the chest.
  points=[(side*.10,-.08,1.66),(side*.29,-.30,1.34),(side*.40,-.30,1.12),(side*.27,-.37,1.08),(side*.36,-.34,.94),(side*.08,-.29,.15)]
  lap=mesh('Blazer_Notched_Lapel',points,[(0,1,2,3,4,5)],satin,parent)
  sub=lap.modifiers.new('Lapel edge bevel','BEVEL');sub.width=.012;sub.segments=3
  curve('Blazer_Welt_Pocket',[(side*.17,-.29,-.04),(side*.39,-.22,-.02)],lining,parent,.01)
 bpy.ops.mesh.primitive_uv_sphere_add(segments=20,ring_count=12,radius=.027,location=(.06,-.292,.12));button=bpy.context.object;button.name='Blazer_Brass_Button';button.scale=(1,.4,1);button.parent=parent;button.data.materials.append(gold)
 return parent

garments=[gown('Draped_Gown'),gown('Structured_Gown',True),jacket()]
bpy.ops.object.select_all(action='DESELECT')
for obj in list(bpy.context.scene.objects):
 if obj.type=='CURVE':obj.select_set(True);bpy.context.view_layer.objects.active=obj
bpy.ops.object.convert(target='MESH')
# Render an honest asset preview from the same geometry served to Three.js.
scene=bpy.context.scene;scene.render.engine='CYCLES';scene.cycles.samples=32;scene.cycles.use_denoising=True;scene.render.resolution_x=900;scene.render.resolution_y=1100;scene.render.resolution_percentage=100;scene.render.film_transparent=False
scene.world.color=(.12,.12,.12);scene.world.use_nodes=True;scene.world.node_tree.nodes.get('Background').inputs[0].default_value=(.22,.19,.23,1);scene.world.node_tree.nodes.get('Background').inputs[1].default_value=.45
scene.view_settings.view_transform='AgX'
bpy.ops.object.camera_add(location=(4,-8,2.1));camera=bpy.context.object;camera.name='Studio_Camera';camera.rotation_euler=(Vector((0,0,-.15))-camera.location).to_track_quat('-Z','Y').to_euler();camera.data.type='ORTHO';camera.data.ortho_scale=5.0;scene.camera=camera
for name,loc,power,size in [('Key',(-3,-4,5),950,4),('Fill',(4,-2,2),700,3),('Rim',(1,3,4),1300,3)]:
 bpy.ops.object.light_add(type='AREA',location=loc);light=bpy.context.object;light.name=name;light.data.energy=power;light.data.shape='DISK';light.data.size=size;light.rotation_euler=(Vector((0,0,0))-light.location).to_track_quat('-Z','Y').to_euler()
for parent in garments:
 for other in garments:
  for child in other.children:child.hide_render=other!=parent
 bpy.ops.object.select_all(action='DESELECT');parent.select_set(True)
 for child in parent.children:child.select_set(True)
 file={'Draped_Gown':'draped-gown','Structured_Gown':'structured-gown','Evening_Blazer':'evening-blazer'}[parent.name]
 bpy.ops.export_scene.gltf(filepath=os.path.join(MODEL,file+'.glb'),export_format='GLB',use_selection=True,export_apply=True,export_yup=True,export_animations=False,export_extras=True)
 camera.data.ortho_scale=3.1 if file=='evening-blazer' else 5.0
 target=Vector((0,0,.56 if file=='evening-blazer' else -.15));camera.rotation_euler=(target-camera.location).to_track_quat('-Z','Y').to_euler()
 scene.render.filepath=os.path.join(RENDER,file+'.png');bpy.ops.render.render(write_still=True)
for parent in garments:
 for child in parent.children:child.hide_render=False
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(ROOT,'art','models','velmora-garments.blend'))
print('VELMORA_ASSETS_COMPLETE')
