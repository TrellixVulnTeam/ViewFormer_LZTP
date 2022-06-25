#!/usr/bin/env python
import os
from setuptools import setup, find_packages

requirements = '''
torch==1.11.0
torchvision==0.12.0
pytorch_lightning==1.1.2
tensorflow-addons==0.17.0
tensorflow==2.9.1
fsspec>=0.8.5
webdataset==0.1.40
colorlog>=4.4.0
wandb>=0.10.8
pytest>=6.1.2
pytest-benchmark>=3.2.3
lpips==0.1.3
onnx_tf==1.8.0
onnx==1.12.0
einops>=0.3.2
tqdm>=4.45.0
aparse==0.0.14
attrs>=0.3.1
click>=8.0.1
tfrecord==1.14.1
matplotlib>=3.5.0
requests>=2.26.0
scipy>=1.7.3
'''.split()

setup(
    name='viewformer',
    version='0.0.1',
    description='ViewFormer: NeRF-free Neural Rendering from Few Images Using Transformers',
    author='',
    author_email='',
    url='',
    install_requires=requirements,
    packages=find_packages(include=('viewformer', 'viewformer.*')),
    entry_points={
        'console_scripts': ['viewformer-cli = viewformer.cli:main']
    },
)
