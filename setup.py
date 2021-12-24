import setuptools

setuptools.setup(
    name='wifi-menu',
    version='1.0',
    author='Charles Marchildon',
    author_email='charles.marchildon2@gmail.com',
    description='Menu for nmcli',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'wifi = src.__main__:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT License',
        'Operating System :: Linux'
    ],
)
