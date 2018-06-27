# Copyright (C) 2011-2016 Paul Kienzle <pkienzle@nist.gov>
#                         W. Trevor King <wking@tremily.us>
#
# This file is part of igor.
#
# igor is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# igor is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with igor.  If not, see <http://www.gnu.org/licenses/>.

"igor: interface for reading binary IGOR files."

from distutils.core import setup
import os.path

from igor import __version__


package_name = 'igor'
_this_dir = os.path.dirname(__file__)

setup(name=package_name,
      version=__version__,
      maintainer='W. Trevor King',
      maintainer_email='wking@tremily.us',
      url='http://blog.tremily.us/posts/{}/'.format(package_name),
      download_url='http://git.tremily.us/?p={}.git;a=snapshot;h=v{};sf=tgz'.format(package_name, __version__),
      license='GNU Lesser General Public License v3 or later (LGPLv3+)',
      platforms=['all'],
      description=__doc__,
      long_description=open(os.path.join(_this_dir, 'README'), 'r').read(),
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      packages=[
        'igor',
        'igor.record',
        ],
      scripts=[
        'bin/igorbinarywave.py',
        'bin/igorpackedexperiment.py',
        ],
      provides=['igor ({})'.format(__version__)],
      )
