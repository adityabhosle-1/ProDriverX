from setuptools import setup
long_des="A command line tool which automates making pdfs and allows you to focus on programming"
setup(
	name="pdx",
	version="1.0.0",
	description="Make PDFS easily",
	long_description=long_des,
	long_description_content_type="text",
	author="Soham And Aditya",
	author_email="MIT",
	packages=['pdx'],
	package_dir={'pdx':'pdx/'},
	classifiers=[
		"Programming Language :: Python :: 2.7",
		"License :: OSI Approved :: MIT License",
		"Environment :: Console",
		"Operating System :: POSIX :: Linux"
	],
	entry_points={
		'console_scripts':['pdx=pdx.pdx:main']
	},
	python_requries="==2.7"
)
