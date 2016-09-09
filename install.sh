# As root

useradd -U almamgr
useradd -U almaproc
echo new2me | echo new2me | passwd --stdin almaproc

yum install -y xz 
tar xJvf ACS-2015.4.tar.xz
mv ACS-2015.4 /home/almamgr/

chmod 0705 /home/almamgr/
chown -R almamgr. /home/almamgr/

mkdir -p /home/almaproc/introot/
chown almaproc:almaproc /home/almaproc/introot/
# Etc 
mkdir -p /etc/acscb/
cp /home/almamgr/ACS-2015.4/ACSSW/config/.acs/.bash_profile.acs /etc/acscb/bash_profile.acs.old
curl https://raw.githubusercontent.com/LeoXDXp/acs-rpm/master/SOURCES/bash_profile.acs -o /etc/acscb/bash_profile.acs
#chmod o+x /home/almamgr/ACS-2015.4/LGPL/acsBUILD/config/.acs/.bash_profile.acs

# Ln to /usr/local/bin/
ln -s /home/almamgr/ACS-2015.4/ACSSW/bin/* /usr/local/bin/

# ln
ln -s /home/almamgr/ACS-2015.4 /home/almamgr/ACS-current
ln -s /home/almamgr/ /alma

# Shared Objects
ln -s /home/almamgr/ACS-2015.4/ACSSW/lib/* /usr/local/lib64/
unlink /usr/local/lib64/python
# Libs in include
ln -s /home/almamgr/ACS-2015.4/ACSSW/include/* /usr/local/include/
# Share. It wont link the mans
ln -s /home/almamgr/ACS-2015.4/ACSSW/share/* /usr/local/share


# Python Libs?
#PYTHONPATH="/alma/ACS-2015.4/ACSSW/lib/python/site-packages:/alma/ACS-2015.4/Python/omni/lib/python:/alma/ACS-2015.4/Python/omni/lib:/alma/ACS-2015.4/Python/lib/python/site-packages:/alma/ACS-2015.4/Python/omni/lib/python/site-packages:/alma/ACS-2015.4/Python/omni/lib64/python/site-packages
