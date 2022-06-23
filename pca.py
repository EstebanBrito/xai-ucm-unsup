from helper_pca import load_images, get_pca_input
import os
import numpy as np
from skimage.io import imshow

if __name__ == '__main__':
    images, _ = load_images(os.path.join('.', 'test_imgs'))
    _, images_matrices = get_pca_input(images)
    X = images_matrices['zebra']
    print('Matrix of flattened images', X.shape)
    # TRAIN PCA
    # Center data using mean of every feature
    print(np.mean(np.mean(X)))
    mean = np.mean(X.T, axis=1)
    print(np.max(mean), np.min(mean))
    print('Averages:', mean.shape)
    C = X - mean
    print(np.max(C))
    # Doc's little trick
    L = C @ C.T
    print('Cov. matrix equivalent', L.shape)
    # Warning: T may have the same shape, but use the transpose
    vals, vecs = np.linalg.eig(L)
    print('Eigenvectors', vecs.shape)
    # Sort eigenstuff
    sorted_vals_idxs = np.argsort(vals)[::-1]
    sorted_vals = np.sort(vals)[::-1] # -1 for descending order
    sorted_vecs = vecs[sorted_vals_idxs]
    print(sorted_vals[0])
    # Construct
    u = np.zeros((78, 150528))
    for i, eig in enumerate(sorted_vecs):
        u[i] = C.T @ eig
        u[i] = u[i] / np.linalg.norm(u[i])
    print('Unnamed matrix', u.shape)
    print('1st Component', u[0][0])
    prototype = np.reshape(u[0], (224, 224, 3))
    print(np.max(prototype))
    print(np.min(prototype))
    prototype = np.abs(prototype / np.max(prototype))
    print(np.max(prototype))
    print(np.min(prototype))
    imshow(prototype)


