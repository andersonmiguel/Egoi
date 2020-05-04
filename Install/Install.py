#Instaladores
%sh

#Install python
cd /usr/src

sudo wget https://www.python.org/ftp/python/2.7.16/Python-2.7.16.tgz

sudo tar xzf Python-2.7.16.tgz

cd Python-2.7.16
sudo ./configure --enable-optimizations
sudo make altinstall

#Install API
pip install --upgrade pip

pip install git+https://github.com/E-goi/sdk-python.git

sudo easy_install soappy

sudo easy_install xmlrpclib

#Install PyODBC
pip3 install --upgrade pyodbc
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get -q -y install msodbcsql17
sudo apt autoremove
apt-get install curl
apt-get install apt-transport-https
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee /etc/apt/sources.list.d/msprod.list
apt-get update
ACCEPT_EULA=y DEBIAN_FRONTEND=noninteractive
apt-get install mssql-tools unixodbc-dev -y
