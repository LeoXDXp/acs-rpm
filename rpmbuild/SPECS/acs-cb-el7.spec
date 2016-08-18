Name:		ACS Community Branch
Version:	2015.4
Release:	1%{?dist}
Summary:	ACS CB for CentOS 7	

Group:		
License:	
URL:		
#Source0:	http://acs-community.github.io/
Source0:	ACS-%{version}-x86_64.tar.gz
#Source1:	http://archive.eclipse.org/eclipse/downloads/drops/R-3.6.1-201009090800/eclipse-3.6.1-delta-pack.zip
#Source2:	http://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/R-4.2.2-201302041200/eclipse-4.2.2-delta-pack.zip	
#Source3:	http://archive.eclipse.org/eclipse/downloads/drops/R-3.6.1-201009090800/eclipse-SDK-3.6.1-linux-gtk-x86_64.tar.gz
#Source4:	http://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/R-4.2.2-201302041200/eclipse-SDK-4.2.2-linux-gtk-x86_64.tar.gz
#Source5:	http://www.jacorb.org/releases/3.6/jacorb-3.6-source.zip

BuildRequires:	java-1.8.0-openjdk java-1.8.0-openjdk-devel java-1.8.0-openjdk-demo ksh blas-devel gcc expat-devel gcc gcc-c++ gcc-gfortran make byacc patch vim subversion libX11-devel ncurses-devel readline gdbm gdbm-devel bzip2-devel zlib-devel sqlite-devel sqlite2-devel openssl-devel openldap-devel freetype-devel libpng-devel libpng10-devel libxml2-devel libxslt-devel gsl-devel flex xemacs xemacs-packages-extra doxygen autoconf213 autoconf util-linux-ng unzip time procmail log4cpp expat expat21 cppunit cppunit-devel swig castor castor-xml castor-demo shunit2 lockfile-progs xterm lpr ant centos-release
Requires: lockfile-progs "X Window System" gnome-classic-session gnome-terminal nautilus-open-terminal control-center liberation-mono-fonts setroubleshoot-server 

%description
RPM Installer of ACS-CB 2015.4. It takes the compiled files and installs it on /home/almamgr/ (symlink to /alma). 

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
#%make_install
mkdir -p  %{buildroot}/home/almamgr
ln -s %{buildroot}/home/almamgr %{buildroot}/alma
cp -r %{_builddir}/%{name}-%{version}/    %{buildroot}/home/almamgr/
%clean


%pre
# Install epel-maven repo
curl -O https://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -o /etc/yum.repos.d/epel-apache-maven.repo

# ACE-TAO RPM from OpenSUSE
echo "
[ace-tao_opensuse]
name=Latest ACE micro release (CentOS_7)
type=rpm-md
baseurl=http://download.opensuse.org/repositories/devel:/libraries:/ACE:/micro/CentOS_7/
gpgcheck=1
gpgkey=http://download.opensuse.org/repositories/devel:/libraries:/ACE:/micro/CentOS_7//repodata/repomd.xml.key
enabled=1
" > /etc/yum.repos.d/ace-tao.repo

#Local users
useradd -U almamgr
useradd -U almaproc
echo new2me | echo new2me | passwd --stdin almaproc
chown almaproc:almaproc /home/almaproc/introot/


%post
# Create systemd service
echo "
[Unit]
Description=Alma Common Software CB Service
Documentation=man:sshd(8) man:sshd_config(5)
After=multi-user.target

[Service]
Type=forking
PIDFile=/var/run/sshd.pid
Environment=INTROOT='/home/almaproc/introot/'
EnvironmentFile=-/alma/..../.bash_profile.acs
User=almamgr
ExecStart=/usr/sbin/sshd $OPTIONS
ExecReload=/bin/kill -HUP $MAINPID
KillMode=process
Restart=on-failure
RestartSec=42s

[Install]
WantedBy=multi-user.target

" > /etc/systemd/system/acscb.service
systemctl enable acscb.service
systemctl daemon-reload

# Set SELinux PERMISSIVE (Audit mode)
sed -i 's/SELINUX=disabled/SELINUX=permissive/g' %{_sysconfdir}/sysconfig/selinux
sed -i 's/SELINUX=enforcing/SELINUX=permissive/g' %{_sysconfdir}/sysconfig/selinux
setenforce 0
%files
%doc
/home/almamgr
/home/almaproc/introot/
%{_sysconfdir}/


%changelog

