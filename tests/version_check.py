#!/usr/bin/env python2.7

import json
import requests
import sys
import yaml


def main(argv):
    '''
    Tests if all declared MacOSX versions in meta/main.yml are supported
    in Ansible Galaxy
    '''
    print "---> Checking meta/main.yml for unsupported platform versions"
    print
    meta = open("meta/main.yml")
    obj = yaml.safe_load(meta)
    meta.close()
    platforms = obj["galaxy_info"]["platforms"]
    macos = filter(lambda x: x["name"] == "MacOSX", platforms)
    declared_versions = set(macos[0]["versions"])
    url = 'https://galaxy.ansible.com/api/v1/platforms/?name=MacOSX'
    r = requests.get(url)
    json_obj = json.loads(r.text)
    allowed_versions = set(map(lambda x: str(x["release"]), json_obj['results']))

    print "ALLOWED:", list(allowed_versions)
    print
    print "DECLARED:", list(declared_versions)
    print

    if declared_versions.issubset(allowed_versions):
        print "All MacOS platform versions are supported in Ansible Galaxy"
        sys.exit(0)
    msg = "Error: meta/main.yml lists MacOSX versions that are currently "
    msg += "unsupported by Ansible Galaxy. Attempts to import this role "
    msg += "into Ansible Galaxy will fail...\n\n"
    msg += "Bad versions: " + str(list(declared_versions - allowed_versions))
    msg += "\n"
    sys.__stderr__.write(msg)
    sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)
