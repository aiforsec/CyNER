from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    readme = f.read()
version = '0.0.1'
setup(
    name='cyner',
    packages=find_packages(exclude=["tests", "models"]),
    version=version,
    license='MIT',
    description='Cybersecurity named entity recognition',
    url='https://github.com/aiforsec/CyNER',
    download_url="https://github.com/aiforsec/CyNER/archive/{}.tar.gz".format(version),
    keywords=['ner', 'nlp', 'language-model'],
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Tanvirul Alam',
    author_email='tanvirul.alam@mail.rit.edu',
    classifiers=[
        'Development Status :: 4 - Beta',       # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    ],
    include_package_data=True,
    # test_suite='tests',
    install_requires=[
        'flair',
        'spacy',
        'ipywidgets',
        'spacy-transformers',
        'Pillow>=7.1.0',
        'sudachipy',
        'sudachidict_core',
        'uvicorn==0.11.8',
        'jinja2==2.11.3',
        'aiofiles==0.5.0',
        'fastapi==0.65.2',
        'matplotlib==3.3.1',
        'toml',
        'tensorboard',
        'torch',
        'transformers',
        'sentencepiece',
        'seqeval',
        'segtok'
    ],
    python_requires='>=3.6',
)