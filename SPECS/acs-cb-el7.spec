%define ALTVER 2016.10

Name:		ACS
Version:	OCT2016
Release:	1%{?dist}
Summary:	ACS CB for CentOS 7	
License:	LGPL
URL:		http://acs-community.github.io/
Source0:	%{name}-%{version}.tar.gz
Source1:	https://raw.githubusercontent.com/tmbdev/pylinda/master/linda/doc/pythfilter.py

BuildArch: x86_64 aarch64
# BuildRequires no acepta un grupo: Se agregan paquetes de Development tools por separado al final desde autoconf
# Packages
BuildRequires: ACS-ExtProds == %{ALTVER}
# Tools
# Hibernate provided in F24: http://rpms.remirepo.net/rpmphp/zoom.php?rpm=hibernate3
# astyle 1.15 - 2.05 in repos
# getopt in repos, check version
BuildRequires: gcc gcc-c++ emacs antlr expat expat-devel cppunit cppunit-devel swig loki-lib log4cpp shunit2 castor hibernate3

# ExtPy Module: PyXB: Required: 1.1.2. Repos: 1.2.4. 
# Pmw 1.2 vs 1.3.2: Only Change: In module PmwBase.py: An explicit cast is now required from exception to string (str) . http://pmw.sourceforge.net/doc/changes.html
# PyXML only available at acs-cb repo (repo.csrg.cl)
BuildRequires: rh-java-common-PyXB python-pmw == 1.3.2 pexpect PyXML
# Pychecker 0.8.14 vs 0.8.19. Changelog: http://pychecker.cvs.sourceforge.net/viewvc/pychecker/pychecker/?pathrev=HEAD
BuildRequires: pychecker

#BuildRequires: blas-devel expat-devel libX11-devel ncurses-devel readline gdbm gdbm-devel bzip2-devel zlib-devel sqlite-devel openssl-devel openldap-devel freetype-devel libpng-devel libxml2-devel libxslt-devel gsl-devel autoconf213 autoconf util-linux-ng unzip time log4cpp expat cppunit cppunit-devel swig xterm lpr ant centos-release asciidoc xmlto cvs openldap-devel bc ime rsync openssh-server autoconf automake binutils bison flex gcc gcc-c++ gettext gcc-gfortran make byacc patch libtool pkgconfig redhat-rpm-config rpm-build rpm-sign cscope ctags diffstat doxygen elfutils indent intltool patchutils rcs  swig systemtap xz libdb-devel

# In epel: log4cpp xemacs xemacs-packages-extra sqlite2-devel
# No existen en centos 7: perl-ExtUtils MakeMaker libncurses-devel ime libpng10-devel expat21
Requires: procmail lockfile-progs net-tools xterm man ACS-ExtProds == %{version}
# X Packages
Requires gnome-classic-session gnome-terminal nautilus-open-terminal control-center liberation-mono-fonts setroubleshoot-server glx-utils gdm openbox mesa-dri-drivers plymouth-system-theme spice-vdagent xorg-x11-drivers xorg-x11-server-Xorg xorg-x11-utils xorg-x11-xauth xorg-x11-xinit xvattr xorg-x11-drv-keyboard xorg-x11-drv-mouse 
Requires: gcc-c++ java-1.8.0-openjdk java-1.8.0-openjdk-devel java-1.8.0-openjdk-demo

%description
RPM Installer of ACS-CB %{version}. It takes the compiled files and installs it on /home/almamgr/. 

%prep
%setup -q

%build
# ALMASW_ROOTDIR, ALMASW_RELEASE, CLASSPATH and JAVA_HOME (OpenJDK 1.8) exported by ACS-ExtProd
# Env Vars for compilation
export ACSDATA="$ALMASW_ROOTDIR/$ALMASW_RELEASE/acsdata"
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export ACS_CDB="$ACSDATA/config/defaultCDB"
export ACS_INSTANCE="0"
export ACS_STARTUP_TIMEOUT_MULTIPLIER="2"
# hostname has to be short, or can be fqdn
export ACS_TMP="$ACSDATA/tmp/$HOSTNAME"
export IDL_PATH="-I$ACSROOT/idl -I/usr/src/debug/ACE_wrappers/TAO/orbsvcs/orbsvcs -I$TAO_ROOT/orbsvcs -I$TAO_ROOT -I/usr/include/orbsvcs -I/usr/include/tao"
#IDL_PATH="-I/alma/ACS-OCT2016/ACSSW/idl -I/alma/ACS-OCT2016/TAO/ACE_wrappers/build/linux/TAO/orbsvcs/orbsvcs -I/alma/ACS-OCT2016/TAO/ACE_wrappers/build/linux/TAO/orbsvcs -I/alma/ACS-OCT2016/TAO/ACE_wrappers/build/linux/TAO -I/alma/ACS-OCT2016/TAO/ACE_wrappers/build/linux/TAO/tao"
# DDS not added to LD PATH. Python, boost and omni all in lib64
export LD_LIBRARY_PATH="$ACSROOT/idl:/usr/lib64/:$ACSROOT/tcltk/lib"
#LD_LIBRARY_PATH="/alma/ACS-OCT2016/ACSSW/lib:/alma/ACS-OCT2016/DDS/build/linux/lib:/alma/ACS-OCT2016/TAO/ACE_wrappers/build/linux/lib:/alma/ACS-OCT2016/Python/lib:/alma/ACS-OCT2016/Python/omni/lib:/alma/ACS-OCT2016/boost/lib:/alma/ACS-OCT2016/tcltk/lib:"
# Compilation specific env vars
export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "
make

%install
# Env Vars for installing
export ACSDATA="$ALMASW_ROOTDIR/$ALMASW_RELEASE/acsdata"
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export ACS_CDB="$ACSDATA/config/defaultCDB"
export ACS_INSTANCE="0"
export ACS_STARTUP_TIMEOUT_MULTIPLIER="2"
# hostname has to be short, or can be fqdn
export ACS_TMP="$ACSDATA/tmp/$HOSTNAME"
export IDL_PATH="-I$ACSROOT/idl -I/usr/src/debug/ACE_wrappers/TAO/orbsvcs/orbsvcs -I$TAO_ROOT/orbsvcs -I$TAO_ROOT -I/usr/include/orbsvcs -I/usr/include/tao"
export LD_LIBRARY_PATH="$ACSROOT/idl:/usr/lib64/:$ACSROOT/tcltk/lib"

# Env Vars to profile.d
echo "ACSDATA=$ALMASW_ROOTDIR/$ALMASW_RELEASE/acsdata" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "ACSROOT=$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "ACS_CDB=$ACSDATA/config/defaultCDB" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh 
echo "ACS_INSTANCE=0" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "ACS_STARTUP_TIMEOUT_MULTIPLIER=2" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "ACS_TMP=$ACSDATA/tmp/$HOSTNAME" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo 'IDL_PATH="-I$ACSROOT/idl -I/usr/src/debug/ACE_wrappers/TAO/orbsvcs/orbsvcs -I$TAO_ROOT/orbsvcs -I$TAO_ROOT -I/usr/include/orbsvcs -I/usr/include/tao"' >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "LD_LIBRARY_PATH=$ACSROOT/idl:/usr/lib64/:$ACSROOT/tcltk/lib" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh

echo "export ACSDATA" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export ACSROOT" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export ACS_CDB" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh 
echo "export ACS_INSTANCE" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export ACS_STARTUP_TIMEOUT_MULTIPLIER" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export ACS_TMP" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export IDL_PATH" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export LD_LIBRARY_PATH" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh

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
# Place to create files for variable exporting on boot
mkdir -p %{buildroot}%{_sysconfdir}/profile.d/

ln -s %{buildroot}/home/almamgr %{buildroot}/alma
#Source0 ACSSW - acsdata
cp -r %{_builddir}%{name}-%{version}/    %{buildroot}/home/almamgr/
ln -s %{buildroot}/home/almamgr%{name}-%{version}/ %{buildroot}/home/almamgr%{name}-current/

cp -r %{buildroot}/home/almamgr%{name}-%{version}/acsdata/config/ %{buildroot}%{_sysconfdir}/acscb/
# Shared Objects
ln -s %{buildroot}/home/almamgr%{name}-%{version}/ACSSW/lib/* /usr/local/lib64/
# Every python lib is installed through pip, rpm or as a rpm source.
unlink /usr/local/lib64/python
# Pythfilter
install -m 0640 -D -p %{SOURCE1} %{buildroot}/home/almamgr%{name}-%{version}/ACSSW/bin/
#Binaries ln
ln -s %{buildroot}/home/almamgr%{name}-%{version}/ACSSW/bin/* /usr/local/bin/

#Libs in include. Seems there is no need for this
#ln -s %{buildroot}/home/almamgr%{name}-%{version}/ACSSW/include/* /usr/local/include/
# Mans
ln -s %{buildroot}/home/almamgr%{name}-%{version}/ACSSW/share/man/man1/* /usr/local/share/man/man1/
ln -s %{buildroot}/home/almamgr%{name}-%{version}/ACSSW/share/man/man3/* /usr/local/share/man/man3/
mkdir -p  %{buildroot}/home/almaproc/introot

# Destroy Symlink in buildroot
/usr/bin/unlink %{buildroot}/alma
%clean

%pre
useradd -U almaproc
echo new2me | echo new2me | passwd --stdin almaproc

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
systemctl enable acscb.service

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
systemctl enable acscbremote.service

systemctl daemon-reload

# Set SELinux Enforcing
sed -i 's/SELINUX=disabled/SELINUX=enforcing/g' %{_sysconfdir}/sysconfig/selinux
sed -i 's/SELINUX=permissive/SELINUX=enforcing/g' %{_sysconfdir}/sysconfig/selinux
setenforce 1

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
%config %{_sysconfdir}/systemd/system/acscb.service
%config %{_sysconfdir}/systemd/system/acscbremote.service
%config %{_sysconfdir}/acscb/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/ACSSW/bin/*
%attr(-,almaproc,almaproc)/home/almaproc/introot/
%{_usr}/local/bin/*
%{_usr}/local/lib/*
%doc %{_usr}/local/share/man/man*
%attr(0755,almagr,almamgr) %{_var}/run/acscb/

%changelog
* Mon Aug 19 2016 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
