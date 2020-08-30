# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.vm.hostname = "flask_python"
  config.ssh.insert_key = false
  config.vm.provider :libvirt do |l|
    l.memory = 2048
  end

  # Ansible provisioning
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "deploy/deploy.yml"
  end

end
