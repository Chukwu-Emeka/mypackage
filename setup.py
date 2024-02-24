from setuptools import setup, find_packages

setup(
    name='mypackage',
    version = '0.1',
    packages=find_packages(exclude=['test*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Chukwu-Emeka/Data-Learning.git',
    author='Emeka Ibezimako',
    author_email='ibezimakoemeka@gmail.com'
)