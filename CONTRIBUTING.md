Contributing Guidelines
=======================

Contributions are welcome. Open a [pull-request][link-pr] to this repository to
submit your code change.

Bug Reports and Feature Requests
--------------------------------

Please [open an issue][link-issue] describing _in detail_ the bug you observed
or the feature you wish to see implemented. For bug reports, it helps to know
versions of the following items:

* _This_ project (supply a tag or revision)
* Ansible
* MacOS

Development and Testing
-----------------------

Unless otherwise specified, pull-requests will not be merged unless the CI build
passes. For developing and testing this project on your system, follow the
instructions below to get started.

1. Install [VirtualBox][link-vbox] (including the VirtualBox Extension Pack)
1. Install [Vagrant][link-vagrant]
1. Install `virtualenv`: `pip install -U virtualenv`

If you already have [Homebrew][link-homebrew] installed, you can use:

```bash
brew cask install virtualbox
brew cask install virtualbox-extension-pack
brew cask install vagrant
```

Now you can setup your virtual environment for testing:

```bash
virtualenv --python=$(which python2.7) .venv
source .venv/bin/activate
pip install --no-deps -r tests/test-requirements.txt
```

Run the full lifecycle test on a given `<PLATFORM>`. Allowed values for
`<PLATFORM>` are `highsierra`, `sierra`, `elcapitan`, and `yosemite`.

```bash
source molecule/<PLATFORM>.sh
molecule test
```

Unset the `MOLECULE_` environment variables:

```bash
source molecule/unset.sh
```

What if I just have a question?
-------------------------------

For now, feel free to [open an issue][link-issue]. I'll do my best to answer in
a timely fashion.

[link-homebrew]: http://brew.sh/
[link-issue]: https://github.com/elliotweiser/ansible-osx-command-line-tools/issues/new
[link-pr]: https://github.com/elliotweiser/ansible-osx-command-line-tools/compare?expand=1
[link-vagrant]: https://www.vagrantup.com/downloads.html
[link-vbox]: https://www.virtualbox.org/wiki/Downloads
