# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

import os


class HashTest3(Package):
    """Used to test package hashing
    """

    homepage = "http://www.hashtest3.org"
    url = "http://www.hashtest1.org/downloads/hashtest3-1.1.tar.bz2"

    version('1.2', 'b' * 32)
    version('1.3', 'c' * 32)
    version('1.5', 'd' * 32)
    version('1.6', 'e' * 32)
    version('1.7', 'f' * 32)

    variant('variantx', default=False, description='Test variant X')
    variant('varianty', default=False, description='Test variant Y')

    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        pass

    @when('@:1.4')
    def install(self, spec, prefix):
        print("install 1")
        os.listdir(os.getcwd())

    @when('@1.5:')
    def install(self, spec, prefix):
        os.listdir(os.getcwd())

    for _version_constraint in ['@1.5', '@1.6']:
        @when(_version_constraint)
        def extra_phase(self, spec, prefix):
            pass