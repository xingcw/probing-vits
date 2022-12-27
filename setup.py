import setuptools
from pip._internal.req import parse_requirements


install_reqs = parse_requirements("requirements.txt", session="test")
reqs = [str(ir.requirement) for ir in install_reqs]

__version__ = '0.0.1'

setuptools.setup(
    name='prob_vit',
    version=__version__,
    packages=setuptools.find_packages(),
    install_requires=reqs
)