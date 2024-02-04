# setup.py

from setuptools import setup, find_packages

# setuptools is a Python library used to facilitate packaging and distribution of Python packages.
# It provides necessary functions to specify what files and dependencies are needed.

setup(
    name="tictactoe",  # This is the name of your package
    version="0.1.0",  # The initial release version
    packages=find_packages(where='src'),  # This function automatically finds all packages in the 'src' directory.
    package_dir={'': 'src'},  # This specifies that the packages are located under the 'src' directory.

    # Here we specify dependencies. These are external packages that your project depends on.
    # These packages will be installed automatically when installing your package.
    # install_requires=[
    #     # For this project, there are no dependencies, but typically it would look like this:
    #     # 'numpy', 'pandas', etc.
    # ],

    entry_points={
        "console_scripts": [
            "tictactoe = tictactoe.main:main",
        ]
    },

    # Metadata for your project
    author="Cedric Anover",
    author_email="ca20110820@gmail.com",
    description="A refactored version and improved version of a Tic Tac Toe game",
    license="MIT",
    keywords="tic-tac-toe refactoring",
    url="https://github.com/ca20110820/tictactoe",  # project home page
)

# With this setup.py in place, you can install your project in another environment with pip:
# pip install .
# The '.' means that setup.py is in the current directory
