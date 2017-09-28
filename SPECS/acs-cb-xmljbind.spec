Name:		ACS-xmljbind
Version:	2017.06
Release:	1%{?dist}
Summary:	ACS XML Java Interface
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
Source1:	Makefile-xmljbind
BuildRequires:	ACS-Tools-Kit-Benchmark-devel >= %{version} ACS-jacsutil >= %{version} castor-ACS >= 0.9.6.%{version}
Requires:	ACS-Tools-Kit-Benchmark >= %{version} ACS-jacsutil >= %{version}

%description
ACS Community Branch Java interface for XML

%prep
%setup -q

%build
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/Makefile
# FieldInfoFactory inside folder patch.
#sed -i 's/org\.exolab\.castor\.builder\.FieldInfoFactory/org\.exolab\.castor\.builder\.factory\.FieldInfoFactory/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/xmljbind/src/alma/tools/entitybuilder/CastorBuilder.java

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
export ACS_CDB="$ALMASW_ROOTDIR/$ALMASW_RELEASE/config/defaultCDB"
export CLASSPATH=":/usr/share/java/ant.jar:/usr/local/share/java/jACSUtil.jar:/usr/local/share/java/castor-ACS.jar"
#export CLASSPATH=":/usr/share/java/ant.jar:/usr/share/java/castor/castor-xml.jar:/usr/share/java/castor/castor-xml-schema.jar:/usr/share/java/castor/castor-codegen.jar:/usr/share/java/castor/castor-core.jar:%{_usr}/local/share/java/jACSUtil.jar:"
export PATH="$PATH:%{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/"

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
ln -s /home/almamgr/ACS-%{version}/ACSSW/lib/libtatlib.tcl/ %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/xmljbind/lib/
ln -s /home/almamgr/ACS-%{version}/ACSSW/lib/libtatlib.tcl/ %{_builddir}/%{name}-%{version}/LGPL/acsBUILD/lib/
export HOST="$HOSTNAME"
export VLTDATA=""
export OSYSTEM="Linux"
export CYGWIN_VER=""
# Classpath for the compilation of xmljbindTest.jar
#export CLASSPATH="$CLASSPATH:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/jacsutil/lib/jACSUtil.jar:/usr/share/java/hamcrest/all.jar:/usr/share/java/junit.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/jacsutil/lib/jACSUtilTest.jar:"
make test


%install

mkdir -p %{buildroot}/%{_usr}/local/share/java/
mv %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/lib/xmljbind.jar %{buildroot}/%{_usr}/local/share/java/

# Clean symlink in builddir
unlink %{_builddir}/alma

%files
%{_usr}/local/share/java/xmljbind.jar

%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
