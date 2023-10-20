import polyscope as ps
import trimesh
import numpy as np
import bend_hessian
import igl

def visualise_mesh(init_mesh_file, current_mesh_file):
    #Load meshes
    init_mesh = trimesh.load(init_mesh_file)
    init_v = init_mesh.vertices
    init_f = init_mesh.faces

    current_mesh = trimesh.load(current_mesh_file)
    current_v = current_mesh.vertices
    current_f = current_mesh.faces

    #Calclulate hessian and force
    H = bend_hessian.calculate_bend_hessian(current_v, current_f)
    forces = H @ current_v

    #Visualize
    ps.init()

    ps_mesh = ps.register_surface_mesh("my mesh", current_v, current_f)

    ps_mesh.add_vector_quantity("bend forces", forces, enabled=True, length=2)

    # set radius/length/color of the vectors
    #ps_mesh.add_vector_quantity("rand vecs opt", vecs_vert, radius=0.001,
    #                            length=0.005, color=(0.2, 0.5, 0.5))

    # ambient vectors don't get auto-scaled, useful e.g. when representing offsets in 3D space
    #ps_mesh.add_vector_quantity("vecs ambient", vecs_vert, vectortype='ambient')

    # view the mesh with all of these quantities
    ps.show()
