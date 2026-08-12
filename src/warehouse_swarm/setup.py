from setuptools import find_packages, setup

package_name = 'warehouse_swarm'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    python_requires='>=3.8',
    zip_safe=True,
    maintainer='shivam',
    maintainer_email='shivamchaturvedi.in@gmail.com',
    description='Warehouse swarm management package for ROS 2.',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'warehouse_swarm = warehouse_swarm.cli:main',
        ],
    },
)
