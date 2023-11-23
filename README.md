Request data: Call python microservice.py <CRN> from command line.
Receive data: After correctly entering a valid CRN, prerequisite will be returned in the form of a CSV file.

Example call: python microservice.py 72109

Will return:

CRN,Registration Restrictions
72109,"""<p class=\""prereq\"">Prerequisites: <a href=\""/search/?p=CS%20162\"" data-action=\""result-detail\"" data-group=\""code:CS 162\"" >CS 162</a> or <a href=\""/search/?p=CS%20165\"" data-action=\""result-detail\"" data-group=\""code:CS 165\""  class=\""notoffered\"">165</a>.<br/>A minimum grade of C is required in <a href=\""/search/?p=CS%20162\"" data-action=\""result-detail\"" data-group=\""code:CS 162\"" >CS 162</a> and <a href=\""/search/?p=CS%20165\"" data-action=\""result-detail\"" data-group=\""code:CS 165\""  class=\""notoffered\"">CS 165</a>.</p><p class=\""maj\"">Enrollment is limited to students with a program in Computer Science (307).</p><p class=\""col\"">Enrollment limited to students in the College of Engineering college.</p>"""
