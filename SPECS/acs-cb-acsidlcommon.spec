Name:		ACS-acsidlcommon
Version:	2017.02
Release:	1%{?dist}
Summary:	ACS Common IDL Declarations
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
Source1:	Makefile-acsidlcommon
BuildRequires:	ACS-Tools-Kit-Benchmark-devel >= %{version} ACS-acserridl >= %{version} ACS-xmlpybind >= %{version}
Requires:	ACS-Tools-Kit-Benchmark >= %{version}

%description
ACS Common IDL Java (Jar), C++ (Shared Object) and Python Interfaces

%prep
%setup -q

%build
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/Makefile

# Basic path
mkdir -p  %{_builddir}/home/almamgr
# Symlink for build log
ln -s %{_builddir}/home/almamgr %{_builddir}/alma
# Symlink acserr.idl to idl folder in acsidlcommon
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserridl/ws/idl/acserr.idl  %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/idl/
# Symlink acserr.jar to lib folder in acsidlcommon
ln -s %{_usr}/local/share/java/acserr.idl %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/
# Env Vars for installing. 
source %{_sysconfdir}/profile.d/acscb.sh
source %{_sysconfdir}/profile.d/acscb-gnu.sh
source %{_sysconfdir}/profile.d/acscb-tcltk.sh
source %{_sysconfdir}/profile.d/acscb-python.sh
#source %{_sysconfdir}/profile.d/jacorb.sh

export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export ACS_CDB="$ALMASW_ROOTDIR/$ALMASW_RELEASE/config/defaultCDB"
#export CLASSPATH="/usr/share/java/castor/castor-xml.jar:/usr/share/java/castor/castor-xml-schema.jar:/usr/share/java/castor/castor-codegen.jar:/usr/share/java/castor/castor-core.jar"

# Compilation specific env vars
export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

cd %{_builddir}/%{name}-%{version}/
# mkdir of ACSSW
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/

make

%install
# Instalation on usr local, if python, then python/site-packages, if C/C++, then include, if Java, then share/java 
# ACSErr and ACSErr__POA folders, and acserr_idl.py
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/
mv %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserridl/ws/lib/python/site-packages/ACSErr/ %{buildroot}%{_usr}/local/lib/python/site-packages/
mv %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserridl/ws/lib/python/site-packages/ACSErr__POA/ %{buildroot}%{_usr}/local/lib/python/site-packages/
mv %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserridl/ws/lib/python/site-packages/acserr_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/

mkdir -p %{buildroot}%{_usr}/local/share/java/
mv %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserridl/ws/lib/acserr.jar %{buildroot}%{_usr}/local/share/java/

mkdir -p %{buildroot}%{_usr}/local/%{_lib}/
mv %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserridl/ws/lib/libacserrStubs.so %{buildroot}%{_usr}/local/%{_lib}/
# Clean
cd %{buildroot}%{_usr}/local/lib/python/site-packages/
find -name "*.pyo" | xargs rm -rf

# Clean symlink in builddir
unlink %{_builddir}/alma

%files
%{_usr}/local/lib/python/site-packages/ACSErr/
%{_usr}/local/lib/python/site-packages/ACSErr__POA/
%{_usr}/local/lib/python/site-packages/acserr_idl.py*
%{_usr}/local/share/java/acserr.jar
%{_usr}/local/%{_lib}/libacserrStubs.so

%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
