%define ALTVER 2016.10

Name:		ACS
Version:	OCT2016
Release:	1%{?dist}
Summary:	ACS CB for CentOS 7	
License:	LGPL
URL:		http://acs-community.github.io/
Source0:	%{name}-%{version}.tar.gz

BuildArch: x86_64 aarch64
# BuildRequires no acepta un grupo: Se agregan paquetes de Development tools por separado al final desde autoconf
# Packages
BuildRequires: ACS-ExtProds == %{version}
BuildRequires: gcc gcc-c++ emacs antlr expat expat-devel cppunit cppunit-devel swig loki-lib log4cpp shunit2 castor 

# ExtPy Module: PyXB: Required: 1.1.2. Repos: 1.2.4. 
# Pmw 1.2 vs 1.3.2
BuildRequires: rh-java-common-PyXB python-pmw pexpect  
#BuildRequires: blas-devel expat-devel libX11-devel ncurses-devel readline gdbm gdbm-devel bzip2-devel zlib-devel sqlite-devel openssl-devel openldap-devel freetype-devel libpng-devel libxml2-devel libxslt-devel gsl-devel autoconf213 autoconf util-linux-ng unzip time log4cpp expat cppunit cppunit-devel swig xterm lpr ant centos-release asciidoc xmlto cvs openldap-devel bc ime rsync openssh-server autoconf automake binutils bison flex gcc gcc-c++ gettext gcc-gfortran make byacc patch libtool pkgconfig redhat-rpm-config rpm-build rpm-sign cscope ctags diffstat doxygen elfutils indent intltool patchutils rcs  swig systemtap xz libdb-devel


# In epel: log4cpp xemacs xemacs-packages-extra sqlite2-devel
# No existen en centos 7: perl-ExtUtils MakeMaker libncurses-devel ime libpng10-devel expat21
# Desglose de paquetes de X Window System desde glx-utils hasta xorg-x11-drv-mouse
Requires: procmail lockfile-progs gnome-classic-session gnome-terminal nautilus-open-terminal control-center liberation-mono-fonts setroubleshoot-server glx-utils gdm openbox mesa-dri-drivers plymouth-system-theme spice-vdagent xorg-x11-drivers xorg-x11-server-Xorg xorg-x11-utils xorg-x11-xauth xorg-x11-xinit xvattr xorg-x11-drv-keyboard xorg-x11-drv-mouse gcc-c++ java-1.8.0-openjdk java-1.8.0-openjdk-devel java-1.8.0-openjdk-demo man xterm ACS-ExtProds == %{version}


%description
RPM Installer of ACS-CB %{version}. It takes the compiled files and installs it on /home/almamgr/ (symlink to /alma). 

%prep
%setup -q

%build
export ALMASW_ROOTDIR="%{buildroot}/alma"
export ALMASW_RELEASE="ACS-%{version}"

%install
mkdir -p  %{buildroot}/home/almamgr
# /usr/local
mkdir -p %{buildroot}%{_usr}/local/bin/
mkdir -p %{buildroot}%{_usr}/local/lib64/
mkdir -p %{buildroot}%{_usr}/local/include/
mkdir -p %{buildroot}%{_usr}/local/share/
# /var/run/
mkdir -p %{buildroot}%{_var}/run/acscb/
# /etc
mkdir -p %{buildroot}%{_sysconfdir}/acscb/
#mkdir -p %{_usr}/lib64/python2.7/site-packages/
# Place to create files for variable exporting on boot
mkdir -p %{buildroot}%{_sysconfdir}/profile.d/

ln -s %{buildroot}/home/almamgr %{buildroot}/alma
#Source0 ACSSW - acsdata
cp -r %{_builddir}%{name}-%{version}/    %{buildroot}/home/almamgr/
ln -s %{buildroot}/home/almamgr%{name}-%{version}/ %{buildroot}/home/almamgr%{name}-current/
#cp %{buildroot}/home/almamgr%{name}-%{version}/LGPL/acsBUILD/config/.acs/.bash_profile.acs %{buildroot}%{_sysconfdir}/acs/bash_profile.acs.old
cp -r %{buildroot}/home/almamgr%{name}-%{version}/acsdata/config/ %{buildroot}%{_sysconfdir}/acscb/
#Binaries ln
ln -s %{buildroot}/home/almamgr%{name}-%{version}/ACSSW/bin/* /usr/local/bin/
# Shared Objects
ln -s %{buildroot}/home/almamgr%{name}-%{version}/ACSSW/lib/* /usr/local/lib64/
unlink /usr/local/lib64/python
#Python Libs

# Libs in include
ln -s %{buildroot}/home/almamgr%{name}-%{version}/ACSSW/include/* /usr/local/include/
# Mans
#ln -s %{buildroot}/home/almamgr/%{name}-%{version}/ACSSW/man/* /usr/local/share/man/*
# Shared
ln -s %{buildroot}/home/almamgr%{name}-%{version}/ACSSW/share/aclocal /usr/local/share/
ln -s %{buildroot}/home/almamgr%{name}-%{version}/ACSSW/share/antlr-2.7.7 /usr/local/share/
ln -s %{buildroot}/home/almamgr%{name}-%{version}/ACSSW/share/doc /usr/local/share/
ln -s %{buildroot}/home/almamgr%{name}-%{version}/ACSSW/share/swig /usr/local/share/
ln -s %{buildroot}/home/almamgr%{name}-%{version}/ACSSW/share/man/man1/* /usr/local/share/man/man1/
ln -s %{buildroot}/home/almamgr%{name}-%{version}/ACSSW/share/man/man3/* /usr/local/share/man/man3/
mkdir -p  %{buildroot}/home/almaproc/introot
%clean

%pre
useradd -U almaproc
echo new2me | echo new2me | passwd --stdin almaproc

echo "
[opensuse-13.2]
name=Opensuse 13.2
baseurl=http://download.opensuse.org/distribution/13.2/repo/oss/suse/
gpgcheck=0
gpgkey=http://download.opensuse.org/repositories/devel:/libraries:/ACE:/micro/CentOS_7//repodata/repomd.xml.key
enabled=0
" >> /etc/yum.repos.d/opensuse-13.2.repo

%post
# Permissions
chown -R almamgr:almamgr /home/almamgr/
chown almamgr:almamgr %{_var}/run/acscb/
chown almaproc:almaproc /home/almaproc/introot/

# Create systemd services
echo "
[Unit]
Description=ACS Core Service
#Documentation=man:sshd(8) man:sshd_config(5)
After=multi-user.target

[Service]
Type=forking
Environment=INTROOT='/home/almaproc/introot/'
EnvironmentFile=-/etc/acs/bash_profile.acs
User=almamgr
ExecPreStart=killACS -q
ExecStart=acsStart
ExecStop=acsStop && acsdataClean --all
ExecReload=cdbjDALClearCache
KillMode=process
#Restart=on-failure
#RestartSec=10s

[Install]
WantedBy=multi-user.target

" > %{_sysconfdir}/systemd/system/acscb.service
#systemctl enable acscb.service

echo "
[Unit]
Description=ACS Remote Management Daemon
#Documentation=man:sshd(8) man:sshd_config(5)
After=multi-user.target

[Service]
Type=forking
Environment=INTROOT='/home/almaproc/introot/'
# EnvFile to later be a conf file
EnvironmentFile=-/etc/acs/bash_profile.acs
User=almamgr
#ExecPreStart=killACS -q
ExecStart=acsdaemonStartAcs
ExecStop=acsdaemonStopAcs && acsdataClean --all
ExecReload=cdbjDALClearCache
KillMode=process
#Restart=on-failure
#RestartSec=10s

[Install]
WantedBy=multi-user.target

" > %{_sysconfdir}/systemd/system/acscbremote.service
#systemctl enable acscbremote.service

#systemctl daemon-reload

# Set SELinux PERMISSIVE (Audit mode)
sed -i 's/SELINUX=disabled/SELINUX=permissive/g' %{_sysconfdir}/sysconfig/selinux
sed -i 's/SELINUX=enforcing/SELINUX=permissive/g' %{_sysconfdir}/sysconfig/selinux
setenforce 0

# /etc/hosts
#echo "" >> /etc/hosts

%preun
systemctl stop acscb.service
systemctl disable acscb.service
 
%postun
systemctl daemon-reload
# Al user processes must be killed before userdel
pkill -u almaproc
pkill -u almamgr
userdel -r almamgr
userdel -r almaproc

%files
# find CommonSoftware/ -type d -name "bin" -exec chmod -R +x {} \;
# find Kit/ -type d -name "bin" -exec chmod -R +x {} \;
%doc
%config %{_sysconfdir}/systemd/system/acscb.service
%config %{_sysconfdir}/acs/bash_profile.acs
%attr(0705,almagr,almamgr) /home/almamgr/ 
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/ACSSW/bin/*
%attr(-,almaproc,almaproc)/home/almaproc/introot/
%{_usr}/local/bin/*
#%{_usr}/local/lib/*
#%{_usr}/lib64/python2.7/site-packages/
%{_var}/run/acscb/

%changelog
* Mon Aug 19 2016 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
