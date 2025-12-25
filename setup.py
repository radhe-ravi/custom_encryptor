from setuptools import setup, find_packages

setup(
    name="encryptor",                     # Package name
    version="0.1.0",                      # Version
    packages=find_packages(),              # Auto-find packages
    install_requires=[                     # Dependencies
        "cryptography>=41.0.0"
    ],
    author="Radhe Ravi",
    author_email="your_email@example.com",
    description="A secure Python module for encrypting and decrypting strings with custom key/salt/iterations",
    url="https://github.com/radhe-ravi/custom_encryptor.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
