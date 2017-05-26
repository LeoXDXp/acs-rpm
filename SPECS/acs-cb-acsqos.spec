Name:       ACS-acsqos
Version:    2017.02
Release:    1%{?dist}
Summary:    ACS QOS Declarations
License:    LGPL
URL:        http://csrg-utfsm.github.io
Source0:    %{name}-%{version}.tar.gz
Source1:    Makefile-acsqos

%description
ACS QOS.

%prep
%setup -q

#cambiar el makefile solo para el modulo
%build
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/Makefile

# Basic path
mkdir -p  %{_builddir}/home/almamgr
# Symlink for build log
ln -s %{_builddir}/home/almamgr %{_builddir}/alma

export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export ACS_CDB="$ALMASW_ROOTDIR/$ALMASW_RELEASE/config/defaultCDB"
export CLASSPATH=":/usr/share/java/xalan-j2.jar"

export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

cd %{_builddir}/%{name}-%{version}/

# mkdir of ACSSW
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/
mkdir -p %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsQoS/ws/lib/

ln -s /usr/share/java/xalan-j2.jar %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsQoS/ws/lib/
make

%install

#unlink
unlink %{_builddir}/alma

%files

%changelog
* Sat May 23 2017 Maximiliano Osorio <mosorio@inf.utfsm.cl> - 0.1-1
Initial Packaging