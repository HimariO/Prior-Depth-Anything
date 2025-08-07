from setuptools import setup, find_packages

setup(
    name="prior_depth_anything",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'torch>=2.2.2',
        'numpy>=1.25.2',
        'huggingface_hub>=0.26.5',
        'einops>=0.8.1',
        'Pillow',
        'torchvision>=0.17.2',
        'opencv-python',
        'torch_cluster',
        'safetensors>=0.4.5',
        'matplotlib'
    ],
    entry_points={
        "console_scripts": [
            "priorda = prior_depth_anything.cli:create_and_execute"
        ]
    },
    description="A pytorch implementation of Prior-Depth-Anything",
    author="Zehan Wang, Siyu Chen, Lihe Yang, Jialei Wang, Ziang Zhang, Hengshuang Zhao, Zhou Zhao", 
    author_email="wangzehan01@zju.edu.cn",
    url="https://github.com/SpatialVision/Prior-Depth-Anything"
)
