#%define ALTVER 2016.10

Name:		ACS
Version:	2016.10
Release:	1%{?dist}
Summary:	ACS CB for CentOS 7	
License:	LGPL
URL:		http://acs-community.github.io/
Source0:	%{name}-%{version}.tar.gz 
Source1:	https://raw.githubusercontent.com/tmbdev/pylinda/master/linda/doc/pythfilter.py

BuildArch: x86_64 aarch64
# BuildRequires no acepta un grupo: Se agregan paquetes de Development tools por separado al final desde autoconf
BuildRequires: ACS-ExtProds >= %{version}
# Tools: Hibernate provided in F24: http://rpms.remirepo.net/rpmphp/zoom.php?rpm=hibernate3
# astyle 1.15 - 2.05 in repos
# getopt in repos, check version
BuildRequires: gcc gcc-c++ emacs antlr expat expat-devel cppunit cppunit-devel swig loki-lib log4cpp shunit2 castor hibernate3
# Consoles that should be unified
BuildRequires: ksh
BuildRequires: time 
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
Requires: gnome-classic-session gnome-terminal nautilus-open-terminal control-center liberation-mono-fonts setroubleshoot-server glx-utils gdm openbox mesa-dri-drivers plymouth-system-theme spice-vdagent xorg-x11-drivers xorg-x11-server-Xorg xorg-x11-utils xorg-x11-xauth xorg-x11-xinit xvattr xorg-x11-drv-keyboard xorg-x11-drv-mouse
Requires: gcc-c++ java-1.8.0-openjdk java-1.8.0-openjdk-devel java-1.8.0-openjdk-demo

%description
RPM Installer of ACS-CB %{version}. Installs ACS CB in /home/almamgr/, leaving env vars in profile.d and commands symlinked to /usr/local/bin avoiding sourcing of .bash_profile.acs file. 

%package devel
Summary: ACS CB Benchmark files for {?dist} 
License: LGPL
Requires: ACS-ExtProds >= %{version}

%description devel
Source files to compile ACS CB %{version} for {?dist}

%prep
%setup -q
%build
# Replace LGPL/Tools/extpy/src/Pythfilter  with SOURCE1 pythfilter.
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/LGPL/Tools/extpy/src/

%install
# Basic paths and symlinks
mkdir -p  %{buildroot}/home/almamgr
ln -s %{buildroot}/home/almamgr %{buildroot}/alma
ln -s %{buildroot}/home/almamgr/%{name}-%{version} %{buildroot}/home/almamgr/%{name}-current
# Env Vars for installing. 
export ALMASW_ROOTDIR=%{buildroot}/alma
export ALMASW_RELEASE=%{name}-%{version}
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
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk
export GNU_ROOT=%{_usr}
export TCLTK_ROOT="/alma/%{name}-%{version}/tctlk"
export PYTHONPATH="/usr/lib64/python2.7/site-packages"
export PYTHON_ROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/Python"
# PYTHONPATH="/alma/ACS-OCT2016/ACSSW/lib/python/site-packages:/alma/ACS-OCT2016/Python/omni/lib/python:/alma/ACS-OCT2016/Python/omni/lib:/alma/ACS-OCT2016/Python/lib/python2.7/site-packages:/alma/ACS-OCT2016/Python/omni/lib/python/site-packages:/alma/ACS-OCT2016/Python/omni/lib64/python2.7/site-packages"
#export PATH="$PATH:/alma/%{name}-%{version}/tctlk/bin:/alma/%{name}-%{version}/JacORB/bin:/alma/%{name}-%{version}/ACSSW/bin:%{buildroot}/home/almamgr/%{name}-%{version}/LGPL/Kit/acs/bin/"
# PATH="/alma/ACS-OCT2016/Python/bin:/alma/ACS-OCT2016/ACSSW/bin:/usr/java/default/bin:/alma/ACS-OCT2016/ant/bin:/alma/ACS-OCT2016/JacORB/bin:/alma/ACS-OCT2016/Python/bin:/alma/ACS-OCT2016/maven/bin:/alma/ACS-OCT2016/Python/omni/bin:/alma/ACS-OCT2016/tcltk/bin:/usr/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/acs.node/.local/bin:/home/acs.node/bin"
# Calling Mico, JacORB, ACE+TAO , MPC, Maven env vars PENDING OmniORB 2 paths, Extend PATH, python_root path, manpath , gnu_root maybe?
sh %{_sysconfdir}/profile.d/mico.sh
sh %{_sysconfdir}/profile.d/jacorb.sh
sh %{_sysconfdir}/profile.d/ant.sh
sh %{_sysconfdir}/profile.d/ace-devel.sh # overrides ACE_ROOT
sh %{_sysconfdir}/profile.d/apache-maven.sh
sh %{_sysconfdir}/profile.d/mpc.sh
sh %{_sysconfdir}/profile.d/tao-devel.sh


# Compilation specific env vars
export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

cd %{_builddir}/%{name}-%{version}/
# mkdir of ACSSW
mkdir -p %{buildroot}/home/almamgr/%{name}-%{version}/ACSSW/
# Symlink of Python's compilelall for hardcoded path in make files
mkdir -p %{buildroot}/home/almamgr/%{name}-%{version}/Python/lib/python2.7/
ln -s %{_usr}/%{_lib}/python2.7/compileall.py %{buildroot}/home/almamgr/%{name}-%{version}/Python/lib/python2.7/compileall.py
# make of LGPL, creates ACSSW and acsdata in buildroot. Benchmark also has 2 products
make
#make install #DESTDIR=%{buildroot}

# Env Vars to profile.d
mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
export ALMASW_ROOTDIR="/alma"
echo "ACSDATA=$ALMASW_ROOTDIR/$ALMASW_RELEASE/acsdata" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "ACSROOT=$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "ACS_CDB=$ACSDATA/config/defaultCDB" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh 
echo "ACS_INSTANCE=0" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "ACS_STARTUP_TIMEOUT_MULTIPLIER=2" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "ACS_TMP=$ACSDATA/tmp/$HOSTNAME" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo 'IDL_PATH="-I$ACSROOT/idl -I/usr/src/debug/ACE_wrappers/TAO/orbsvcs/orbsvcs -I$TAO_ROOT/orbsvcs -I$TAO_ROOT -I/usr/include/orbsvcs -I/usr/include/tao"' >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "LD_LIBRARY_PATH=$ACSROOT/idl:/usr/lib64/:$ACSROOT/tcltk/lib" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "GNU_ROOT=%{_usr}" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-gnu.sh
echo "TCLTK_ROOT=$ALMASW_ROOTDIR/$ALMASW_RELEASE/tcltk" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-tcltk.sh
echo 'PYTHONPATH="/usr/lib64/python2.7/site-packages"' >> %{buildroot}%{_sysconfdir}/profile.d/acscb-python.sh
echo 'PYTHON_ROOT=%{buildroot}/$ALMASW_ROOTDIR/$ALMASW_RELEASE/Python' >> %{buildroot}%{_sysconfdir}/profile.d/acscb-python.sh
echo 'PATH="$PATH:/alma/%{name}-%{version}/tctlk/bin:/alma/%{name}-%{version}/JacORB/bin"' >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh

echo "export ACSDATA" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export ACSROOT" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export ACS_CDB" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh 
echo "export ACS_INSTANCE" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export ACS_STARTUP_TIMEOUT_MULTIPLIER" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export ACS_TMP" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export IDL_PATH" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export LD_LIBRARY_PATH" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export GNU_ROOT" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-gnu.sh
echo "export TCLTK_ROOT" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-tcltk.sh
echo "export PYTHONPATH" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-python.sh
echo "export PYTHON_ROOT" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-python.sh
echo "export PATH" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh

# /usr/local. Symlink binaries to here. Not needed due to extended PATH
#mkdir -p %{buildroot}%{_usr}/local/bin/
#ln -s %{buildroot}/home/almamgr/%{name}-%{version}/ACSSW/bin/* %{buildroot}%{_usr}/local/bin/

# Symlink Shared Objects to lib64, except python. Every python lib is installed through pip, rpm or as a rpm source.
#mkdir -p %{buildroot}%{_usr}/local/lib64/
#ln -s %{buildroot}/home/almamgr/%{name}-%{version}/ACSSW/lib/* %{buildroot}%{_usr}/local/lib64/
#unlink {buildroot}%{_usr}/local/lib64/python
#Symlink Libs in include. Seems there is no need for this
#mkdir -p %{buildroot}%{_usr}/local/include/
#ln -s %{buildroot}/home/almamgr%{name}-%{version}/ACSSW/include/* %{buildroot}%{_usr}/local/include/

# Move ACS Mans to here
mkdir -p %{buildroot}%{_usr}/local/share/
mv %{buildroot}/home/almamgr/%{name}-%{version}/ACSSW/share/man/man1/ %{buildroot}%{_usr}/local/share/man/
mv %{buildroot}/home/almamgr/%{name}-%{version}/ACSSW/share/man/man3/ %{buildroot}%{_usr}/local/share/man/
# Documentation
mkdir -p %{buildroot}%{_usr}/local/acscb/
mv %{_builddir}/%{name}-%{version}/README* %{buildroot}%{_usr}/local/acscb/
mv %{_builddir}/%{name}-%{version}/LICENSE.md %{buildroot}%{_usr}/local/acscb/
mv %{_builddir}/%{name}-%{version}/ACS_* %{buildroot}%{_usr}/local/acscb/
mv %{_builddir}/%{name}-%{version}/Documents/ %{buildroot}%{_usr}/local/acscb/
# /var/run/
mkdir -p %{buildroot}%{_var}/run/acscb/
# /etc. Hoping to have acsdata only on etc in the future
mkdir -p %{buildroot}%{_sysconfdir}/acscb/
cp -r %{buildroot}/home/almamgr/%{name}-%{version}/acsdata/config/ %{buildroot}%{_sysconfdir}/acscb/
# Place to create files for variable exporting on boot
mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
# Introot for development
mkdir -p  %{buildroot}/home/almaproc/introot
# Destroy Symlink in buildroot
%{_usr}/bin/unlink %{buildroot}/alma
%{_usr}/bin/unlink %{buildroot}/home/almamgr/%{name}-current
%{_usr}/bin/unlink %{buildroot}/home/almamgr/%{name}-%{version}/Python/lib/python2.7/compileall.py
# Devel folders: RPM, Makefile, LGPL, Benchmark
mkdir -p  %{buildroot}/home/almaproc/acscb-devel/
mv %{_builddir}/%{name}-%{version}/Makefile %{buildroot}/home/almaproc/acscb-devel/
mv %{_builddir}/%{name}-%{version}/LGPL/ %{buildroot}/home/almaproc/acscb-devel/
mv %{_builddir}/%{name}-%{version}/Benchmark/ %{buildroot}/home/almaproc/acscb-devel/
mv %{_builddir}/%{name}-%{version}/RPM/ %{buildroot}/home/almaproc/acscb-devel/

%clean

%pre
useradd -U almaproc
echo new2me | echo new2me | passwd --stdin almaproc

%post
# Permissions
chown -R almamgr:almamgr /home/almamgr/
chown almamgr:almamgr %{_var}/run/acscb/
chown almaproc:almaproc /home/almaproc/introot/
mkdir -p /home/almamgr/%{name}-%{version}/Python/lib/python2.7/
ln -s %{_usr}/%{_lib}/python2.7/compileall.py /home/almamgr/%{name}-%{version}/Python/lib/python2.7/compileall.py


# Create systemd services
echo "
[Unit]
Description=ACS Core Service
#Documentation=man:sshd(8) man:sshd_config(5)
After=multi-user.target

[Service]
Type=forking
Environment=INTROOT='/home/almaproc/introot/'
#EnvironmentFile=-/etc/acs/bash_profile.acs
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
#EnvironmentFile=-/etc/acs/bash_profile.acs
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
# ACSSW, acsdata, READMEs, LICENSE, ACS_VERSION, ACS_PATCH_LEVEL
%config %{_sysconfdir}/systemd/system/acscb.service
%config %{_sysconfdir}/systemd/system/acscbremote.service
%config %{_sysconfdir}/acscb/
%attr(0705,almamgr,almamgr) /home/almamgr/%{name}-%{version}/ACSSW/
%attr(0705,almamgr,almamgr) /home/almamgr/%{name}-%{version}/ACSSW/bin/
%attr(0705,almamgr,almamgr) /home/almamgr/%{name}-%{version}/acsdata/
%attr(-,almaproc,almaproc)/home/almaproc/introot/
#%{_usr}/local/bin/
#%{_usr}/local/lib/
%license /home/almamgr/%{name}-%{version}/LICENSE.md
%docdir %{_usr}/local/share/man/
%{_usr}/local/share/man/
%docdir %{_usr}/local/acscb/
%{_usr}/local/acscb/
%attr(0755,almamgr,almamgr) %{_var}/run/acscb/

%files devel
# LGPL, Benchmark, Makefile, RPM
%attr(0705,almaproc,almaproc) /home/almaproc/acscb-devel/

%changelog
* Fri Aug 19 2016 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
