from setuptools import setup

package_name = 'ad_boxtra'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='luckierdodge',
    maintainer_email='ryandlewis.rl@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle_ad_boxtra = ad_boxtra.turtle_ad_boxtra:main'
        ],
    },
)
