import os
from setuptools import setup, find_packages

package_name = 'gs2d_ros2_driver'


def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements


setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=read_requirements(),
    zip_safe=True,
    description='ROS2 driver for gs2d',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Karakuri Products',
    author_email='gs2d@krkrpro.com',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gs2d = gs2d_ros2_driver.gs2d_ros2_driver:main'
        ],
    },
)
