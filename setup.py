import setuptools

setuptools.setup(
    name="krx_holidays",
    version="0.0.3",
    install_requires=[
        'pandas',
        'xlrd'
    ],
    license='MIT',
    author="cheddars",
    author_email="nezahrish@gmail.com",
    description="KRX Holidays",
    long_description=open('README.rst').read(),
    url="https://github.com/cheddars/krx_holidays",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
