from setuptools import setup
from glob import glob

package_name = 'ex_arca'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        #('share/' + package_name, ['launch/launch_drive_control.py']),
        ('share/' + package_name, glob('launch/*.py')), # include all launch files
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='niurover',
    maintainer_email='niurover@gmail.com',
    description="ROS 2 Package to drive the NIU Mars Rover Team's Ex Arca platform.",
    license='MIT License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle_ex_arca = ex_arca.turtle_ex_arca:main',
            'conversationalist = ex_arca.conversationalist:main',
            'drive_control_serial = ex_arca.drive_control_serial:main',
        ],
    },
)
