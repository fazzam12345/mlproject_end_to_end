from setuptools import setup, find_packages



def get_requirements(file_path:str)->list[str]:
    '''
    this function will return a list of requirements from a file
    '''
    HYPEN_E_DOT = "-e ."
    requirements = []
    with open(file_path) as file_obj:
         requirements = file_obj.readlines()
         requirements = [requirement.replace('\n','') for requirement in requirements]
         if HYPEN_E_DOT in requirements:
             requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name='end_to_end_ml_project',
    version='0.1.0',
    description='End-to-end machine learning project with deployment',
    author='Fares',
    author_email='azzamfares.199@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)