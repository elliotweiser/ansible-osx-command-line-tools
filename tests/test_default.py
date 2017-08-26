import re


def test_tmp_file_is_gone(host):
    tmp_file = 'tmp/.com.apple.dt.CommandLineTools.installondemand.in-progress'
    f = host.file(tmp_file)
    assert not f.exists


def test_command_line_tools_dir(host):
    f = host.file('/Library/Developer/CommandLineTools')
    assert f.exists
    assert f.is_directory
    assert f.user == 'root'
    assert f.group == 'admin'
    assert f.mode == 0o755


def test_clt_package_metadata(host):
    c = host.command('pkgutil --pkg-info=com.apple.pkg.CLTools_Executables')
    assert c.rc == 0


def test_git_is_useable(host):
    c = host.command('/usr/bin/git --version')
    assert c.rc == 0
    assert re.match('^git version \d+(.\d+)* \(Apple Git-\d+\)$', c.stdout)
