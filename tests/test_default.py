import re


def test_tmp_file_is_gone(File):
    f = File('/tmp/.com.apple.dt.CommandLineTools.installondemand.in-progress')
    assert not f.exists


def test_command_line_tools_dir(File):
    f = File('/Library/Developer/CommandLineTools')
    assert f.exists
    assert f.is_directory
    assert f.user == 'root'
    assert f.group == 'admin'
    assert f.mode == 0o755


def test_xcode_select_print_path(Command):
    c = Command('xcode-select -print-path')
    assert c.rc == 0
    assert c.stdout == '/Library/Developer/CommandLineTools'


def test_git_is_useable(Command):
    c = Command('/usr/bin/git --version')
    assert c.rc == 0
    assert re.match('^git version \d+(.\d+)* \(Apple Git-\d+\)$', c.stdout)
