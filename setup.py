import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamlit_template",
    version="0.0.1",
    author="telcrome",
    author_email="raphaelschaefer1@outlook.com",
    description="streamlit_template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Telcrome/ai-trainer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    entry_points='''
        [console_scripts]
        st_demo=st_demo.cli:main
    ''',
    install_requires=[
        "click",
        "streamlit"
    ],
)
