from setuptools import find_packages, setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='py_lexical_analyzer',
    version='1.0.0',
    description='Lexic Analyzer Build with Python',
    long_description=readme(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    url="https://github.com/giusniyyel/pylexicanalyzer",
    author='Jose Daniel Bautista Campos',
    author_email='giusniyyel@gmail.com',
    keywords='lexical analyzer compilers analizador lexico compiladores',
    license='LGPLv2+',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    zip_safe=False
)