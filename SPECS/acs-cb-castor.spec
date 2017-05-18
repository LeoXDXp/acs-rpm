Name:		castor-ACS
Version:	0.9.6.2017.02
Release:	1%{?dist}
Summary:	Old version of Castor with ACS patches
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
Source1:	Makefile-castor
Source2:	MakefileTools-castor
#BuildRequires:	ACS-Tools-Kit-Benchmark-devel >= %{version}
#Requires:	ACS-Tools-Kit-Benchmark >= %{version}

%description
Castor package patched for ACS

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
source %{_sysconfdir}/profile.d/acscb.sh
source %{_sysconfdir}/profile.d/acscb-gnu.sh
source %{_sysconfdir}/profile.d/acscb-tcltk.sh
source %{_sysconfdir}/profile.d/ant.sh

export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export CLASSPATH="$CLASSPATH:/usr/share/java/xerces-j2.jar:/usr/share/java/apache-commons-logging.jar:/usr/share/java/jakarta-oro.jar"

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
mv %{_builddir}/%{name}-%{version}/LGPL/Tools/castor/lib/castor.jar %{buildroot}/%{_usr}/local/share/java/castor-ACS.jar

# Clean symlink in builddir
unlink %{_builddir}/alma

%files
%{_usr}/local/share/java/castor-ACS.jar

%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
