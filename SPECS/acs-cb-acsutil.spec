%define minVersion 2017.06

Name:		ACS-acsutil
Version:	2017.08
Release:	1%{?dist}
Summary:	ACS Utils C++ Core
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
Source1:	Makefile-acsutil
BuildRequires:	ACS-Tools-Kit-Benchmark-devel >= %{minVersion} ACS-acsidlcommon >= %{version} ACS-acsidlcommon-devel >= %{version} 
# ACS-baciidl >= %{version}  ACS-baciidl-devel >= %{version}
Requires:	ACS-Tools-Kit-Benchmark >= %{minVersion}
Obsoletes:	acsutil

%description
ACS Util Core functions in C++

%prep
%setup -q

%build
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/Makefile

# Basic path
mkdir -p  %{_builddir}/home/almamgr
# Symlink for build log
ln -s %{_builddir}/home/almamgr %{_builddir}/alma
# Symlink for libacscommonStubs.so required to create libacsutil.so. libbaciStubs for testAnyAide
mkdir -p %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/lib/
ln -s  %{_usr}/local/%{_lib}/libacscommonStubs.so  %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/lib/
#ln -s  %{_usr}/local/%{_lib}/libbaciStubs.so %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/lib/
# Env Vars for installing. 
source %{_sysconfdir}/profile.d/acscb.sh
source %{_sysconfdir}/profile.d/acscb-toolsKit.sh
source %{_sysconfdir}/profile.d/acscb-gnu.sh
source %{_sysconfdir}/profile.d/tcltk-acs.sh

export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export ACS_CDB="$ALMASW_ROOTDIR/$ALMASW_RELEASE/config/defaultCDB"
export CPATH="/home/almadevel/LGPL/Tools/loki/ws/include/"
export PATH="$PATH:%{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src"

# Remove acsMakeJavaClasspath
echo '#!/usr/bin/env perl' > %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath
echo 'print $ENV{CLASSPATH}' >> %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath
chmod +x %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath

# Compilation specific env vars
export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

cd %{_builddir}/%{name}-%{version}/
# mkdir of ACSSW
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/

make

# TAT Stuff. Symlink to libtatlib.tcl/ folder
ln -s /home/almamgr/ACS-%{version}/ACSSW/lib/libtatlib.tcl/ %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/lib/
ln -s /home/almamgr/ACS-%{version}/ACSSW/lib/libtatlib.tcl/ %{_builddir}/%{name}-%{version}/LGPL/acsBUILD/lib/
export HOST="$HOSTNAME"
export VLTDATA=""
export OSYSTEM="Linux"
export CYGWIN_VER=""

# Replace to "". Its not system available
#sed -i 's/<baciC.h>/"baciC.h"/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/test/testAnyAide.cpp

#make test

# Clean symlink in builddir
unlink %{_builddir}/alma

%install
# Instalation on usr local, if python, then python/site-packages, if C/C++, then include, if Java, then share/java 
mkdir -p %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/lib/libacsutil.so %{buildroot}%{_usr}/local/%{_lib}/
chmod 755 %{buildroot}%{_usr}/local/%{_lib}/libacsutil.so

mkdir -p %{buildroot}%{_usr}/local/bin/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/bin/* %{buildroot}%{_usr}/local/bin/

%files
%{_usr}/local/%{_lib}/libacsutil.so
%{_usr}/local/bin/acsutilAwaitContainerStart
%{_usr}/local/bin/acsutilBlock
%{_usr}/local/bin/acsutilDiffTrap
%{_usr}/local/bin/acsutilProfiler
%{_usr}/local/bin/acsutilRedo
%{_usr}/local/bin/acsutilTATEpilogue
%{_usr}/local/bin/acsutilTATPrologue
%{_usr}/local/bin/acsutilTATTestRunner
#%{_usr}/local/bin/testacsutilBlock
#%{_usr}/local/bin/testFindFile
#%{_usr}/local/bin/testLLU
#%{_usr}/local/bin/testPorts
#%{_usr}/local/bin/testTmp

%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
