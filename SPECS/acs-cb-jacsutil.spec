Name:		ACS-jacsutil
Version:	2017.02
Release:	1%{?dist}
Summary:	Java ACS util
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
Source1:	Makefile-jacsutil
Source2:	javahelp-2.0.05.jar
BuildRequires:	ACS-Tools-Kit-Benchmark-devel >= %{version}
Requires:	ACS-Tools-Kit-Benchmark >= %{version}

%description
ACS Community Branch Java interface for ACS util

%prep
%setup -q

%build
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/Makefile
cp -f %{SOURCE2} %{_builddir}/%{name}-%{version}/
# Basic path
mkdir -p  %{_builddir}/home/almamgr
# Symlink for build log
ln -s %{_builddir}/home/almamgr %{_builddir}/alma
# Env Vars for installing. 
source %{_sysconfdir}/profile.d/acscb.sh
source %{_sysconfdir}/profile.d/acscb-gnu.sh
export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
#export CLASSPATH="/usr/share/java/:/usr/share/local/java/:/usr/share/java/ant.jar:/alma/ACS-%{version}/ACSSW/lib/"
export CLASSPATH="/usr/share/java/apache-commons-lang.jar:/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.131-2.b11.el7_3.x86_64/jre/lib/rt.jar:/usr/share/java/junit.jar:/home/almadevel/LGPL/Tools/hibernate/lib/hibernate-core-4.3.11.Final.jar:%{_builddir}/%{name}-%{version}/javahelp-2.0.05.jar"

# Compilation specific env vars
export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

cd %{_builddir}/%{name}-%{version}/
# mkdir of ACSSW
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/

make

# Remove objects
cd %{_builddir}/alma/ACS-%{version}/ACSSW/
find -name "*.o" | xargs rm -rf

%install

mkdir -p %{buildroot}/home/almamgr/ACS-%{version}/ACSSW/
mv %{_builddir}/home/almamgr/ACS-%{version}/ACSSW %{buildroot}/home/almamgr/ACS-%{version}/
mkdir -p %{buildroot}/%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/javahelp-2.0.05.jar %{buildroot}/%{_usr}/local/share/java/

# Clean symlink in builddir
unlink %{_builddir}/alma

%files
%attr(645,-,-) /home/almamgr/ACS-%{version}/ACSSW/lib/jACSUtil.jar
/home/almamgr/ACS-%{version}/ACSSW/lib/jhall-2.0_05.jar
%{_usr}/local/share/java/javahelp-2.0.05.jar

%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
