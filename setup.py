# -*- coding: utf-8 -*-
version = "0.0.6"
print(version)

import os
from shutil import copy2

from setuptools import setup, find_packages

# load README.md/README.rst file
try:
    if os.path.exists('README.md'):
        with open('README.md', 'r') as fp:
            readme = fp.read()
            readme_type = 'text/markdown; charset=UTF-8'
    elif os.path.exists('README.rst'):
        with open('README.rst', 'r') as fp:
            readme = fp.read()
            readme_type = 'text/x-rst; charset=UTF-8'
    else:
        readme = ""
except:
    readme = ""

setup_args = {
    'name': 'ndx-fllab-novela',
    'version': version,
    'description': 'NovelaNeurotechnologies Namespaces',
    'long_description': readme,
    'long_description_content_type': readme_type,
    'author': 'NovelaDevops',
    'author_email': 'devops@novelaneuro.com',
    'url': '',
    'license': 'BSD 3-Clause',
    'install_requires': [
        'hdmf==1.6.1',
        'pynwb==1.3.0'
    ],
    'packages': find_packages('src/pynwb'),
    'package_dir': {'': 'src/pynwb'},
    'package_data': {'ndx_fllab_novela': [
        'spec/ndx-fllab-novela.namespace.yaml',
        'spec/ndx-fllab-novela.extensions.yaml',
    ]},
    'classifiers': [
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
    'zip_safe': False
}


def _copy_spec_files(project_dir):
    ns_path = os.path.join(project_dir, 'spec', 'ndx-fllab-novela.namespace.yaml')
    ext_path = os.path.join(project_dir, 'spec', 'ndx-fllab-novela.extensions.yaml')

    dst_dir = os.path.join(project_dir, 'src', 'pynwb', 'ndx_fllab_novela', 'spec')
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    copy2(ns_path, dst_dir)
    copy2(ext_path, dst_dir)


if __name__ == '__main__':
    _copy_spec_files(os.path.dirname(__file__))
    setup(**setup_args)
