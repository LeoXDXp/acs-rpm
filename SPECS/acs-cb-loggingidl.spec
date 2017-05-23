Name:       ACS-loggingidl
Version:    2017.02
Release:    1%{?dist}
Summary:    ACS Logging IDL Declarations
License:    LGPL
URL:        http://csrg-utfsm.github.io
Source0:    %{name}-%{version}.tar.gz
Source1:    Makefile-loggingidl
Source2:    DsLogAdmin.jar
Source3:    TimeBase.jar

%description
ACS logging idl.

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
mkdir -p %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/lib/
cp -f %{SOURCE2} %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/lib/DsLogAdmin.jar

export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export ACS_CDB="$ALMASW_ROOTDIR/$ALMASW_RELEASE/config/defaultCDB"

export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

cd %{_builddir}/%{name}-%{version}/

# mkdir of ACSSW
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/

make
%changelog
* Sat May 23 2017 Maximiliano Osorio <mosorio@inf.utfsm.cl> - 0.1-1
Initial Packaging
