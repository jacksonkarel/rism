import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="selfmodifai",
    version="0.1.0",
    description="LLM-powered AI agents modifying the source code of other LLMs",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jacksonkarel/selfmodifai",
    author="Jackson Karel",
    author_email="jackson.karel2@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["openai", "transformers", "torch", "xformers", "accelerate", "GitPython", "black", "pytype"],
    setup_requires=["torch"],
    entry_points={
        "console_scripts": [
            "selfmodifai=selfmodifai.__main__:main",
        ]
    },
)