
from setuptools import setup
from utile import git_version
import filewatcher

readme = open('README.rst').read()
changes = open('CHANGES.txt').read()
version = git_version(filewatcher.__version__)

setup(
    name='filewatcher',
    version=version,
    description="Collection of useful functions and classes",
    long_description=readme + '\n\n' + changes,
    keywords='filewatcher',
    author='Marwan Alsabbagh',
    author_email='marwan.alsabbagh@gmail.com',
    url='https://github.com/marwano/filewatcher',
    license='BSD',
    py_modules=['filewatcher'],
    namespace_packages=[],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
