from neatmesh.meshio_handler import MeshioHandler3D

if __name__ == "__main__":
    mesh = MeshioHandler3D("./neatmesh/test_meshes/tetra_wedge.med")
    """cells = mesh.cells()
    
    for _ in range(mesh.n_cells):
        print(next(cells))"""
