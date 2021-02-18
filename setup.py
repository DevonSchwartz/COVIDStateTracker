from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = "Package to Access State COVID Data"
LONG_DESCRIPTION = 'Package to Access State COVID Data for camp, interface with pandas'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="COVIDDataInterface", 
        version= VERSION,
        author="Devon Schwartz and Neil Aylor",
        author_email="<devon.s.schwartz@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["pandas"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'COVID','state'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)