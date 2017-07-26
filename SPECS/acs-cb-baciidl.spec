Name:		ACS-baciidl
Version:	2017.02
Release:	1%{?dist}
Summary:	ACS BACI IDL Declarations
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
Source1:	Makefile-baciidl
BuildRequires:	ACS-Tools-Kit-Benchmark-devel >= %{version} ACS-acserr >= %{version} ACS-acscomponentidl-devel >= %{version}
Requires:	ACS-Tools-Kit-Benchmark >= %{version}

%description
ACS Baci IDL Java (Jar), C++ (Shared Object) and Python Interfaces

%package devel
Summary: ACS Baci IDL Objects (Stubs-Skeletons)
License: LGPL

%description devel
IDL object output: .h,.cpp,.inl,.o Stubs and Skeletons

%prep
%setup -q

%build
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/Makefile

# Basic path
mkdir -p  %{_builddir}/home/almamgr
# Symlink for build log
ln -s %{_builddir}/home/almamgr %{_builddir}/alma
# Symlink for acserrGenIDL, acserrGenCPP and acserrCheckXML
cp -f %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/config/XSDIncludeDependencies.xml %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/config/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/config/AES2IDL.xslt %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/config/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/config/AES2CPP.xslt %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/config/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/config/AES2H.xslt %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/config/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/config/AES2Java.xslt %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/config/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/config/AES2Py.xslt %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/config/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/idl/ACSError.xsd %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/idl/

# IDL files needed by baciidl
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserridl/ws/idl/acserr.idl %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/idl/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acscomponentidl/ws/idl/acscomponent.idl %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/idl/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/idl/acscommon.idl %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/idl/
# Hack to look inside the same folder. acserr seems not needed to be installed on the end system as its only for development
sed -i 's/<acserr.idl>/\"acserr.idl\"/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/idl/acscommon.idl
# Similar Hack of AES2IDL
sed -i 's/&lt;acserr.idl&gt;/"acserr.idl"/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/config/AES2IDL.xslt

# ACSerr stuff 
mkdir -p %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/
ln -s %{_usr}/local/share/java/acserr.jar %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/
ln -s %{_usr}/local/%{_lib}/libacserr.so %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/
ln -s %{_usr}/local/%{_lib}/libacserrStubs.so %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/
mkdir -p %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/acserrExceptionManager.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/acserrACSbaseExImpl.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/acserr.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/acserrLegacy.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/acserrGenExport.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
#cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/ %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/


# ACScomponentIDL stuff
cp -f %{_usr}/local/include/acscomponentC.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
# Logging Stuff
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/logging.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingGetLogger.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/

# The result of using pyxbgen is bindings.py, which is renamed to commontypes.py for ACS.
#pyxbgen -u %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/idl/ACSError.xsd -m ACSError --archive-to-file %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSError.wxs

export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export ACS_CDB="$ALMASW_ROOTDIR/$ALMASW_RELEASE/config/defaultCDB"
#export CLASSPATH=":/usr/share/java/:/usr/share/java/xalan-j2.jar:/usr/share/java/xalan-j2-serializer.jar"
#export IDL_PATH="$IDL_PATH:-I%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/idl/"

# Compilation specific env vars
export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

cd %{_builddir}/%{name}-%{version}/
# mkdir of ACSSW
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/

make

# TAT Stuff. Symlink to libtatlib.tcl/ folder
ln -s /home/almamgr/ACS-%{version}/ACSSW/lib/libtatlib.tcl/ %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/
ln -s /home/almamgr/ACS-%{version}/ACSSW/lib/libtatlib.tcl/ %{_builddir}/%{name}-%{version}/LGPL/acsBUILD/lib/
export HOST="$HOSTNAME"
export VLTDATA=""
export OSYSTEM="Linux"
export CYGWIN_VER=""
make test


# Clean symlink in builddir
unlink %{_builddir}/alma

%install
# Instalation on usr local, if python, then python/site-packages, if C/C++, then include, if Java, then share/java 
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/python/site-packages/acscommon/ %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/python/site-packages/acscommon__POA/ %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/python/site-packages/acscommon_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/

cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/python/site-packages/log_audience/ %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/python/site-packages/log_audience__POA/ %{buildroot}%{_usr}/local/lib/python/site-packages/

cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/python/site-packages/ACS/ %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/python/site-packages/ACS__POA/ %{buildroot}%{_usr}/local/lib/python/site-packages/

mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/commontypes/
cp -f %{_builddir}/%{name}-%{version}/binding.py %{buildroot}%{_usr}/local/lib/python/site-packages/commontypes/commontypes.py

mkdir -p %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/commontypes.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/acscommon.jar %{buildroot}%{_usr}/local/share/java/

mkdir -p %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/libacscommonStubs.so %{buildroot}%{_usr}/local/%{_lib}/
chmod 755 %{buildroot}%{_usr}/local/%{_lib}/libacscommonStubs.so
# Clean
cd %{buildroot}%{_usr}/local/lib/python/site-packages/
find -name "*.pyo" | xargs rm -rf

# Devel Stuff
mkdir -p %{buildroot}%{_usr}/local/include/
# unlink acserrC.h
unlink %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/object/acserrC.h
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/object/*.h %{buildroot}%{_usr}/local/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/object/*.cpp %{buildroot}%{_usr}/local/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/object/*.inl %{buildroot}%{_usr}/local/include/

%files
%{_usr}/local/lib/python/site-packages/acscommon/
%{_usr}/local/lib/python/site-packages/acscommon__POA/
%{_usr}/local/lib/python/site-packages/acscommon_idl.py*
%{_usr}/local/lib/python/site-packages/log_audience/
%{_usr}/local/lib/python/site-packages/log_audience__POA/
%{_usr}/local/lib/python/site-packages/ACS/
%{_usr}/local/lib/python/site-packages/ACS__POA/
%{_usr}/local/lib/python/site-packages/commontypes/commontypes.py*

%{_usr}/local/share/java/commontypes.jar
%{_usr}/local/share/java/acscommon.jar
%{_usr}/local/%{_lib}/libacscommonStubs.so

%files devel
%{_usr}/local/include/acscommonC.cpp
%{_usr}/local/include/acscommonC.h
%{_usr}/local/include/acscommonC.inl
%{_usr}/local/include/acscommonS.cpp
%{_usr}/local/include/acscommonS.h
%{_usr}/local/include/acscommonS_T.cpp
%{_usr}/local/include/acscommonS_T.h

%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
