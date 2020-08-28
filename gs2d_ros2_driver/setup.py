from setuptools import setup

package_name = 'gs2d_ros2_driver'


setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    py_modules=['gs2d_ros2_driver.gs2d_ros2_driver'],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'gs2d'],
    zip_safe=False,
    description='ROS2 driver for gs2d',
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
