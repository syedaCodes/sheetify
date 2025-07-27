from setuptools import setup, find_packages

setup(
    name='sheetify',
    version='1.0.0',
    description='Convert and clean messy CSV, JSON, and raw data into clean Excel/CSV files.',
    author='Syeda',
    author_email='your@email.com',
    url='https://github.com/syedacodes/sheetify',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'streamlit',
        'pandas',
        'openpyxl'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.7'
)
