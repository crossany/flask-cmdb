import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='Flask-CMDB',
    version='1.0.0',
    url='http://github.com/crossany/flask-cmdb',
    license='BSD',
    author='JIN CHEN',
    author_email='crossany@gmail.com',
    description='An extension that includes AdminLTE in your '
                'project, without any boilerplate code.',
    long_description=read('README.rst'),
    packages=['flask_adminlte'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=1.1.1',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
