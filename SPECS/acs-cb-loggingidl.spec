Name:       ACS-loggingidl
Version:    2017.06
Release:    1%{?dist}
Summary:    ACS Logging IDL Declarations
License:    LGPL
URL:        http://csrg-utfsm.github.io
Source0:    %{name}-%{version}.tar.gz
Source1:    Makefile-loggingidl
Source2:    DsLogAdmin.jar
Source3:    TimeBase.jar

BuildRequires:  ACS-Tools-Kit-Benchmark-devel >= %{version}
Requires:       ACS-Tools-Kit-Benchmark >= %{version}
Obsoletes:	loggingidl logging
%description
ACS Logging IDL Interfaces.

%package devel
Summary:        ACS Logging IDL Objects
License:        LGPL

%description devel
IDL object output: .h,.cpp,.inl,.o Stubs and Skeletons

%prep
%setup -q

#cambiar el makefile solo para el modulo
%build
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/Makefile

# Basic path
mkdir -p  %{_builddir}/home/almamgr
# Symlink for build log
ln -s %{_builddir}/home/almamgr %{_builddir}/alma
ln -s /usr/include/orbsvcs/DsLogAdmin.idl %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/idl/
ln -s /usr/share/tao/tao/ %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/idl/

# Small hack, due to Jenkins not finding <DsLogAdmin.idl>
sed -i 's/<DsLogAdmin.idl>/\"DsLogAdmin.idl\"/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/idl/logging_idl.idl

mkdir -p %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/lib/
mkdir -p %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/lib/tao/
# jar cvf DsLogAdmin.jar org/omg/DsLogAdmin/*.class
cp -f %{SOURCE2} %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/lib/DsLogAdmin.jar
cp -f %{SOURCE3} %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/lib/tao/TimeBase.jar

source %{_sysconfdir}/profile.d/acscb-gnu.sh
source %{_sysconfdir}/profile.d/tcltk-acs.sh
source %{_sysconfdir}/profile.d/ace-devel.sh
source %{_sysconfdir}/profile.d/acscb-python.sh
source %{_sysconfdir}/profile.d/jacorb-acs.sh
source %{_sysconfdir}/profile.d/tao-devel.sh

export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export ACS_CDB="$ALMASW_ROOTDIR/$ALMASW_RELEASE/config/defaultCDB"
export ACSDATA="$ALMASW_ROOTDIR/$ALMASW_RELEASE/acsdata"

export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

export PATH="$PATH:%{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/"

# Remove acsMakeJavaClasspath
echo '#!/usr/bin/env perl' > %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath
echo 'print $ENV{CLASSPATH}' >> %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath
chmod +x %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath

# omniorb acs_python lookup
sed -i 's|-bacs_python|-p %{_builddir}/%{name}-%{version}/LGPL/Tools/extpy/src/ -bacs_python |g' %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/include/acsMakefileDefinitions.mk

# DsLogAdminC needed
mkdir -p %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/include/
ln -s /usr/include/orbsvcs/DsLogAdminC.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/include/
ln -s /usr/include/orbsvcs/DsLogAdminC.inl %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/include/
ln -s /usr/include/orbsvcs/DsLogAdminS.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/include/

cd %{_builddir}/%{name}-%{version}/

# mkdir of ACSSW
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/

make

#unlink
unlink %{_builddir}/alma

%install
mkdir -p %{buildroot}/%{_usr}/local/share/java/
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/
mkdir -p %{buildroot}%{_usr}/local/%{_lib}/

#python files
mv %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/lib/python/site-packages/* %{buildroot}%{_usr}/local/lib/python/site-packages/
#java files
cp %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/lib/DsLogAdmin.jar %{buildroot}/%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/lib/logging_idl.jar %{buildroot}/%{_usr}/local/share/java/
#lib
cp %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/lib/liblogging_idlStubs.so %{buildroot}%{_usr}/local/%{_lib}/
chmod 755 %{buildroot}%{_usr}/local/%{_lib}/liblogging_idlStubs.so

# Devel Stuff
mkdir -p %{buildroot}%{_usr}/local/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/object/*.h %{buildroot}%{_usr}/local/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/object/*.cpp %{buildroot}%{_usr}/local/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/object/*.inl %{buildroot}%{_usr}/local/include/

%files
%{_usr}/local/lib/python/site-packages/ACSLoggingLog/
%{_usr}/local/lib/python/site-packages/ACSLoggingLog__POA/
%{_usr}/local/lib/python/site-packages/AcsLogLevels/
%{_usr}/local/lib/python/site-packages/AcsLogLevels__POA/
%{_usr}/local/lib/python/site-packages/Logging/
%{_usr}/local/lib/python/site-packages/Logging__POA/
%{_usr}/local/lib/python/site-packages/logging_idl_idl.py*
%{_usr}/local/share/java/logging_idl.jar
%{_usr}/local/share/java/DsLogAdmin.jar
%{_usr}/local/%{_lib}/liblogging_idlStubs.so

%files devel
%{_usr}/local/include/logging_idlC.cpp
%{_usr}/local/include/logging_idlC.h
%{_usr}/local/include/logging_idlC.inl
%{_usr}/local/include/logging_idlS.cpp
%{_usr}/local/include/logging_idlS.h

%changelog
* Wed May 24 2017 Maximiliano Osorio <mosorio@inf.utfsm.cl> - 0.1-1
Initial Packaging
