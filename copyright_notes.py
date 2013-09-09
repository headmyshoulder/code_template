#!/usr/bin/env python


no_copyright = ""
no_copyright_for_header = " *"
no_copyright_for_python = " #"

boost_copyright =  """Distributed under the Boost Software License, Version 1.0.
(See accompanying file LICENSE_1_0.txt or
copy at http://www.boost.org/LICENSE_1_0.txt)"""
    
boost_copyright_for_header = """ * Distributed under the Boost Software License, Version 1.0.
 * (See accompanying file LICENSE_1_0.txt or
 * copy at http://www.boost.org/LICENSE_1_0.txt)"""

boost_copyright_for_python = """# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE_1_0.txt or
# copy at http://www.boost.org/LICENSE_1_0.txt)"""


copyrights = { "no" : no_copyright , "boost" : boost_copyright }
copyright_for_header = { "no" : no_copyright_for_header , "boost" : boost_copyright_for_header }
copyright_for_python = { "no" : no_copyright_for_python , "boost" : boost_copyright_for_python }