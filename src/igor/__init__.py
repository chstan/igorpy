# Copyright (C) 2012-2016 W. Trevor King <wking@tremily.us>
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

# Memo: there is a difference with igor2

"Interface for reading binary IGOR files."

__version__ = "0.3.2"

__all__ = ("__version__",)

import logging


LOG = logging.getLogger("igor")
LOG.setLevel(logging.ERROR)
LOG.addHandler(logging.StreamHandler())
LOG.handlers[-1].setFormatter(
    logging.Formatter("%(name)s - %(levelname)s - %(message)s")
)
