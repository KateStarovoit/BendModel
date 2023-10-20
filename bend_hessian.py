from igl import *
import scipy

def calculate_bend_hessian(v, f):
    L = igl.pyigl.cotmatrix(v, f)
    M = igl.pyigl.massmatrix(v, f, igl.MASSMATRIX_TYPE_BARYCENTRIC)
    boundary_v = igl.pyigl.boundary_loop(f)
    for i in boundary_v:
        L[i] = 0
    #return 0.5*(v.transpose()*L.transpose()*scipy.sparse.linalg.inv(M)*L*v)
    return (L.transpose()*scipy.sparse.linalg.inv(M)*L)