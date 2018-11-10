from setuptools import setup, find_packages
import versioneer
import io
import os


def read(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with io.open(filepath, mode='r', encoding='utf-8') as f:
        return f.read().splitlines()


setup(
    name='thrill_digger_tdd',
    packages=find_packages(), 
    version=versioneer.get_version(), 
    cmdclass=versioneer.get_cmdclass(), 
    entry_points={
        'console_scripts': [
            'thrill_digger_tdd = thrill_digger_tdd.__main__:main'
        ]
    },
    url='https://github.com/Seth-Rothschild/thrill_digger_tdd.git',
    author='Seth Rothschild',
    author_email='seth.j.rothschild@gmail.com',
    description='Like adventure? Danger?',
    install_requires=read('requirements.txt'),
    tests_require=[
        'hypothesis', 'pytest'
    ],
    test_suite='pytest'
)
