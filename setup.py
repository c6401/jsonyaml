from distutils.core import setup

setup(
    name='jsonyaml',
    version='1.0',
    description='Creates json from yaml',
    author='Ruslan Zhenetl',
    author_email='nc6401+gh@gmail.com',
    url='https://github.com/c6401/jsonyaml',
    scripts=['jsonyaml'],
    install_requires=[
        "pyyaml",
    ],
)
