from setuptools import setup
from portable_extension import PortableExtension, BuildExtension

import os.path as osp

ROOT = osp.dirname(osp.abspath(__file__))

setup(
    name='lietorch',
    version='0.2',
    description='Lie Groups for PyTorch',
    author='teedrz',
    packages=['lietorch'],
    ext_modules=[
        PortableExtension('lietorch_backends', 
            include_dirs=[
                osp.join(ROOT, 'lietorch/include'), 
                "/usr/include/eigen3",
                "/usr/local/include/eigen3"],
            sources=[
                'lietorch/src/lietorch.cpp', 
                'lietorch/src/lietorch_gpu.cu',
                'lietorch/src/lietorch_cpu.cpp'],
            extra_compile_args={
                'cxx': ['-O2',"-std=c++17"],
                'nvcc': ['-O2',"-std=c++17",
                    '-gencode=arch=compute_60,code=sm_60', 
                    '-gencode=arch=compute_61,code=sm_61', 
                    '-gencode=arch=compute_70,code=sm_70', 
                    '-gencode=arch=compute_75,code=sm_75',
                    '-gencode=arch=compute_75,code=compute_75',
                ]
            }),

        PortableExtension('lietorch_extras', 
            sources=[
                'lietorch/extras/altcorr_kernel.cu',
                'lietorch/extras/corr_index_kernel.cu',
                'lietorch/extras/se3_builder.cu',
                'lietorch/extras/se3_inplace_builder.cu',
                'lietorch/extras/se3_solver.cu',
                'lietorch/extras/extras.cpp',
            ],
            extra_compile_args={
                'cxx': ['-O2',"-std=c++17"],
                'nvcc': ['-O2',"-std=c++17",
                    '-gencode=arch=compute_60,code=sm_60', 
                    '-gencode=arch=compute_61,code=sm_61', 
                    '-gencode=arch=compute_70,code=sm_70', 
                    '-gencode=arch=compute_75,code=sm_75',
                    '-gencode=arch=compute_75,code=compute_75',
                    
                ]
            }),
    ],
    cmdclass={ 'build_ext': BuildExtension }
)
