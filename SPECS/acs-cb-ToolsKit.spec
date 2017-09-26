%define ALTVER JUN2017

Name:		ACS-Tools-Kit-Benchmark
Version:	2017.06
Release:	1%{?dist}
Summary:	ACS CB Tools and Kit Module for CentOS 7	
License:	LGPL
URL:		http://acs-community.github.io/
Source0:	%{name}-%{version}.tar.gz 
# Modified Makefile to compile only Tools, Kit and Benchmark
Source1:	Makefile-TKB

# BuildRequires no acepta un grupo: Se agregan paquetes de Development tools por separado al final desde autoconf
BuildRequires: ACS-ExtProds >= %{version} ACS-ExtJars >= %{version} ACS-eclipse-plugins >= %{version}
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
Requires: procmail python-lockfile net-tools xterm man ACS-ExtProds >= %{version} tkinter ACS-eclipse-plugins >= %{version}
Requires: apache-commons-lang junit
# X Packages: nautilus-open-terminal not yet in EL7
Requires: gnome-classic-session gnome-terminal control-center liberation-mono-fonts setroubleshoot-server glx-utils gdm openbox mesa-dri-drivers plymouth-system-theme spice-vdagent xorg-x11-drivers xorg-x11-server-Xorg xorg-x11-utils xorg-x11-xauth xorg-x11-xinit xvattr xorg-x11-drv-keyboard xorg-x11-drv-mouse
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
# Basic paths and symlinks
mkdir -p  %{_builddir}/home/almamgr
ln -s %{_builddir}/home/almamgr %{_builddir}/alma
# Env Vars for installing. 
export ALMASW_ROOTDIR=%{_builddir}/alma
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

export LD_LIBRARY_PATH="$ACSROOT/idl:%{_usr}/%{_lib}/:%{_usr}/local/%{_lib}"
#LD_LIBRARY_PATH="/alma/ACS-OCT2016/ACSSW/lib:/alma/ACS-OCT2016/DDS/build/linux/lib:/alma/ACS-OCT2016/TAO/ACE_wrappers/build/linux/lib:/alma/ACS-OCT2016/Python/lib:/alma/ACS-OCT2016/Python/omni/lib:/alma/ACS-OCT2016/boost/lib:/alma/ACS-OCT2016/tcltk/lib:"
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk
export GNU_ROOT=%{_usr}
export PYTHONPATH="$PYTHONPATH:/usr/lib/python2.7/site-packages:/opt/rh/rh-java-common/root/usr/lib/python2.7/site-packages/:%{_builddir}/home/almamgr/ACS-%{version}/ACSSW/lib/python/site-packages:%{_usr}/local/lib/python/site-packages/"
export PYTHON_ROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/Python"
export PYTHONINC="/usr/include/python2.7"
# Calling Mico, JacORB, ACE+TAO , MPC, Maven env vars PENDING OmniORB 2 paths, Extend PATH, python_root path, manpath , gnu_root maybe?
source %{_sysconfdir}/profile.d/tcltk-acs.sh
source %{_sysconfdir}/profile.d/mico-acs.sh
source %{_sysconfdir}/profile.d/jacorb-acs.sh
source %{_sysconfdir}/profile.d/ant.sh
source %{_sysconfdir}/profile.d/ace-devel.sh # overrides ACE_ROOT
source %{_sysconfdir}/profile.d/apache-maven.sh
source %{_sysconfdir}/profile.d/mpc.sh
source %{_sysconfdir}/profile.d/tao-devel.sh

export PATH="$PATH:/alma/ACS-%{version}/ACSSW/bin:%{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src:"

# Temp CLASSPATH for xsddoc and extidl
export CLASSPATH="/usr/share/java/:/usr/local/share/java/:/usr/share/java/ant.jar:/usr/share/java/xalan-j2.jar:%{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/lib/Monitor_Types.jar:%{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/lib/Monitor.jar:%{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/lib/NotificationServiceMC.jar:/usr/local/share/JacORB/lib/jacorb-services-3.6.1.jar:%{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/lib/NotifyExt.jar"
# Compilation specific env vars
export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

# Fixing/replacing searchFile
#tat xsddoc extidl vtd-xml oAW scxml_apache
tempbdir=$( echo %{_builddir} | sed 's/\//\\\//g' )
#sed -i 's/$(shell searchFile include\/acsMakefile)//g'  %{_builddir}/%{name}-%{version}/LGPL/Tools/tat/src/Makefile
sed -i "s/\$(MAKEDIR)\/acsMakefile/$tempbdir\/%{name}-%{version}\/LGPL\/Kit\/acs\/include\/acsMakefile/g" %{_builddir}/%{name}-%{version}/LGPL/Kit/doc/src/Makefile
sed -i "s/\$(MAKEDIR)\/acsMakefile/$tempbdir\/%{name}-%{version}\/LGPL\/Kit\/acs\/include\/acsMakefile/g" %{_builddir}/%{name}-%{version}/LGPL/Kit/acstempl/src/Makefile
sed -i "s/\$(MAKEDIR)\/acsMakefile/$tempbdir\/%{name}-%{version}\/LGPL\/Kit\/acs\/include\/acsMakefile/g" %{_builddir}/%{name}-%{version}/LGPL/Kit/acsutilpy/src/Makefile

sed -i "s/\$(MAKEDIR)\/acsMakefile/$tempbdir\/%{name}-%{version}\/LGPL\/Kit\/acs\/include\/acsMakefile/g" %{_builddir}/%{name}-%{version}/LGPL/Tools/tat/src/Makefile
sed -i "s/\$(MAKEDIR)\/acsMakefile/$tempbdir\/%{name}-%{version}\/LGPL\/Kit\/acs\/include\/acsMakefile/g" %{_builddir}/%{name}-%{version}/LGPL/Tools/xsddoc/src/Makefile
sed -i "s/\$(MAKEDIR)\/acsMakefile/$tempbdir\/%{name}-%{version}\/LGPL\/Kit\/acs\/include\/acsMakefile/g" %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/src/Makefile
sed -i "s/\$(MAKEDIR)\/acsMakefile/$tempbdir\/%{name}-%{version}\/LGPL\/Kit\/acs\/include\/acsMakefile/g" %{_builddir}/%{name}-%{version}/LGPL/Tools/vtd-xml/src/Makefile
sed -i "s/\$(MAKEDIR)\/acsMakefile/$tempbdir\/%{name}-%{version}\/LGPL\/Kit\/acs\/include\/acsMakefile/g" %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/src/Makefile
sed -i "s/\$(MAKEDIR)\/acsMakefile/$tempbdir\/%{name}-%{version}\/LGPL\/Kit\/acs\/include\/acsMakefile/g" %{_builddir}/%{name}-%{version}/LGPL/Tools/scxml_apache/src/Makefile

# extidl makefiles
#sed -i 's/$(shell searchFile include\/acsMakefile)//g'  %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/src/Makefile.c++
#sed -i "s/\$(MAKEDIR)\/acsMakefile/$tempbdir\/%{name}-%{version}\/LGPL\/Kit\/acs\/include\/acsMakefile/g" %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/src/Makefile.c++
#sed -i 's/$(shell searchFile include\/acsMakefile)//g'  %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/src/Makefile.java
#sed -i "s/\$(MAKEDIR)\/acsMakefile/$tempbdir\/%{name}-%{version}\/LGPL\/Kit\/acs\/include\/acsMakefile/g" %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/src/Makefile.java
#sed -i 's/$(shell searchFile include\/acsMakefile)//g'  %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/src/Makefile.python
#sed -i "s/\$(MAKEDIR)\/acsMakefile/$tempbdir\/%{name}-%{version}\/LGPL\/Kit\/acs\/include\/acsMakefile/g" %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/src/Makefile.python

#sed -i 's/$(OMNI_ROOT)\/idl\//$(OMNI_ROOT)/g' %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/src/Makefile.python
#sed -i 's/$(OMNI_IDL)/\/usr\/bin\/omniidl/g' %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/src/Makefile.python
#sed -i "s/ -bacs_python/ -p $tempbdir\/%{name}-%{version}\/LGPL\/Tools\/extpy\/src\/ -bacs_python/g" %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/src/Makefile.python

# Temporary for debugging
sed -i 's/tat xsddoc extidl vtd-xml oAW scxml_apache/extidl/g' %{_builddir}/%{name}-%{version}/LGPL/Tools/Makefile
#acsBuild searchfile fix
sed -i "s/\$(MAKEDIR)\/acsMakefile/$tempbdir\/%{name}-%{version}\/LGPL\/Kit\/acs\/include\/acsMakefile $tempbdir\/%{name}-%{version}\/LGPL\/Kit\/acs\/include\/acsMakefileCore.mk $tempbdir\/%{name}-%{version}\/LGPL\/Kit\/acs\/include\/acsMakefileDefinitions.mk  /g" %{_builddir}/%{name}-%{version}/LGPL/acsBUILD/src/Makefile

# Temporary for debugging
#sed -i 's/tat xsddoc extidl vtd-xml oAW scxml_apache/extidl/g' %{_builddir}/%{name}-%{version}/LGPL/Tools/Makefile

cd %{_builddir}/%{name}-%{version}/
# mkdir of ACSSW
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/
# Symlink of Python's compilelall for hardcoded path in make files
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/Python/lib/python2.7/
ln -s %{_usr}/%{_lib}/python2.7/compileall.py %{_builddir}/home/almamgr/ACS-%{version}/Python/lib/python2.7/compileall.py

make

#Manual creation of extidl jars
#cd %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/idl
#ln -s  /usr/include/tao/ tao
#idlj Monitor_Types.idl
#idlj Monitor.idl
#idlj NotificationServiceMC.idl
#NotifyExt
#idlj -i /usr/include/orbsvcs NotifyExt.idl
#idlj NotifyMonitoringExt.idl

# Destroy Symlink in buildroot
%{_usr}/bin/unlink %{_builddir}/home/almamgr/ACS-%{version}/Python/lib/python2.7/compileall.py

# Remove objects
cd %{_builddir}/alma/ACS-%{version}/ACSSW/
find -name "*.o" | xargs rm -rf

%install
# Copy {_builddir}/home/almamgr/ to %{buildroot}/home/almamgr/
mkdir -p  %{buildroot}/home/almamgr/ACS-%{version}/
cp -r %{_builddir}/home/almamgr/ACS-%{version}/ACSSW %{buildroot}/home/almamgr/ACS-%{version}/
cp -r %{_builddir}/home/almamgr/ACS-%{version}/acsdata %{buildroot}/home/almamgr/ACS-%{version}/
mv %{_builddir}/%{name}-%{version}/README* %{buildroot}/home/almamgr/ACS-%{version}/
mv %{_builddir}/%{name}-%{version}/LICENSE* %{buildroot}/home/almamgr/ACS-%{version}/
mv %{_builddir}/%{name}-%{version}/ACS_* %{buildroot}/home/almamgr/ACS-%{version}/

# /etc. Hoping to have acsdata only on etc in the future
mkdir -p %{buildroot}%{_sysconfdir}/acscb/
cp -r %{_builddir}/home/almamgr/ACS-%{version}/acsdata/config/ %{buildroot}%{_sysconfdir}/acscb/

# Devel folders: RPM, LGPL, Benchmark
mkdir -p  %{buildroot}/home/almadevel/
mv %{_builddir}/%{name}-%{version}/LGPL/ %{buildroot}/home/almadevel/
mv %{_builddir}/%{name}-%{version}/Benchmark/ %{buildroot}/home/almadevel/
mv %{_builddir}/%{name}-%{version}/RPM/ %{buildroot}/home/almadevel/RPM-legacy/

# Env Vars to profile.d. Place to create files for variable exporting on boot
mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
export ALMASW_ROOTDIR="/alma"
echo "ACSDATA=$ALMASW_ROOTDIR/ACS-%{version}/acsdata" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "ACSROOT=$ALMASW_ROOTDIR/ACS-%{version}/ACSSW" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "ACS_CDB=$ALMASW_ROOTDIR/ACS-%{version}/config/defaultCDB" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh 
echo "ACS_INSTANCE=0" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "ACS_STARTUP_TIMEOUT_MULTIPLIER=2" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "ACS_TMP=$ALMASW_ROOTDIR/ACS-%{version}/tmp/$HOSTNAME" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo 'IDL_PATH="-I$ACSROOT/idl -I/usr/src/debug/ACE_wrappers/TAO/orbsvcs/orbsvcs -I$TAO_ROOT/orbsvcs -I$TAO_ROOT -I/usr/include/orbsvcs -I/usr/include/tao"' >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ALMASW_ROOTDIR/ACS-%{version}/idl:/usr/lib64/:" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "GNU_ROOT=%{_usr}" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-gnu.sh
echo "PYTHONPATH=/usr/lib64/python2.7/site-packages:/opt/rh/rh-java-common/root/usr/lib/python2.7/site-packages/:%{_usr}/local/lib/python/site-packages/:$ALMASW_ROOTDIR/ACS-%{version}/ACSSW/lib/python/site-packages/" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-python.sh
echo "PYTHON_ROOT=$ALMASW_ROOTDIR/ACS-%{version}/Python" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-python.sh
echo 'PYTHONINC=/usr/include/python2.7' >> %{buildroot}%{_sysconfdir}/profile.d/acscb-python.sh
# $GNU_ROOT/bin is already part of the path
echo 'PATH="$PATH:/alma/ACS-%{version}/ACSSW/bin"' >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh

echo "export ACSDATA" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export ACSROOT" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export ACS_CDB" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh 
echo "export ACS_INSTANCE" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export ACS_STARTUP_TIMEOUT_MULTIPLIER" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export ACS_TMP" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export IDL_PATH" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export LD_LIBRARY_PATH" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export GNU_ROOT" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-gnu.sh
echo "export PYTHONPATH" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-python.sh
echo "export PYTHON_ROOT" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-python.sh
echo "export PYTHONINC" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-python.sh
echo "export PATH" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh

#mv %{buildroot}%{_sysconfdir}/profile.d/acscb.sh %{buildroot}%{_sysconfdir}/profile.d/acscb2.sh
#Symlink Libs in include. Very useful when building, because it's in gcc's default path
#mkdir -p %{buildroot}%{_usr}/local/include/

# Move ACS Mans to here
#mkdir -p %{buildroot}%{_usr}/local/share/
#mv %{buildroot}/home/almamgr/ACS-%{version}/ACSSW/share/man/man1/ %{buildroot}%{_usr}/local/share/man/
#mv %{buildroot}/home/almamgr/ACS-%{version}/ACSSW/share/man/man3/ %{buildroot}%{_usr}/local/share/man/

# /var/run/
mkdir -p %{buildroot}%{_var}/run/acscb/

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

%post devel
# Re-enabling the syntax error for testing
sed -i 's/#skdfksdllk = \$\$\$\$/skdfksdllk = \$\$\$\$/g' /home/almadevel/LGPL/Kit/acs/test/AcsPyTestPkg1/A.py
%preun
# Remove env vars
export LD_LIBRARY_PATH=$(echo $LD_LIBRARY_PATH | sed "s/\$ALMASW_ROOTDIR\/ACS-%{version}\/idl:\/usr\/lib64\/://g" )
export PATH=$(echo $PATH | sed "s/\/alma\/ACS-%{version}}/ACSSW}/bin//g" )
export PYTHONPATH=$(echo $PYTHONPATH | sed "s/\/usr\/lib64\/python2.7\/site-packages:\/opt\/rh\/rh-java-common\/root\/usr\/lib\/python2.7\/site-packages\/:\%{_usr}\/local\/lib\/python\/site-packages\/:\$ALMASW_ROOTDIR\/ACS-%{version}\/ACSSW\/lib\/python\/site-packages\///g" )
unset ACSDATA
unset ACSROOT
unset ACS_CDB
unset ACS_INSTANCE
unset ACS_STARTUP_TIMEOUT_MULTIPLIER
unset ACS_TMP
unset IDL_PATH
unset GNU_ROOT
unset PYTHONINC
 
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
%config %{_sysconfdir}/profile.d/acscb-gnu.sh
%config %{_sysconfdir}/profile.d/acscb-python.sh
%config %{_sysconfdir}/profile.d/acscb.sh
%attr(0705,almamgr,almamgr) /home/almamgr/ACS-%{version}/
%attr(0755,almamgr,almamgr) %{_var}/run/acscb/
#%docdir %{_usr}/local/share/man/
#%{_usr}/local/share/man/

%files devel
# LGPL, Benchmark, RPM-legacy
%attr(0705,almadevel,almadevel) /home/almadevel/

%changelog
* Sat Aug 19 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 2017.06-1
Updating version
* Fri Aug 19 2016 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
