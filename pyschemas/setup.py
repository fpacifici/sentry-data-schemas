import os
import setuptools
import shutil

if os.path.isfile("../relay/event.schema.json"):
    shutil.copyfile("../relay/event.schema.json", "./schemas/event.schema.json")

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sentry-schemas",
    version="0.0.1",
    author="Sentry",
    license="BSL-1.1",
    author_email="hello@sentry.io",
    description="Sentry shared data schemas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/getsentry/sentry-data-schemas",
    packages=setuptools.find_packages(),
    classifiers=[],
    include_package_data=True,
    install_requires=[
        "jsonschema-typed-v2==0.8.0"
    ],
    python_requires='>=3.8',
)
