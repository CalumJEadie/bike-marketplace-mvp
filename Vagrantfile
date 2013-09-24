VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # 32 bit Ubuntu 12.04
  config.vm.box = "precise32"
  config.vm.box_url = "http://files.vagrantup.com/precise32.box"

  config.vm.network "public_network"

  config.vm.provision :shell, :path => "vagrant/bootstrap.sh"
end
