#!/usr/bin/env python2.7
# encoding: utf-8
'''
extract_features -- extract planning instance and domain features

extract_features is a script to extract scalar features from
a given PDDL planning instance and domain, using several component
extractors.

@author:     Chris Fawcett
@copyright:  TBD
@license:    TBD

@contact:    fawcettc@cs.ubc.ca
'''

import sys
import os
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from subprocess import Popen, PIPE
import shutil

__version__ = 0.1
__authors__ = 'Chris Fawcett'
__date__ = '2013-11-15'
__updated__ = '2015-11-15'

__default_mem_limit__ = 6144
__default_per_extraction_time_limit__ = 1800

if __name__ == "__main__":
    program_version = "v%s" % __version__
    program_update_date = str(__updated__)
    program_msg = "%%(prog)s %s (%s)" % (program_version, program_update_date)
    program_shortmsg = __import__("__main__").__doc__.split("\n")[1]
    program_license = '''%s
        Created by %s on %s.
        Copyright 2015 - TBD INSERT COPYRIGHT INFO. All rights reserved.

        Licensed under TBD INSERT LICENSE INFO

        LPG, Fast Downward, Torchlight and runsolver appear with permission from their
        respective authors, with their own licenses. Please see the respective
        source folders for that information.

        Distributed on an "AS IS" basis without warranties or conditions
        of any kind, either express or implied.

        USAGE
    ''' % (program_shortmsg, str(__authors__), str(__date__))

    abs_script_directory = os.path.abspath(os.path.dirname(sys.argv[0]))

    parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter, add_help=True)

    parser.add_argument("--runsolver-path", dest="runsolver", default=abs_script_directory+"/runsolver/runsolver", help="path to the runsolver binary (used for enforcing runtime and memory limits)")
    parser.add_argument("--mem-limit", dest="mem_limit", default=__default_mem_limit__, type=int, help="memory limit for extraction, in MiB")
    parser.add_argument("--per-extraction-time-limit", dest="per_extraction_time_limit", default=__default_per_extraction_time_limit__, type=float, help="CPU time limit for each component feature extraction, in seconds")

    parser.add_argument("--domain-file", dest="domain_file", default=None, type=str, help="PDDL domain file for feature extraction")
    parser.add_argument("--instance-file", dest="instance_file", default=None, type=str, help="PDDL instance file for feature extraction")

    parser.add_argument("--no-csv-header", dest="csv_header", action='store_false', help="Do not print the CSV header line")
    parser.set_defaults(csv_header=True)

    args = parser.parse_args(sys.argv[1:])

    # check to make sure the domain and instance exist
    if os.path.exists(args.domain_file):
        domain_file = os.path.abspath(args.domain_file)
    else:
        print "ERROR: Domain file %s does not exist!" % args.domain_file
        sys.exit(1)

    if os.path.exists(args.instance_file):
        instance_file = os.path.abspath(args.instance_file)
    else:
        print "ERROR: Instance file %s does not exist!" % args.instance_file
        sys.exit(1)

    sys.exit(0)