%define minVersion 2017.06

Name:       ACS-acscomponentidl
Version:    2017.08
Release:    1%{?dist}
Summary:    ACS Logging
License:    LGPL
URL:        http://csrg-utfsm.github.io
Source0:    %{name}-%{version}.tar.gz
Source1:    Makefile-acscomponentidl
BuildRequires:  ACS-Tools-Kit-Benchmark-devel >= %{minVersion}
Requires:       ACS-Tools-Kit-Benchmark >= %{minVersion}
Obsoletes:  acscomponentidl

%description
ACS Component IDL.

%package devel
Summary: ACS Component IDL Objects (Stubs-Skeletons)
License: LGPL

%description devel
IDL object output: .h,.cpp,.inl,.o Stubs and Skeletons

%prep
%setup -q

%build
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/Makefile

# Basic path
mkdir -p  %{_builddir}/home/almamgr

# Symlink for build log
ln -s %{_builddir}/home/almamgr %{_builddir}/alma

source %{_sysconfdir}/profile.d/acscb-gnu.sh
source %{_sysconfdir}/profile.d/tcltk-acs.sh
source %{_sysconfdir}/profile.d/acscb-python.sh
source %{_sysconfdir}/profile.d/jacorb-acs.sh
export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export ACS_CDB="$ALMASW_ROOTDIR/$ALMASW_RELEASE/config/defaultCDB"
export ACSDATA="$ALMASW_ROOTDIR/$ALMASW_RELEASE/acsdata"

export CPATH="%{_builddir}/%{name}-%{version}/LGPL/Tools/loki/ws/include"

export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

export PATH="$PATH:%{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/"
export PYTHONPATH=$PYTHONPATH:%{_usr}/share/idl/omniORB/

# Remove acsMakeJavaClasspath
echo '#!/usr/bin/env perl' > %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath
echo 'print $ENV{CLASSPATH}' >> %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath
chmod +x %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath
# omniorb acs_python lookup
sed -i 's|-bacs_python|-p %{_builddir}/%{name}-%{version}/LGPL/Tools/extpy/src/ -bacs_python |g' %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/include/acsMakefileDefinitions.mk

cd %{_builddir}/%{name}-%{version}/

# mkdir of ACSSW
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/

make

#unlink
unlink %{_builddir}/alma

%install
# Devel stuff
mkdir -p %{buildroot}%{_usr}/local/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acscomponentidl/ws/object/*.h %{buildroot}%{_usr}/local/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acscomponentidl/ws/object/*.inl %{buildroot}%{_usr}/local/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acscomponentidl/ws/object/*.cpp %{buildroot}%{_usr}/local/include/

mkdir -p %{buildroot}%{_usr}/local/%{_lib}/
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acscomponentidl/ws/lib/libacscomponentStubs.so
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acscomponentidl/ws/lib/libacscomponentStubs.so %{buildroot}%{_usr}/local/%{_lib}/libacscomponentStubs.so

# ACS and ACS__POA already provided by ACS Common IDL 
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acscomponentidl/ws/lib/python/site-packages/acscomponent_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/acscomponent_idl.py
# Clean
cd %{buildroot}%{_usr}/local/lib/python/site-packages/
find -name "*.pyo" | xargs rm -rf

mkdir -p %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acscomponentidl/ws/lib/acscomponent.jar %{buildroot}%{_usr}/local/share/java/acscomponent.jar

%files
#%{_usr}/local/lib/python/site-packages/ACS/
#%{_usr}/local/lib/python/site-packages/ACS__POA/
%{_usr}/local/lib/python/site-packages/acscomponent_idl.py*
%{_usr}/local/%{_lib}/libacscomponentStubs.so
%{_usr}/local/share/java/acscomponent.jar

%files devel
%{_usr}/local/include/acscomponentC.h
%{_usr}/local/include/acscomponentS.h
%{_usr}/local/include/acscomponentC.cpp
%{_usr}/local/include/acscomponentS.cpp
%{_usr}/local/include/acscomponentC.inl

%changelog
* Wed May 31 2017 Marcelo Jara <mijara@alumnos.inf.utfsm.cl> - 0.1-1
Initial Packaging
