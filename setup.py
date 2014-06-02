from setuptools import setup, find_packages

setup(
        name='blinkDetect',
        version='0.1',
        description='Fast blink detector using Haar cascade \
                detection and simple binary thresholding',
        packages=find_packages(),
        include_package_data=True,
        package_data = { '': [ '*.xml' ] },
        install_requires=[],
        )

