Name:		ACS Community Branch
Version:	2015.4
Release:	1%{?dist}
Summary:	ACS CB for CentOS 6	

License:	LGPL	
URL:		http://acs-community.github.io/
Source0:	http://acs-community.github.io/
Source1:        http://archive.eclipse.org/eclipse/downloads/drops/R-3.6.1-201009090800/eclipse-3.6.1-delta-pack.zip
Source2:        http://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/R-4.2.2-201302041200/eclipse-4.2.2-delta-pack.zip
Source3:        http://archive.eclipse.org/eclipse/downloads/drops/R-3.6.1-201009090800/eclipse-SDK-3.6.1-linux-gtk-x86_64.tar.gz
Source4:        http://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/R-4.2.2-201302041200/eclipse-SDK-4.2.2-linux-gtk-x86_64.tar.gz
Source5:        http://www.jacorb.org/releases/3.6/jacorb-3.6-source.zip

BuildRequires:	java-1.8.0-openjdk java-1.8.0-openjdk-devel java-1.8.0-openjdk-demo ksh blas-devel gcc expat-devel gcc gcc-c++ gcc-gfortran make byacc patch vim subversion libX11-devel ncurses-devel readline gdbm gdbm-devel bzip2-devel zlib-devel sqlite-devel sqlite2-devel openssl-devel openldap-devel freetype-devel libpng-devel libpng10-devel libxml2-devel libxslt-devel gsl-devel flex xemacs xemacs-packages-extra doxygen autoconf213 autoconf util-linux-ng unzip time procmail log4cpp expat expat21 cppunit cppunit-devel swig castor castor-xml castor-demo shunit2 lockfile-progs xterm lpr ant centos-release
Requires: lockfile-progs	

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%clean


%pre
# Install epel-maven repo
curl -O https://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -o /etc/yum.repos.d/epel-apache-maven.repo

# ACE-TAO RPM from OpenSUSE
echo "
[ace-tao_opensuse]
name=ACE+TAO RPMS for CentOS_CentOS-6
type=rpm-md
baseurl=http://download.opensuse.org/repositories/devel:/libraries:/ACE:/micro/CentOS_CentOS-6/
gpgcheck=1
gpgkey=http://download.opensuse.org/repositories/devel:/libraries:/ACE:/micro/CentOS_CentOS-6/repodata/repomd.xml.key
enabled=0
" > /etc/yum.repos.d/ace-tao.repo

# Local users
useradd -U almamgr
useradd -U almaproc
echo new2me | echo new2me | passwd --stdin almaproc
mkdir -p /home/almaproc/introot/
chown almaproc:almaproc /home/almaproc/introot/
echo 'export INTROOT="/home/almaproc/introot/" '


%post
# Create SysV service
echo "
#!/bin/bash
#
# chkconfig: 35 90 12
# description: ACS CB Daemon
#
# Get function from functions library
. /etc/init.d/functions
# Start the service ACS
start() {
        initlog -c "echo -n Starting FOO server: "
        /path/to/FOO &
        ### Create the lock file ###
        touch /var/lock/subsys/FOO
        success $"FOO server startup"
        echo
}
# Restart the service FOO
stop() {
        initlog -c "echo -n Stopping FOO server: "
        killproc FOO
        ### Now, delete the lock file ###
        rm -f /var/lock/subsys/FOO
        echo
}

### main logic ###
case "$1" in
  start)
        start
        ;;
  stop)
        stop
        ;;
  status)
        acs
        ;;
  restart|reload|condrestart)
        stop
        start
        ;;
  *)
        echo $"Usage: $0 {start|stop|restart|reload|status}"
        exit 1
esac
exit 0

" > 

%files
%doc



%changelog

