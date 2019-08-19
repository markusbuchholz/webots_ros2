"""webots_ros2 package setup file."""

from setuptools import setup

package_name = 'webots_ros2-universal-robot'
data_files = []


data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name, ['launch/universal_robot.launch.py']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/universal_robot.wbt']))
data_files.append(('share/' + package_name, ['package.xml']))


setup(
    name=package_name,
    version='0.0.2',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    author='Cyberbotics',
    author_email='support@cyberbotics.com',
    maintainer='Cyberbotics',
    maintainer_email='support@cyberbotics.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Universal Robot ROS2 interface for Webots.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 'universal_robot = webots_ros2.universal_robot:main' ],
        'launch.frontend.launch_extension': [ 'launch_ros = launch_ros' ]
    }
)
