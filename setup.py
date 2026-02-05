import ast

from setuptools import find_packages, setup

version = 'unknown'
with open('eventmq/__init__.py') as f:
    for line in f:
        if line.startswith('__version__'):
            version = ast.parse(line).body[0].value.value
            break

setup(
    name='eventmq',
    version=version,
    description='EventMQ job execution and messaging system based on ZeroMQ',
    packages=find_packages(),
    python_requires='>=3.10',
    install_requires=[
        'pyzmq==25.1.2',
        'croniter==2.0.5',
        'psutil==5.9.8',
    ],
    extras_require={
          'docs': ['Sphinx>=7.0.0,<8', ],
          'testing': [
              'flake8>=7.0.0,<8',
              'flake8-import-order>=0.18.2,<1',
              'flake8-print>=5.0.0,<6',
              'coverage>=7.0.0,<8',
              'testfixtures>=8.0.0,<9',
              'freezegun>=1.4.0,<2',
          ],
      },
    author='EventMQ Contributors',
    url='https://github.com/eventmq/eventmq/',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: System :: Distributed Computing',

        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',  # noqa
        'Operating System :: OS Independent',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    scripts=[
        'bin/emq-cli',
        'bin/emq-jobmanager',
        'bin/emq-router',
        'bin/emq-scheduler',
        'bin/emq-pubsub'
    ],
)
