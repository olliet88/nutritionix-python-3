import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='nutritionix_unofficial',
    version='1.0.0',
    description='Nutritionix Python Client (Unofficial update)',
    url='https://github.com/olliet88/nutritionix-python-update',

    # Author details
    author='Ollie Thwaites',
    author_email='olliethwaites@gmail.com',

    # License
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='nutritionix food nutrition',
    packages=setuptools.find_packages(),
    install_requires=['requests'],
)
