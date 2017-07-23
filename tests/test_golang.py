import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_binary_file_exists(File):
    f = File("/usr/local/go/bin/go")

    assert f.exists
    assert f.is_file


def test_go_version(host):
    result = host.run("/usr/local/go/bin/go version")

    assert result.rc == 0
    assert "go version go1.8.3 linux/amd64" in result.stdout


def test_profile(host):
    file = host.file("/root/.profile")

    assert file.exists
    assert file.is_file
    assert file.contains("export PATH=/usr/local/go/bin:$PATH")
    assert file.user == "root"
    assert file.group == "root"
