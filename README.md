Ansible Role: osx-command-line-tools
====================================

[![Build Status][travis-badge]][travis-link]
[![MIT licensed][mit-badge]][mit-link]
[![Galaxy Role][role-badge]][galaxy-link]

An ansible role that installs OS X Command Line Tools. Releases are hosted
on [Ansible Galaxy][galaxy-link].

Requirements
------------

None (except running on Mac OS X).

Role Variables
--------------

`force_install`: Install the Command Line Tools, even if they are already installed (Default: `no`).

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

1. Install [Virtualbox][vbox]
1. Install [Vagrant][vagrant]
1. Install `virtualenv`: `pip install -U virtualenv`

If you already have [Homebrew][homebrew] installed, you can use:

```bash
brew cask install virtualbox
brew cask install vagrant
```

Now you can setup your virtual environment for testing:

```bash
virtualenv --python=$(which python2.7) .venv
source .venv/bin/activate
pip install --no-deps -r test-requirements.txt
```

Run the full test suite against the default platform. The default platform is
`sierra`:

```bash
molecule test
```

Run the full test suite on a different platform:

```bash
molecule test --platform yosemite
```

License
-------

[MIT][mit-link]

Author Information
------------------

[Elliot Weiser](https://github.com/elliotweiser)

[galaxy-link]: https://galaxy.ansible.com/elliotweiser/osx-command-line-tools/
[homebrew]: http://brew.sh/
[mit-badge]: https://img.shields.io/badge/license-MIT-blue.svg
[mit-link]: https://raw.githubusercontent.com/elliotweiser/ansible-osx-command-line-tools/master/LICENSE
[role-badge]: https://img.shields.io/ansible/role/14481.svg
[travis-badge]: https://api.travis-ci.org/elliotweiser/ansible-osx-command-line-tools.svg?branch=master
[travis-link]: https://travis-ci.org/elliotweiser/ansible-osx-command-line-tools
[vagrant]: https://www.vagrantup.com/downloads.html
[vbox]: https://www.virtualbox.org/wiki/Downloads
