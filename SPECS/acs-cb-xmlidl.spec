%define minVersion 2017.06

Name:       ACS-xmlidl
Version:    2017.08
Release:    1%{?dist}
Summary:    ACS XML IDL Declarations
License:    LGPL
URL:        http://csrg-utfsm.github.io
Source0:    %{name}-%{version}.tar.gz
Source1:    Makefile-xmlidl
BuildRequires:  ACS-Tools-Kit-Benchmark-devel >= %{minVersion}
Requires:       ACS-Tools-Kit-Benchmark >= %{minVersion}

%description
ACS xml idl.

%prep
%setup -q

%build
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/Makefile

# Basic path
mkdir -p  %{_builddir}/home/almamgr
# Symlink for build log
ln -s %{_builddir}/home/almamgr %{_builddir}/alma
#ln -s /usr/include/orbsvcs/DsLogAdmin.idl %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/lowxmwgingidl/ws/idl/
#ln -s /usr/share/tao/tao/ %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/idl/

#
#mkdir -p %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/lib/
#mkdir -p %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/lib/tao/

#cp -f %{SOURCE2} %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/lib/DsLogAdmin.jar
#cp -f %{SOURCE3} %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/lib/tao/TimeBase.jar

#source %{_sysconfdir}/profile.d/acscb.sh
#source %{_sysconfdir}/profile.d/acscb-toolsKit.sh
#source %{_sysconfdir}/profile.d/acscb-gnu.sh
#source %{_sysconfdir}/profile.d/tcltk-acs.sh
#source %{_sysconfdir}/profile.d/ace-devel.sh
#source %{_sysconfdir}/profile.d/acscb-python.sh
#source %{_sysconfdir}/profile.d/jacorb-acs.sh
#source %{_sysconfdir}/profile.d/tao-devel.sh

# standard.
export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export ACS_CDB="$ALMASW_ROOTDIR/$ALMASW_RELEASE/config/defaultCDB"
export ACSDATA="$ALMASW_ROOTDIR/$ALMASW_RELEASE/acsdata"

# standard.
export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

cd %{_builddir}/%{name}-%{version}/

# mkdir of ACSSW
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/

#export CLASSPATH="/usr/share/java/*:/usr/local/share/java/*:/home/almamgr/ACS-2017.02/JacORB/lib/*:/usr/share/java/*/*"

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

%files
%{_usr}/local/lib/python/site-packages/ACSLoggingLog/
%{_usr}/local/lib/python/site-packages/ACSLoggingLog__POA/
%{_usr}/local/lib/python/site-packages/AcsLogLevels/
%{_usr}/local/lib/python/site-packages/AcsLogLevels__POA/
%{_usr}/local/lib/python/site-packages/Logging/
%{_usr}/local/lib/python/site-packages/Logging__POA/
%{_usr}/local/lib/python/site-packages/logging_idl_idl.py*

%{_usr}/local/share/java/DsLogAdmin.jar
%{_usr}/local/share/java/logging_idl.jar

%{_usr}/local/%{_lib}/liblogging_idlStubs.so

%changelog
* Wed May 24 2017 Marcelo Jara <mijara@alumnos.inf.utfsm.cl> - 0.1-1
Initial Packaging
