from setuptools import setup, find_packages

setup(
    name="syslog-wrap",  # Package name on PyPI
    version="1.0.0",  # Initial version
    description="A tool to wrap commands and forward logs to syslog.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your_email@example.com",
    url="https://github.com/yourusername/syslog-wrap",  # Link to your GitHub or project repo
    packages=find_packages(),
    install_requires=[  # Dependencies
        "asyncio",  # Or any other dependencies
    ],
    entry_points={  # CLI entry point
        "console_scripts": [
            "robust-syslog-wrap=robust_syslog_wrap.main:main",
        ]
    },
    classifiers=[  # PyPI classifiers for your package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version
)

