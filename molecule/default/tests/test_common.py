import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('file, content', [
  ("/etc/automysqlbackup/automysqlbackup.conf", "Ansible managed"),
  ("/usr/local/bin/automysqlbackup", "AutoMySQLBackup version"),
  ("/etc/cron.d/ansible_automysqlbackup",
      "root /usr/local/bin/automysqlbackup")
])
def test_files(host, file, content):
    file = host.file(file)

    assert file.exists
    assert file.contains(content)
