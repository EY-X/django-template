import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='django-template',  
     version='0.1',
     scripts=['django-template'],
     author="Jacob Benaim",
     author_email="benaimjacob@gmail.com",
     description="A Django-template utility package with Auth",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/jaybenaim/django-template",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )