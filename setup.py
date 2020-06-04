import setuptools 

with open('README.md') as readme_file:
	README = readme_file.read()

setuptools.setup(
	name="ct2vl",
	version="0.0.3",
	author= "Ramy Arnaout",
	author_email="rarnaout@bidmc.harvard.edu",
	description="Convert Ct values to viral loads for the Abbott m2000 SARS-CoV-2 RT-PCR test",
	long_description=README, 
	long_description_content_type="text/markdown",
	url ="https://github.org/rarnaout/ct2vl",
	packages=setuptools.find_packages(),
	classifiers = [
		"Programming Language :: Python :: 3", # took the examples straight from python.org so may need to adjust these details 
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires ='>=3.6',
)

