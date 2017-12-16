%define minVersion 2017.06

Name:       ACS-logging
Version:    2017.08
Release:    1%{?dist}
Summary:    ACS Logging
License:    LGPL
URL:        http://csrg-utfsm.github.io
Source0:    %{name}-%{version}.tar.gz
Source1:    Makefile-logging

BuildRequires: ACS-Tools-Kit-Benchmark >= %{minVersion} ACS-loggingidl-devel >= %{version} ACS-loggingidl >= %{version}  log4cpp log4cpp-ACS-devel ACS-acsutil >= %{version} ACS-acsidlcommon >= %{version}
# log4cpp-ACS >= 1.0.%{version}
Requires:       ACS-Tools-Kit-Benchmark >= %{minVersion}

%description
ACS logging.

%prep
%setup -q

%build
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/Makefile

# Basic path
rm -rf %{_builddir}/home/almamgr/
mkdir -p  %{_builddir}/home/almamgr
# Symlink for build log
ln -s %{_builddir}/home/almamgr %{_builddir}/alma

# Include acsutil
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/include/*.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/
# acsutil.so
mkdir -p %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/lib/
ln -s %{_usr}/local/%{_lib}/libacsutil.so %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/lib/
# loki
ln -s /usr/%{_lib}/libloki.so.0 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/lib/libloki.so
# Testing with normal log4cpp
ln -s /usr/%{_lib}/liblog4cpp.so.5 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/lib/liblog4cpp.so
# liblogging_idlStubs.so
ln -s /usr/local/%{_lib}/liblogging_idlStubs.so %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/lib/
# acsidlcommon
ln -s /usr/local/%{_lib}/libacscommonStubs.so %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/lib/
#DsLogAdmin{C|S}.h, DsLogAdminC.inl not located by logging_idlC.h
ln -s %{_usr}/include/orbsvcs/DsLogAdminC.h  %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/
ln -s %{_usr}/include/orbsvcs/DsLogAdminS.h  %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/
ln -s %{_usr}/include/orbsvcs/DsLogAdminC.inl  %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/
# Compilation cant file libbaselogging.a
sed -i 's/@echo "ERROR: ----> $@  does not exist."; exit 1/@echo "ERROR: ----> $@  does not exist.";/g'  %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/include/acsMakefile


export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export ACS_CDB="$ALMASW_ROOTDIR/$ALMASW_RELEASE/config/defaultCDB"
export ACSDATA="$ALMASW_ROOTDIR/$ALMASW_RELEASE/acsdata"
export PYTHON_ROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/Python"
export CPATH="%{_builddir}/%{name}-%{version}/LGPL/Tools/loki/ws/include"
export PATH="$PATH:%{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src"

# Remove acsMakeJavaClasspath
echo '#!/usr/bin/env perl' > %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath
echo 'print $ENV{CLASSPATH}' >> %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath
chmod +x %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath

# DsLogAdminC.h and CosNamingC.h are at /usr/include. No need for special extendend route
sed -i 's|orbsvcs/orbsvcs|orbsvcs|g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingLoggingProxy.h

export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

cd %{_builddir}/%{name}-%{version}/

# mkdir of ACSSW
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/
# Symlink of Python's compilelall for hardcoded path in make files
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/Python/lib/python2.7/
ln -s %{_usr}/%{_lib}/python2.7/compileall.py %{_builddir}/home/almamgr/ACS-%{version}/Python/lib/python2.7/compileall.py
make

# TAT Stuff. Symlink to libtatlib.tcl/ folder
ln -s /home/almamgr/ACS-%{version}/ACSSW/lib/libtatlib.tcl/ %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/lib/
ln -s /home/almamgr/ACS-%{version}/ACSSW/lib/libtatlib.tcl/ %{_builddir}/%{name}-%{version}/LGPL/acsBUILD/lib/
export HOST="$HOSTNAME"
export VLTDATA=""
export OSYSTEM="Linux"
export CYGWIN_VER=""

# maciSimpleClient.h
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/maci/ws/include/maciSimpleClient.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/
#sed -i 's/<maciSimpleClient.h>/"maciSimpleClient.h"/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/
# maciSimpleClientThreadHook.h
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/maci/ws/include/maciSimpleClientThreadHook.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/
# maciClientExport.h
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/maci/ws/include/maciClientExport.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/

#make test

#unlink
unlink %{_builddir}/alma

%install
#mkdir -p %{buildroot}/%{_usr}/local/share/java/
mkdir -p %{buildroot}%{_usr}/local/%{_lib}/

#java files
#cp %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/lib/DsLogAdmin.jar %{buildroot}/%{_usr}/local/share/java/
#cp %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/lib/logging_idl.jar %{buildroot}/%{_usr}/local/share/java/
#lib
cp %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/lib/libbaselogging.so %{buildroot}%{_usr}/local/%{_lib}/
cp %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/lib/libbaselogging.a %{buildroot}%{_usr}/local/%{_lib}/
cp %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/lib/liblogging.so %{buildroot}%{_usr}/local/%{_lib}/
cp %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/lib/liblogging.a %{buildroot}%{_usr}/local/%{_lib}/
chmod 755 %{buildroot}%{_usr}/local/%{_lib}/libbaselogging.so
chmod 755 %{buildroot}%{_usr}/local/%{_lib}/liblogging.so

%files
#%{_usr}/local/share/java/logging_idl.jar

%{_usr}/local/%{_lib}/libbaselogging.so
%{_usr}/local/%{_lib}/liblogging.so
%{_usr}/local/%{_lib}/libbaselogging.a
%{_usr}/local/%{_lib}/liblogging.a

%changelog
* Sat Aug 19 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Updating to 2017.06
* Wed May 24 2017 Marcelo Jara <mijara@alumnos.inf.utfsm.cl> - 0.1-1
Initial Packaging
