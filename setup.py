# Don't import __future__ packages here; they make setup fail
import shutil
import os

# We need to copy the generated swagger to the Python package
SWAGGER_JSON_PATH = os.path.abspath(
    os.path.join('openapi', 'workflow_execution_service.swagger.yaml'))
SWAGGER_DEST_PATH = os.path.abspath(os.path.join(
    'python', 'ga4gh', 'wes', 'workflow_execution_service.swagger.yaml'))
shutil.copyfile(SWAGGER_JSON_PATH, SWAGGER_DEST_PATH)

# First, we try to use setuptools. If it's not available locally,
# we fall back on ez_setup.
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

with open("python/README.pypi.rst") as readmeFile:
    long_description = readmeFile.read()

install_requires = []
with open("python/requirements.txt") as requirementsFile:
    for line in requirementsFile:
        line = line.strip()
        if len(line) == 0:
            continue
        if line[0] == '#':
            continue
        pinnedVersion = line.split()[0]
        install_requires.append(pinnedVersion)

dependency_links = []
try:
    with open("python/constraints.txt") as constraintsFile:
        for line in constraintsFile:
            line = line.strip()
            if len(line) == 0:
                continue
            if line[0] == '#':
                continue
            dependency_links.append(line)
except EnvironmentError:
    print('No constraints file found, proceeding without '
          'creating dependency links.')
print(dependency_links)

setup(
    name="ga4gh_wes_schemas",
    description="GA4GH Data Object Service Schemas",
    packages=[
        "ga4gh",
        "ga4gh.wes"
    ],
    namespace_packages=["ga4gh"],
    url="https://github.com/ga4gh/workflow-execution-service-schemas",
    entry_points={
        'console_scripts': [
            'ga4gh_wes_server=ga4gh.wes.server:main',
            'ga4gh_wes_client=ga4gh.wes.client:main',
        ]
    },
    package_dir={'': 'python'},
    long_description=long_description,
    install_requires=install_requires,
    dependency_links=dependency_links,
    license='Apache License 2.0',
    package_data={'ga4gh.wes': ['workflow_execution_service.swagger.yaml'],},
    include_package_data=True,
    zip_safe=True,
    author="Global Alliance for Genomics and Health",
    author_email="theglobalalliance@genomicsandhealth.org",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    version='0.3.0',
    keywords=['genomics'],
    # Use setuptools_scm to set the version number automatically from Git
    setup_requires=['setuptools_scm'],
)
