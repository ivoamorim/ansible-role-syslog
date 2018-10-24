import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('distro, pkg', [
    ('centos,debian,ubuntu', 'rsyslog'),
])
def test_packages_are_installed(host, distro, pkg):
    if host.system_info.distribution not in distro:
        pytest.skip("skipping unmatch distribution")
    package = host.package(pkg)
    assert package.is_installed


@pytest.mark.parametrize('distro, svc', [
    ('centos,debian,ubuntu', 'rsyslog'),
])
def test_rsyslog_is_running(host, distro, svc):
    if host.system_info.distribution not in distro:
        pytest.skip("skipping unmatch distribution")
    service = host.service(svc)
    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize('distro, conf', [
    ('centos,debian,ubuntu', '/etc/rsyslog.conf'),
    ('centos,debian,ubuntu', '/etc/rsyslog.d/default.conf'),
])
def test_configuration_files_are_existed(host, distro, conf):
    if host.system_info.distribution not in distro:
        pytest.skip("skipping unmatch distribution")
    file = host.file(conf)
    assert file.exists
    cmd = 'rsyslogd -N 1 -f ' + conf
    result = host.run(cmd)
    assert result.rc == 0
