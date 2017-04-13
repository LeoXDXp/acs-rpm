%define ALTVER FEB2017

Name:		ACS-Tools-Kit-Benchmark
Version:	2017.02
Release:	1%{?dist}
Summary:	ACS CB Tools and Kit Module for CentOS 7	
License:	LGPL
URL:		http://acs-community.github.io/
Source0:	%{name}-%{version}.tar.gz 
# Modified Makefile to compile only Tools, Kit and Benchmark
Source1:	Makefile-TKB

BuildArch: x86_64 aarch64
# BuildRequires no acepta un grupo: Se agregan paquetes de Development tools por separado al final desde autoconf
BuildRequires: ACS-ExtProds >= %{version} ACS-ExtJars >= %{version}
# Tools: Hibernate provided in F24: http://rpms.remirepo.net/rpmphp/zoom.php?rpm=hibernate3
# astyle 1.15 - 2.05 in repos
# getopt in repos, check version. Only needed by Sun OS, Ignoring.
# xsd-doc seems to be different than xsddoc (part of xframe)
BuildRequires: gcc gcc-c++ emacs antlr expat expat-devel cppunit cppunit-devel swig loki-lib log4cpp shunit2 castor hibernate3 xerces-c xerces-c-devel xerces-j2 
# Consoles that should be unified
BuildRequires: ksh time
# ExtPy Module: PyXB: Required: 1.1.2. Repos: 1.2.4. 
# Pmw 1.2 vs 1.3.2: Only Change: In module PmwBase.py: An explicit cast is now required from exception to string (str) . http://pmw.sourceforge.net/doc/changes.html
# PyXML only available at acs-cb repo (repo.csrg.cl)
BuildRequires: rh-java-common-PyXB python-pmw == 1.3.2 pexpect PyXML
# Pychecker 0.8.14 vs 0.8.19. Changelog: http://pychecker.cvs.sourceforge.net/viewvc/pychecker/pychecker/?pathrev=HEAD
BuildRequires: pychecker
# Other java packages requires. Such as ExtJars
BuildRequires: apache-commons-lang junit javassist geronimo-jta mockito mysql-connector-java objenesis xmlunit
BuildRequires: procmail tkinter

# In epel: log4cpp xemacs xemacs-packages-extra sqlite2-devel
# No existen en centos 7: perl-ExtUtils MakeMaker libncurses-devel time libpng10-devel expat21
Requires: procmail python-lockfile net-tools xterm man ACS-ExtProds >= %{version} tkinter
Requires: apache-commons-lang junit
# X Packages
Requires: gnome-classic-session gnome-terminal nautilus-open-terminal control-center liberation-mono-fonts setroubleshoot-server glx-utils gdm openbox mesa-dri-drivers plymouth-system-theme spice-vdagent xorg-x11-drivers xorg-x11-server-Xorg xorg-x11-utils xorg-x11-xauth xorg-x11-xinit xvattr xorg-x11-drv-keyboard xorg-x11-drv-mouse
Requires: gcc-c++ java-1.8.0-openjdk java-1.8.0-openjdk-devel java-1.8.0-openjdk-demo

%description
RPM Installer of ACS-CB Tools and Kit %{version}. Installs ACS CB Tools and Kit modules in /home/almamgr/ACS-%{version}/ACSSW/, leaving env vars in profile.d and commands symlinked to /usr/local/bin avoiding sourcing of .bash_profile.acs file. It also creates acsdata.

%package devel
Summary: ACS CB Benchmark files for {?dist} 
License: LGPL
#Requires: ACS-ExtProds >= %{version}

%description devel
Source files to compile ACS CB Tools, Kit and Benchmark %{version} for {?dist}

%prep
%setup -q
%build
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/Makefile

%install
# Basic paths and symlinks
mkdir -p  %{buildroot}/home/almamgr
ln -s %{buildroot}/home/almamgr %{buildroot}/alma
# Env Vars for installing. 
export ALMASW_ROOTDIR=%{buildroot}/alma
export ALMASW_RELEASE=ACS-%{version}
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
export LD_LIBRARY_PATH="$ACSROOT/idl:/usr/lib64/:$ACSROOT/tcltk/lib:/usr/local/lib64:/usr/local/lib"
#LD_LIBRARY_PATH="/alma/ACS-OCT2016/ACSSW/lib:/alma/ACS-OCT2016/DDS/build/linux/lib:/alma/ACS-OCT2016/TAO/ACE_wrappers/build/linux/lib:/alma/ACS-OCT2016/Python/lib:/alma/ACS-OCT2016/Python/omni/lib:/alma/ACS-OCT2016/boost/lib:/alma/ACS-OCT2016/tcltk/lib:"
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk
export GNU_ROOT=%{_usr}
export TCLTK_ROOT="/alma/ACS-%{version}/tcltk"
export PYTHONPATH="/usr/lib64/python2.7/site-packages:/usr/lib/python2.7/site-packages:/opt/rh/rh-java-common/root/usr/lib/python2.7/site-packages/:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/xmlpybind/lib/python/site-packages:%{buildroot}/home/almamgr/ACS-%{version}/ACSSW/lib/python/site-packages:%{_usr}/local/lib/python/site-packages/"
export PYTHON_ROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/Python"
export PYTHONINC="/usr/include/python2.7"
# PYTHONPATH="/alma/ACS-OCT2016/ACSSW/lib/python/site-packages:/alma/ACS-OCT2016/Python/omni/lib/python:/alma/ACS-OCT2016/Python/omni/lib:/alma/ACS-OCT2016/Python/lib/python2.7/site-packages:/alma/ACS-OCT2016/Python/omni/lib/python/site-packages:/alma/ACS-OCT2016/Python/omni/lib64/python2.7/site-packages"
export PATH="$PATH:/alma/ACS-%{version}/tcltk/bin:/alma/ACS-%{version}/JacORB/bin:$GNU_ROOT/bin:/alma/ACS-%{version}/ACSSW/bin"
# PATH="/alma/ACS-OCT2016/Python/bin:/alma/ACS-OCT2016/ACSSW/bin:/usr/java/default/bin:/alma/ACS-OCT2016/ant/bin:/alma/ACS-OCT2016/JacORB/bin:/alma/ACS-OCT2016/Python/bin:/alma/ACS-OCT2016/maven/bin:/alma/ACS-OCT2016/Python/omni/bin:/alma/ACS-OCT2016/tcltk/bin:/usr/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/acs.node/.local/bin:/home/acs.node/bin"
# Calling Mico, JacORB, ACE+TAO , MPC, Maven env vars PENDING OmniORB 2 paths, Extend PATH, python_root path, manpath , gnu_root maybe?
source %{_sysconfdir}/profile.d/mico.sh
source %{_sysconfdir}/profile.d/jacorb.sh
source %{_sysconfdir}/profile.d/ant.sh
source %{_sysconfdir}/profile.d/ace-devel.sh # overrides ACE_ROOT
source %{_sysconfdir}/profile.d/apache-maven.sh
source %{_sysconfdir}/profile.d/mpc.sh
source %{_sysconfdir}/profile.d/tao-devel.sh

# Temp CLASSPATH for xsddoc and extidl
export CLASSPATH="/usr/share/java/:/usr/share/local/java/:/usr/share/java/ant.jar:/usr/share/java/xalan-j2.jar:%{buildroot}/home/almamgr/ACS-%{version}/ACSSW/lib/Monitor_Types.jar"
# Compilation specific env vars
export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

cd %{_builddir}/%{name}-%{version}/
# mkdir of ACSSW
mkdir -p %{buildroot}/home/almamgr/ACS-%{version}/ACSSW/
# Symlink of Python's compilelall for hardcoded path in make files
mkdir -p %{buildroot}/home/almamgr/ACS-%{version}/Python/lib/python2.7/
ln -s %{_usr}/%{_lib}/python2.7/compileall.py %{buildroot}/home/almamgr/ACS-%{version}/Python/lib/python2.7/compileall.py

make

# Devel folders: RPM, LGPL, Benchmark
mkdir -p  %{buildroot}/home/almadevel/
mv %{_builddir}/%{name}-%{version}/LGPL/ %{buildroot}/home/almadevel/
mv %{_builddir}/%{name}-%{version}/Benchmark/ %{buildroot}/home/almadevel/
mv %{_builddir}/%{name}-%{version}/RPM/ %{buildroot}/home/almadevel/RPM-legacy/

# Env Vars to profile.d
mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
export ALMASW_ROOTDIR="/alma"
echo "ACSDATA=$ALMASW_ROOTDIR/ACS-%{version}/acsdata" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "ACSROOT=$ALMASW_ROOTDIR/ACS-%{version}/ACSSW" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "ACS_CDB=$ALMASW_ROOTDIR/ACS-%{version}/config/defaultCDB" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh 
echo "ACS_INSTANCE=0" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "ACS_STARTUP_TIMEOUT_MULTIPLIER=2" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "ACS_TMP=$ALMASW_ROOTDIR/ACS-%{version}/tmp/$HOSTNAME" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo 'IDL_PATH="-I$ACSROOT/idl -I/usr/src/debug/ACE_wrappers/TAO/orbsvcs/orbsvcs -I$TAO_ROOT/orbsvcs -I$TAO_ROOT -I/usr/include/orbsvcs -I/usr/include/tao"' >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "LD_LIBRARY_PATH=$ALMASW_ROOTDIR/ACS-%{version}/idl:/usr/lib64/:$ALMASW_ROOTDIR/ACS-%{version}/tcltk/lib" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "GNU_ROOT=%{_usr}" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-gnu.sh
echo "TCLTK_ROOT=$ALMASW_ROOTDIR/$ALMASW_RELEASE/tcltk" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-tcltk.sh
echo "PYTHONPATH=/usr/lib64/python2.7/site-packages:/opt/rh/rh-java-common/root/usr/lib/python2.7/site-packages/:%{_usr}/local/lib/python/site-packages/:$ALMASW_ROOTDIR/ACS-%{version}/ACSSW/lib/python/site-packages/" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-python.sh
echo "PYTHON_ROOT=$ALMASW_ROOTDIR/ACS-%{version}/Python" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-python.sh
echo 'PYTHONINC=/usr/include/python2.7' >> %{buildroot}%{_sysconfdir}/profile.d/acscb-python.sh

echo 'PATH="$PATH:/alma/ACS-%{version}/tctlk/bin:/alma/ACS-%{version}/JacORB/bin:$GNU_ROOT/bin:/alma/ACS-%{version}/ACSSW/bin"' >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh

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
echo "export PYTHONINC" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-python.sh
echo "export PATH" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh

#mkdir -p %{buildroot}%{_usr}/local/bin/
#Symlink Libs in include. Very useful when building, because it's in gcc's default path
mkdir -p %{buildroot}%{_usr}/local/include/
#ln -s %{buildroot}/home/almamgrACS-%{version}/ACSSW/include/* %{buildroot}%{_usr}/local/include/

# Move ACS Mans to here
mkdir -p %{buildroot}%{_usr}/local/share/
#mv %{buildroot}/home/almamgr/ACS-%{version}/ACSSW/share/man/man1/ %{buildroot}%{_usr}/local/share/man/
#mv %{buildroot}/home/almamgr/ACS-%{version}/ACSSW/share/man/man3/ %{buildroot}%{_usr}/local/share/man/

# /var/run/
mkdir -p %{buildroot}%{_var}/run/acscb/
# /etc. Hoping to have acsdata only on etc in the future
mkdir -p %{buildroot}%{_sysconfdir}/acscb/
cp -r %{buildroot}/home/almamgr/ACS-%{version}/acsdata/config/ %{buildroot}%{_sysconfdir}/acscb/
# Place to create files for variable exporting on boot
mkdir -p %{buildroot}%{_sysconfdir}/profile.d/

# Remove objects
cd %{buildroot}/alma/ACS-%{version}/ACSSW/
find -name "*.o" | xargs rm -rf

# Destroy Symlink in buildroot
%{_usr}/bin/unlink %{buildroot}/alma
%{_usr}/bin/unlink %{buildroot}/home/almamgr/ACS-%{version}/Python/lib/python2.7/compileall.py

%clean

%pre
useradd -U almaproc
echo new2me | echo new2me | passwd --stdin almaproc

%pre devel
useradd -U almadevel

%post
# Permissions
chown -R almamgr:almamgr /home/almamgr/
chown almamgr:almamgr %{_var}/run/acscb/
chown almaproc:almaproc /home/almaproc/introot/
mkdir -p /home/almamgr/ACS-%{version}/Python/lib/python2.7/
ln -s %{_usr}/%{_lib}/python2.7/compileall.py /home/almamgr/ACS-%{version}/Python/lib/python2.7/compileall.py
ln -s /home/almamgr/ACS-%{version}/ /home/almamgr/%{ALTVER}
ln -s /home/almamgr/ACS-%{version}/ /home/almamgr/ACS-latest

%preun
 
%postun
# Al user processes must be killed before userdel
pkill -u almaproc
userdel -r almaproc

%postun devel
pkill -u almadevel
userdel -r almadevel

%files
# ACSSW, acsdata, READMEs, LICENSE, ACS_VERSION, ACS_PATCH_LEVEL
%config %{_sysconfdir}/acscb/
%attr(0705,almamgr,almamgr) /home/almamgr/ACS-%{version}/ACSSW/
%attr(0705,almamgr,almamgr) /home/almamgr/ACS-%{version}/ACSSW/bin/
%attr(0705,almamgr,almamgr) /home/almamgr/ACS-%{version}/acsdata/
%{_usr}/local/bin
%{_usr}/local/lib
%docdir %{_usr}/local/share/man/
%{_usr}/local/share/man/
%attr(0755,almamgr,almamgr) %{_var}/run/acscb/

%files devel
# LGPL, Benchmark, RPM-legacy
%attr(0705,almadevel,almadevel) /home/almadevel/

%changelog
* Fri Aug 19 2016 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
