# As root

useradd -U almamgr
useradd -U almaproc
echo new2me | echo new2me | passwd --stdin almaproc

chmod 0705 /home/almamgr/
mkdir -p /home/almaproc/introot/
chown almaproc:almaproc /home/almaproc/introot/
chmod o+x /home/almamgr/ACS-2015.4/LGPL/acsBUILD/config/.acs/.bash_profile.acs
# Make binaries executable
for i in $( find /home/almamgr/ACS-current/LGPL/CommonSoftware/ -type d -name "bin" ); do chmod 0705 $i/*  ;done
for i in $( find /home/almamgr/ACS-current/LGPL/Kit/ -type d -name "bin" ); do chmod 0705 $i/*  ;done

# ln
ln -s /home/almamgr/ACS-2015.4 /home/almamgr/ACS-current
ln -s /home/almamgr /alma
# Autocomplete in usr local bin
for i in $( find /home/almamgr/ACS-current/LGPL/CommonSoftware/ -type d -name "bin" ); do ln -s $i/* /usr/local/bin/ ;done
for i in $( find /home/almamgr/ACS-current/LGPL/Kit/ -type d -name "bin" ); do ln -s $i/* /usr/local/bin/ ;done

# Shared Objects
for i in $( find /home/almamgr/ACS-current/LGPL/CommonSoftware/ -type f -name "*.so" ) ; do  ln -s $i /usr/local/lib64/ ; done

# Python Libs?
#PYTHONPATH="/alma/ACS-2015.4/ACSSW/lib/python/site-packages:/alma/ACS-2015.4/Python/omni/lib/python:/alma/ACS-2015.4/Python/omni/lib:/alma/ACS-2015.4/Python/lib/python/site-packages:/alma/ACS-2015.4/Python/omni/lib/python/site-packages:/alma/ACS-2015.4/Python/omni/lib64/python/site-packages
