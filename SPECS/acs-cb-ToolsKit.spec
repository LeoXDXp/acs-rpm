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
AutoReq:	no

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
Requires: procmail python-lockfile net-tools xterm man ACS-ExtProds >= %{version} tkinter ACS-eclipse-plugins >= %{version} ACS-ExtJars >= %{version}
Requires: apache-commons-lang junit
# X Packages: nautilus-open-terminal not yet in EL7
Requires: gnome-classic-session gnome-terminal control-center liberation-mono-fonts setroubleshoot-server glx-utils gdm openbox mesa-dri-drivers plymouth-system-theme spice-vdagent xorg-x11-drivers xorg-x11-server-Xorg xorg-x11-utils xorg-x11-xauth xorg-x11-xinit xvattr xorg-x11-drv-keyboard xorg-x11-drv-mouse
Requires: gcc-c++ java-1.8.0-openjdk java-1.8.0-openjdk-devel java-1.8.0-openjdk-demo net-tools
Requires: log4cpp-ACS castor-ACS gcc gcc-c++ emacs antlr expat expat-devel cppunit cppunit-devel swig loki-lib shunit2 hibernate3 xerces-c xerces-c-devel xerces-j2

%description
RPM Installer of ACS-CB Tools and Kit %{version}. Installs ACS CB Tools and Kit modules in /home/almamgr/ACS-%{version}/ACSSW/, leaving env vars in profile.d and commands symlinked to /usr/local/bin avoiding sourcing of .bash_profile.acs file. It also creates acsdata.

%package devel
Summary: ACS CB Benchmark files for {?dist} 
License: LGPL
AutoReq: no
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
export ACS_CDB="$ALMASW_ROOTDIR/$ALMASW_RELEASE/acsdata/config/defaultCDB"
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
export PYTHONPATH="$PYTHONPATH:/usr/lib/python2.7/site-packages:/opt/rh/rh-java-common/root/usr/lib/python2.7/site-packages/:%{_builddir}/home/almamgr/ACS-%{version}/ACSSW/lib/python/site-packages:%{_usr}/local/lib/python/site-packages/:%{_builddir}/%{name}-%{version}/LGPL/Tools/extpy/src/:/usr/share/idl/omniORB/"
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
#sed -i "s///g" %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/include/acsMakefileDefinitions.mk

# Temporary for debugging
#sed -i 's/tat xsddoc extidl vtd-xml oAW scxml_apache/extidl/g' %{_builddir}/%{name}-%{version}/LGPL/Tools/Makefile
#acsBuild searchfile fix
sed -i "s/\$(MAKEDIR)\/acsMakefile/$tempbdir\/%{name}-%{version}\/LGPL\/Kit\/acs\/include\/acsMakefile $tempbdir\/%{name}-%{version}\/LGPL\/Kit\/acs\/include\/acsMakefileCore.mk $tempbdir\/%{name}-%{version}\/LGPL\/Kit\/acs\/include\/acsMakefileDefinitions.mk  /g" %{_builddir}/%{name}-%{version}/LGPL/acsBUILD/src/Makefile

# Remove acsMakeJavaClasspath
echo '#!/usr/bin/env perl' > %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath
echo 'print $ENV{CLASSPATH}' >> %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath
chmod +x %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath

cd %{_builddir}/%{name}-%{version}/
# mkdir of ACSSW
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/
# Symlink of Python's compilelall for hardcoded path in make files
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/Python/lib/python2.7/
# Only if symlink is not already written
if [ ! -e %{_builddir}/home/almamgr/ACS-%{version}/Python/lib/python2.7/compileall.py  ]; then
  ln -s %{_usr}/%{_lib}/python2.7/compileall.py %{_builddir}/home/almamgr/ACS-%{version}/Python/lib/python2.7/compileall.py
fi

make

#Manual creation of extidl py
cd %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/idl
#ln -s  /usr/include/tao/ tao
#ln -s /usr/share/idl/omniORB/orb.idl .
#omniidl -I /usr/include/ -bacs_python -p %{_builddir}/%{name}-%{version}/LGPL/Tools/extpy/src/ Monitor_Types.idl
#omniidl -I /usr/include/ -bacs_python -p %{_builddir}/%{name}-%{version}/LGPL/Tools/extpy/src/ Monitor.idl
#omniidl -I /usr/include/ -bacs_python -p %{_builddir}/%{name}-%{version}/LGPL/Tools/extpy/src/ NotificationServiceMC.idl
export PYTHONPATH=%{_usr}/share/idl/omniORB/
omniidl -I /usr/include/ -bacs_python -p %{_builddir}/%{name}-%{version}/LGPL/Tools/extpy/src/ DsLogAdmin.idl
#NotifyExt
omniidl -I /usr/share/idl/omniORB/COS/ -bacs_python -p %{_builddir}/%{name}-%{version}/LGPL/Tools/extpy/src/ NotifyExt.idl
omniidl -I /usr/include/ -I /usr/share/idl/omniORB/ -bacs_python -p %{_builddir}/%{name}-%{version}/LGPL/Tools/extpy/src/ NotifyMonitoringExt.idl
omniidl -I /usr/include/ -bacs_python -p %{_builddir}/%{name}-%{version}/LGPL/Tools/extpy/src/ TimeBase.pidl
#omniidl -I /usr/include/ -bacs_python -p %{_builddir}/%{name}-%{version}/LGPL/Tools/extpy/src/ StringSeq.pidl

#make test #make: *** No rule to make target `test'.  Stop.

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

mkdir -p %{buildroot}%{_usr}/local/share/java/
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/DsLogAdmin
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/DsLogAdmin__POA
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/NotifyExt
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/NotifyExt__POA
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/NotifyMonitoringExt
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/NotifyMonitoringExt__POA
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/TimeBase
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/TimeBase__POA
#mkdir -p %{buildroot}%{_usr}/local/include/
mkdir -p %{buildroot}%{_usr}/local/bin/

# /etc. Hoping to have acsdata only on etc in the future
mkdir -p %{buildroot}%{_sysconfdir}/acscb/
cp -r %{_builddir}/home/almamgr/ACS-%{version}/acsdata/config/ %{buildroot}%{_sysconfdir}/acscb/
# TAT bin
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/tat/bin/tat %{buildroot}%{_usr}/local/bin/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/tat/bin/tatCleanShm %{buildroot}%{_usr}/local/bin/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/tat/bin/tatEnvStatus %{buildroot}%{_usr}/local/bin/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/tat/bin/tatGetClock %{buildroot}%{_usr}/local/bin/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/tat/bin/tatRemExec %{buildroot}%{_usr}/local/bin/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/tat/bin/tatTestSpawner %{buildroot}%{_usr}/local/bin/ 
# TAT lib - can be recreated. Not packing it
# xsddoc bin - jar
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/xsddoc/bin/xsddoc %{buildroot}%{_usr}/local/bin/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/xsddoc/lib/xsddoc.jar %{buildroot}%{_usr}/local/share/java/
#Extidl Java
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/lib/Monitor.jar  %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/lib/Monitor_Types.jar  %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/lib/NotificationServiceMC.jar  %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/lib/NotifyExt.jar  %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/lib/NotifyMonitoringExt.jar  %{buildroot}%{_usr}/local/share/java/
# Extidl Python
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/idl/DsLogAdmin/__init__.py %{buildroot}%{_usr}/local/lib/python/site-packages/DsLogAdmin/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/idl/DsLogAdmin__POA/__init__.py %{buildroot}%{_usr}/local/lib/python/site-packages/DsLogAdmin__POA/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/idl/DsLogAdmin_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/idl/NotifyExt/__init__.py %{buildroot}%{_usr}/local/lib/python/site-packages/NotifyExt/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/idl/NotifyExt__POA/__init__.py %{buildroot}%{_usr}/local/lib/python/site-packages/NotifyExt__POA/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/idl/NotifyExt_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/idl/NotifyMonitoringExt/__init__.py %{buildroot}%{_usr}/local/lib/python/site-packages/NotifyMonitoringExt/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/idl/NotifyMonitoringExt__POA/__init__.py %{buildroot}%{_usr}/local/lib/python/site-packages/NotifyMonitoringExt__POA/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/idl/NotifyMonitoringExt_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/idl/TimeBase/__init__.py %{buildroot}%{_usr}/local/lib/python/site-packages/TimeBase/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/idl/TimeBase__POA/__init__.py %{buildroot}%{_usr}/local/lib/python/site-packages/TimeBase__POA/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/extidl/ws/idl/TimeBase_pidl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
# vtd-xml 
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/vtd-xml/lib/vtd-xml.jar %{buildroot}%{_usr}/local/share/java/
# oAW
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/antlr-generator-3.0.1.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/com.google.collect_0.8.0.v201008251220.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/com.google.inject_2.0.0.v201003051000.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/com.ibm.icu_4.2.1.v20100412.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/ecj-4.4.2.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.antlr.runtime_3.0.0.v200803061811.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.emf.codegen_2.6.0.v20100914-1218.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.emf.codegen.ecore_2.6.1.v20100914-1218.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.emf.common_2.6.0.v20100914-1218.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.emf.ecore_2.6.1.v20100914-1218.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.emf.ecore.xmi_2.5.0.v20100521-1846.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.emf.mapping.ecore2xml_2.5.0.v20100521-1847.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.emf.mwe2.runtime_1.0.1.v201008251113.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.emf.mwe.core_1.0.0.v201008251122.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.emf.mwe.utils_1.0.0.v201008251122.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.equinox.common_3.6.0.v20100503.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.text_3.5.0.v20100601-1300.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.uml2.common_1.5.0.v201005031530.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.uml2.uml_3.1.1.v201008191505.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.uml2.uml.resources_3.1.1.v201008191505.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.xpand_1.0.1.v201008251147.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.xtend_1.0.1.v201008251147.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.xtend.typesystem.emf_1.0.1.v201008251147.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.xtend.typesystem.uml2_1.0.1.v201008251147.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.xtend.util.stdlib_1.0.1.v201008251147.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.xtext_1.0.1.v201008251220.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.xtext.generator_1.0.1.v201008251220.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.xtext.util_1.0.1.v201008251220.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/oAW/lib/org.eclipse.xtext.xtend_1.0.1.v201008251220.jar %{buildroot}%{_usr}/local/share/java/
# scxml_apache
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/scxml_apache/lib/commons-el-1.0.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/scxml_apache/lib/commons-scxml-0.9.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/scxml_apache/lib/jsp-api-2.0.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/scxml_apache/lib/myfaces-api-1.1.5.jar %{buildroot}%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/Tools/scxml_apache/lib/servlet-api-2.4.jar %{buildroot}%{_usr}/local/share/java/

# Devel folders: LGPL, Benchmark
mkdir -p  %{buildroot}/home/almadevel/
mv %{_builddir}/%{name}-%{version}/LGPL/ %{buildroot}/home/almadevel/
mv %{_builddir}/%{name}-%{version}/Benchmark/ %{buildroot}/home/almadevel/

# Env Vars to profile.d. Place to create files for variable exporting on boot
mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
export ALMASW_ROOTDIR="/alma"
echo "ACSDATA=$ALMASW_ROOTDIR/ACS-%{version}/acsdata" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "ACSROOT=$ALMASW_ROOTDIR/ACS-%{version}/ACSSW" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "ACS_CDB=$ALMASW_ROOTDIR/ACS-%{version}/config/defaultCDB" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh 
echo "ACS_INSTANCE=0" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "ACS_STARTUP_TIMEOUT_MULTIPLIER=2" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
#echo "ACS_TMP=$ALMASW_ROOTDIR/ACS-%{version}/tmp/$HOSTNAME" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo 'IDL_PATH="-I$ACSROOT/idl -I/usr/src/debug/ACE_wrappers/TAO/orbsvcs/orbsvcs -I$TAO_ROOT/orbsvcs -I$TAO_ROOT -I/usr/include/orbsvcs -I/usr/include/tao"' >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ALMASW_ROOTDIR/ACS-%{version}/idl:/usr/lib64/:%{_usr}/local/%{_lib}/" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "GNU_ROOT=%{_usr}" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-gnu.sh
echo "PYTHONPATH=/usr/lib64/python2.7/site-packages:/opt/rh/rh-java-common/root/usr/lib/python2.7/site-packages/:%{_usr}/local/lib/python/site-packages/:$ALMASW_ROOTDIR/ACS-%{version}/ACSSW/lib/python/site-packages/" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-python.sh
echo "PYTHON_ROOT=$ALMASW_ROOTDIR/ACS-%{version}/Python" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-python.sh
echo 'PYTHONINC=/usr/include/python2.7' >> %{buildroot}%{_sysconfdir}/profile.d/acscb-python.sh
# $GNU_ROOT/bin is already part of the path
echo 'PATH="$PATH:/alma/ACS-%{version}/ACSSW/bin"' >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo 'OSYSTEM=LINUX'  >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo 'CYGWIN_VER="CYGWIN_NT-5.1"' >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo 'PATH_SEP=":"' >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh

echo "export ACSDATA" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export ACSROOT" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export ACS_CDB" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh 
echo "export ACS_INSTANCE" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export ACS_STARTUP_TIMEOUT_MULTIPLIER" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
#echo "export ACS_TMP" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export IDL_PATH" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export LD_LIBRARY_PATH" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export GNU_ROOT" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-gnu.sh
echo "export PYTHONPATH" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-python.sh
echo "export PYTHON_ROOT" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-python.sh
echo "export PYTHONINC" >> %{buildroot}%{_sysconfdir}/profile.d/acscb-python.sh
echo "export PATH" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo 'export OSYSTEM'  >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export CYGWIN_VER" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo 'export PATH_SEP' >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh

mv %{buildroot}%{_sysconfdir}/profile.d/acscb.sh %{buildroot}%{_sysconfdir}/profile.d/acscb-toolsKit.sh

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
#useradd -U almaproc
#echo new2me | echo new2me | passwd --stdin almaproc

%pre devel

if ! id almadevel >/dev/null 2>&1; then
        useradd -U almadevel
fi

%post
# Permissions
chown -R almamgr:almamgr /home/almamgr/
chown almamgr:almamgr %{_var}/run/acscb/
#chown almaproc:almaproc /home/almaproc/introot/
mkdir -p /home/almamgr/ACS-%{version}/Python/lib/python2.7/
ln -s %{_usr}/%{_lib}/python2.7/compileall.py /home/almamgr/ACS-%{version}/Python/lib/python2.7/compileall.py
ln -s /home/almamgr/ACS-%{version}/ /home/almamgr/ACS-%{ALTVER}
ln -s /home/almamgr/ACS-%{version}/ /home/almamgr/ACS-latest

echo "ACS_TMP=$ALMASW_ROOTDIR/ACS-%{version}/tmp/$HOSTNAME" >> %{_sysconfdir}/profile.d/acscb.sh
echo "export ACS_TMP" >> %{_sysconfdir}/profile.d/acscb.sh

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
#pkill -u almaproc
#userdel -r almaproc

%postun devel
pkill -u almadevel
userdel -r almadevel

%files
# ACSSW, acsdata, READMEs, LICENSE, ACS_VERSION, ACS_PATCH_LEVEL
%config %{_sysconfdir}/acscb/
%config %{_sysconfdir}/profile.d/acscb-gnu.sh
%config %{_sysconfdir}/profile.d/acscb-python.sh
%config %{_sysconfdir}/profile.d/acscb-toolsKit.sh
%attr(0705,almamgr,almamgr) /home/almamgr/ACS-%{version}/
%attr(0755,almamgr,almamgr) %{_var}/run/acscb/
%{_usr}/local/share/java/Monitor.jar
%{_usr}/local/share/java/Monitor_Types.jar
%{_usr}/local/share/java/NotificationServiceMC.jar
%{_usr}/local/share/java/NotifyExt.jar
%{_usr}/local/share/java/NotifyMonitoringExt.jar
%{_usr}/local/share/java/xsddoc.jar
%{_usr}/local/share/java/vtd-xml.jar
%{_usr}/local/share/java/antlr-generator-3.0.1.jar
%{_usr}/local/share/java/com.google.collect_0.8.0.v201008251220.jar
%{_usr}/local/share/java/com.google.inject_2.0.0.v201003051000.jar
%{_usr}/local/share/java/com.ibm.icu_4.2.1.v20100412.jar
%{_usr}/local/share/java/ecj-4.4.2.jar
%{_usr}/local/share/java/org.antlr.runtime_3.0.0.v200803061811.jar
%{_usr}/local/share/java/org.eclipse.emf.codegen_2.6.0.v20100914-1218.jar
%{_usr}/local/share/java/org.eclipse.emf.codegen.ecore_2.6.1.v20100914-1218.jar
%{_usr}/local/share/java/org.eclipse.emf.common_2.6.0.v20100914-1218.jar
%{_usr}/local/share/java/org.eclipse.emf.ecore_2.6.1.v20100914-1218.jar
%{_usr}/local/share/java/org.eclipse.emf.ecore.xmi_2.5.0.v20100521-1846.jar
%{_usr}/local/share/java/org.eclipse.emf.mapping.ecore2xml_2.5.0.v20100521-1847.jar
%{_usr}/local/share/java/org.eclipse.emf.mwe2.runtime_1.0.1.v201008251113.jar
%{_usr}/local/share/java/org.eclipse.emf.mwe.core_1.0.0.v201008251122.jar
%{_usr}/local/share/java/org.eclipse.emf.mwe.utils_1.0.0.v201008251122.jar
%{_usr}/local/share/java/org.eclipse.equinox.common_3.6.0.v20100503.jar
%{_usr}/local/share/java/org.eclipse.text_3.5.0.v20100601-1300.jar
%{_usr}/local/share/java/org.eclipse.uml2.common_1.5.0.v201005031530.jar
%{_usr}/local/share/java/org.eclipse.uml2.uml_3.1.1.v201008191505.jar
%{_usr}/local/share/java/org.eclipse.uml2.uml.resources_3.1.1.v201008191505.jar
%{_usr}/local/share/java/org.eclipse.xpand_1.0.1.v201008251147.jar
%{_usr}/local/share/java/org.eclipse.xtend_1.0.1.v201008251147.jar
%{_usr}/local/share/java/org.eclipse.xtend.typesystem.emf_1.0.1.v201008251147.jar
%{_usr}/local/share/java/org.eclipse.xtend.typesystem.uml2_1.0.1.v201008251147.jar
%{_usr}/local/share/java/org.eclipse.xtend.util.stdlib_1.0.1.v201008251147.jar
%{_usr}/local/share/java/org.eclipse.xtext_1.0.1.v201008251220.jar
%{_usr}/local/share/java/org.eclipse.xtext.generator_1.0.1.v201008251220.jar
%{_usr}/local/share/java/org.eclipse.xtext.util_1.0.1.v201008251220.jar
%{_usr}/local/share/java/org.eclipse.xtext.xtend_1.0.1.v201008251220.jar
%{_usr}/local/share/java/commons-el-1.0.jar
%{_usr}/local/share/java/commons-scxml-0.9.jar
%{_usr}/local/share/java/jsp-api-2.0.jar
%{_usr}/local/share/java/myfaces-api-1.1.5.jar
%{_usr}/local/share/java/servlet-api-2.4.jar

%{_usr}/local/lib/python/site-packages/DsLogAdmin/
%{_usr}/local/lib/python/site-packages/DsLogAdmin__POA/
%{_usr}/local/lib/python/site-packages/DsLogAdmin_idl.py*
%{_usr}/local/lib/python/site-packages/NotifyExt/
%{_usr}/local/lib/python/site-packages/NotifyExt__POA/
%{_usr}/local/lib/python/site-packages/NotifyExt_idl.py*
%{_usr}/local/lib/python/site-packages/NotifyMonitoringExt/
%{_usr}/local/lib/python/site-packages/NotifyMonitoringExt__POA/
%{_usr}/local/lib/python/site-packages/NotifyMonitoringExt_idl.py*
%{_usr}/local/lib/python/site-packages/TimeBase/
%{_usr}/local/lib/python/site-packages/TimeBase__POA/
%{_usr}/local/lib/python/site-packages/TimeBase_pidl.py*

%{_usr}/local/bin/tat
%{_usr}/local/bin/tatCleanShm
%{_usr}/local/bin/tatEnvStatus
%{_usr}/local/bin/tatGetClock
%{_usr}/local/bin/tatRemExec
%{_usr}/local/bin/tatTestSpawner
%{_usr}/local/bin/xsddoc

%files devel
# LGPL, Benchmark
%attr(0705,almadevel,almadevel) /home/almadevel/

%changelog
* Sat Aug 19 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 2017.06-1
Updating version
* Fri Aug 19 2016 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
