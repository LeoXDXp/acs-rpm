Name:		log4cpp-ACS
Version:	1.0.2017.02
Release:	1%{?dist}
Summary:	Old version of log4cpp with ACS patches
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
Source1:	Makefile-log4cpp
Source2:	MakefileTools-log4cpp

%description
Castor package patched for ACS. Patch modifies messages and levels.

%prep
%setup -q

%build
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/Makefile
cp -f %{SOURCE2} %{_builddir}/%{name}-%{version}/LGPL/Tools/Makefile
# Basic path
mkdir -p  %{_builddir}/home/almamgr
# Symlink for build log
ln -s %{_builddir}/home/almamgr %{_builddir}/alma
# Env Vars for installing. 
#source %{_sysconfdir}/profile.d/acscb.sh
#source %{_sysconfdir}/profile.d/acscb-gnu.sh

export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export OSYSTEM="Linux"

# Compilation specific env vars
export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

cd %{_builddir}/%{name}-%{version}/
# mkdir of ACSSW
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/

make

%install

mkdir -p %{buildroot}/%{_usr}/local/share/java/
mv %{_builddir}/%{name}-%{version}/LGPL/Tools/log4cpp/lib/log4cpp.jar %{buildroot}/%{_usr}/local/share/java/log4cpp-ACS.jar

# Clean symlink in builddir
unlink %{_builddir}/alma

%files
%{_usr}/local/share/java/log4cpp-ACS.jar

%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
