Name:		ACS-jacsutil
Version:	2017.06
Release:	1%{?dist}
Summary:	Java ACS util
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
Source1:	Makefile-jacsutil
Source2:	javahelp-2.0.05.jar
BuildRequires:	ACS-Tools-Kit-Benchmark-devel >= %{version}
Requires:	ACS-Tools-Kit-Benchmark >= %{version}
Obsoletes:	jacsutil

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
source %{_sysconfdir}/profile.d/acscb-toolsKit.sh
source %{_sysconfdir}/profile.d/acscb-gnu.sh
source %{_sysconfdir}/profile.d/tcltk-acs.sh
source %{_sysconfdir}/profile.d/ant.sh

export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export CLASSPATH="/usr/share/java/apache-commons-lang.jar:/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.131-2.b11.el7_3.x86_64/jre/lib/rt.jar:/usr/share/java/junit.jar:/home/almadevel/LGPL/Tools/hibernate/lib/hibernate-core-4.3.11.Final.jar:%{_builddir}/%{name}-%{version}/javahelp-2.0.05.jar:/usr/lib/jvm/java/lib/tools.jar"
export PATH="$PATH:%{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src"

# Remove acsMakeJavaClasspath
echo '#!/usr/bin/env perl' > %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath
echo 'print $ENV{CLASSPATH}' >> %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath
chmod +x %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath

# Compilation specific env vars
export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

cd %{_builddir}/%{name}-%{version}/
# mkdir of ACSSW
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/

make

# TAT Stuff. Symlink to libtatlib.tcl/ folder
ln -s /home/almamgr/ACS-%{version}/ACSSW/lib/libtatlib.tcl/ %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/jacsutil/lib/
ln -s /home/almamgr/ACS-%{version}/ACSSW/lib/libtatlib.tcl/ %{_builddir}/%{name}-%{version}/LGPL/acsBUILD/lib/
export HOST="$HOSTNAME"
export VLTDATA=""
export OSYSTEM="Linux"
export CYGWIN_VER=""
# Classpath for the compilation of jACSutilTest.jar
export CLASSPATH="$CLASSPATH:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/jacsutil/lib/jACSUtil.jar:/usr/share/java/hamcrest/all.jar:/usr/share/java/junit.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/jacsutil/lib/jACSUtilTest.jar:"
# PATH_SEP variable is useless and needs replacement. Setting Classpath where not very useful function was. Better to centraly manage dependencies
sed -i 's/`getJarFile jACSUtil.jar`/${CLASSPATH}/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/jacsutil/test/doAllTests
sed -i 's/${PATH_SEP}/:/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/jacsutil/test/doAllTests
# seems make test can be replaced with sh doAllTest in %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/jacsutil/test/ directly
make test


# Remove objects
#cd %{_builddir}/alma/ACS-%{version}/ACSSW/
#find -name "*.o" | xargs rm -rf

%install

#mkdir -p %{buildroot}/home/almamgr/ACS-%{version}/ACSSW/lib
mkdir -p %{buildroot}/%{_usr}/local/share/java/
mv %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/jacsutil/lib/*.jar %{buildroot}/%{_usr}/local/share/java/
mkdir -p %{buildroot}/%{_usr}/local/share/java/
cp %{_builddir}/%{name}-%{version}/javahelp-2.0.05.jar %{buildroot}/%{_usr}/local/share/java/

mkdir -p %{buildroot}/%{_usr}/local/bin/
cp %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/jacsutil/bin/* %{buildroot}/%{_usr}/local/bin/

# Clean symlink in builddir
unlink %{_builddir}/alma

%post
ln -s %{_usr}/local/share/java/jACSUtil.jar ${ACSROOT}/lib/

%preun
unlink ${ACSROOT}/lib/jACSUtil.jar

%files
%{_usr}/local/share/java/jACSUtil.jar
%{_usr}/local/share/java/jACSUtilTest.jar
%{_usr}/local/share/java/jhall-2.0_05.jar
%{_usr}/local/share/java/javahelp-2.0.05.jar

%{_usr}/local/bin/acsExtractJavaSources
%{_usr}/local/bin/acsJarPackageInfo
%{_usr}/local/bin/acsJarsearch
%{_usr}/local/bin/acsJarSignInfo
%{_usr}/local/bin/acsJarUnsign
%{_usr}/local/bin/acsJavaHelp
%{_usr}/local/bin/doAllTests

%changelog
* Sat Aug 19 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Updating version
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
