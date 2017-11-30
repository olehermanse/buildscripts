#!/usr/bin/env python3

import sys
import argparse
import logging as log

def user_error(msg):
    log.error(msg)
    sys.exit(1)

def get_args():
    ap = argparse.ArgumentParser(description='Developer script for building CFEngine enterprise')
    
    # STEPS:
    ap.add_argument('--autogen', help='Run autogen step', action="store_true")
    ap.add_argument('--make',    help='Run make step',    action="store_true")
    ap.add_argument('--install', help='Run install step', action="store_true")
    ap.add_argument('--steps',   help='Steps (commands) to run', nargs='+')
    
    # REPOS:
    ap.add_argument('--core',       help='Add core to --repos',       action="store_true")
    ap.add_argument('--enterprise', help='Add enterprise to --repos', action="store_true")
    ap.add_argument('--nova',       help='Add nova to --repos',       action="store_true")
    ap.add_argument('--repos',      help='Repositories to run commands in', nargs='+')
    
    # LOGGING:
    ap.add_argument('--info',    help='Sets python loglevel to info',  action="store_true")
    ap.add_argument('--verbose', help='Sets python loglevel to debug', action="store_true")
    
    # BUILD TYPE:
    ap.add_argument('--debug',   help='Build in debug mode',   action="store_true")
    ap.add_argument('--release', help='Build in release mode', action="store_true")
    
    args = ap.parse_args()
    
    if args.info:
        log.setLevel(log.INFO)
    if args.verbose:
        log.setLevel(log.DEBUG)
    
    if not args.release and not args.debug:
        args.debug = True

    if not (args.steps or args.autogen or args.make or args.install):
        ap.print_help()
        user_error("No build steps specified")

    if not (args.repos or args.core or args.enterprise or args.nova):
        ap.print_help()
        user_error("No repos specified")


    return args

def main(args):
    pass

if __name__ == "__main__":
    log.setLevel(log.WARNING)
    args = get_args()
    main(args)