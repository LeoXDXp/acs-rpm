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
#export CLASSPATH="/usr/share/java/apache-commons-lang.jar:/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.131-2.b11.el7_3.x86_64/jre/lib/rt.jar:/usr/share/java/junit.jar:/home/almadevel/LGPL/Tools/hibernate/lib/hibernate-core-4.3.11.Final.jar:%{_builddir}/%{name}-%{version}/javahelp-2.0.05.jar"

# Compilation specific env vars
export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

cd %{_builddir}/%{name}-%{version}/
# mkdir of ACSSW
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/

make

# TAT Stuff. Symlink to libtatlib.tcl/ folder
#ln -s /home/almamgr/ACS-%{version}/ACSSW/lib/libtatlib.tcl/ %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/jacsutil/lib/
ln -s /home/almamgr/ACS-%{version}/ACSSW/lib/libtatlib.tcl/ %{_builddir}/%{name}-%{version}/LGPL/acsBUILD/lib/
export HOST="$HOSTNAME"
export VLTDATA=""
export OSYSTEM="Linux"
export CYGWIN_VER=""
# Classpath for the compilation of jACSutilTest.jar
#export CLASSPATH="$CLASSPATH:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/jacsutil/lib/jACSUtil.jar:/usr/share/java/hamcrest/all.jar:/usr/share/java/junit.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/jacsutil/lib/jACSUtilTest.jar:"
# PATH_SEP variable is useless and needs replacement. Setting Classpath where not very useful function was. Better to centraly manage dependencies
make test

%install

#mkdir -p %{buildroot}/home/almamgr/ACS-%{version}/ACSSW/lib
mkdir -p %{buildroot}/%{_usr}/local/share/java/
mv %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/jacsutil/lib/*.jar %{buildroot}/%{_usr}/local/share/java/
mkdir -p %{buildroot}/%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/javahelp-2.0.05.jar %{buildroot}/%{_usr}/local/share/java/

# Clean symlink in builddir
unlink %{_builddir}/alma

%files
%{_usr}/local/share/java/jACSUtil.jar

%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
