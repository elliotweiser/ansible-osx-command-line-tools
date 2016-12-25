Ansible Role: osx-command-line-tools
====================================

An ansible that installs OS X Command Line Tools.
README test

Requirements
------------

None (except running on Mac OS X).

Role Variables
--------------

None.

Dependencies
------------

None.

Example Playbook
----------------

A simple playbook example:

    - hosts: servers
      roles:
         - { role: elliotweiser.osx-command-line-tools }


Testing Instructions
--------------------

1. Install [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
1. Install [Vagrant](https://www.vagrantup.com/downloads.html)
1. Install `virtualenv`: `pip install -U virtualenv`

If you already have [Homebrew](http://brew.sh/) installed, you can use:

```bash
brew cask install virtualbox
brew cask install vagrant
```

Now you can setup your virtual environment for testing:

```bash
virtualenv --python=$(which python2.7) .venv
source .venv/bin/activate
pip install -r test-requirements.txt
```

Use `molecule` commands for testing.

License
-------

MIT

Author Information
------------------

[Elliot Weiser](https://github.com/elliotweiser)
