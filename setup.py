from setuptools import setup, find_packages

setup(
    name="gurtai-llama",
    version="0.1.0",
    description="GurtAi — A forked Llama architecture with custom branding",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.38.0",
    ],
    author="Gurt",
    author_email="",
    license="Apache 2.0",
)
