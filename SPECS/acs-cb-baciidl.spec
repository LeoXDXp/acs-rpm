Name:		ACS-baciidl
Version:	2017.06
Release:	1%{?dist}
Summary:	ACS BACI IDL Declarations
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
Source1:	Makefile-baciidl
Source2:	CosProperty.jar
BuildRequires:	ACS-Tools-Kit-Benchmark-devel >= %{version} ACS-acserr >= %{version} ACS-acscomponentidl-devel >= %{version} ACS-acscomponentidl >= %{version} ACS-acsidlcommon >= %{version} 
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
ln -s %{_usr}/local/share/java/acscomponent.jar %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/
ln -s %{_usr}/local/%{_lib}/libacscomponentStubs.so %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/
# Logging Stuff
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/logging.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingGetLogger.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingLogger.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingBaseLog.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingBaseExport.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingStatistics.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingHandler.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingACEMACROS.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingMACROS.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingStopWatch.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingLogTrace.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingLogSvcHandler.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingExport.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingLoggingProxy.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingLoggingTSSStorage.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingLogThrottle.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingThrottleAlarmInterface.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingACSLogger.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingCacheLogger.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
#cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/ %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
# ACSutil Stuff
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/include/acsutilTimeStamp.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
# Loki Stuff
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiSmartPtr.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
# lokiExport.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiExport.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
# lokiSmallObj.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiSmallObj.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
# lokiThreads.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiThreads.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
# lokiSingleton.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiSingleton.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
# lokiTypeManip.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiTypeManip.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
# lokiStatic_check.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiStatic_check.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
# lokiRefToValue.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiRefToValue.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
# lokiConstPolicy.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiConstPolicy.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/

# acsutil.h
ln -s  %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/include/acsutil.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/include/
# acscommon.jar and so
ln -s %{_usr}/local/share/java/acscommon.jar %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/
ln -s %{_usr}/local/%{_lib}/libacscommonStubs.so %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/
# CosProperty.idl
ln -s %{_usr}/include/orbsvcs/CosProperty.idl %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/idl/
# CosProperty.jar: Manually created: jar cvf CosProperty.jar org/omg/CosPropertyService/*.class
cp -f %{SOURCE2} %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/CosProperty.jar

# The result of using pyxbgen is bindings.py, which is renamed to commontypes.py for ACS.
#pyxbgen -u %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/idl/ACSError.xsd -m ACSError --archive-to-file %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSError.wxs

# Delete use of acsMakeJavaClasspath on acsMakefileDefinitions.mk, lines 312, and 2 more. Classpath is static and global here
sed -i 's/export CLASSPATH="`acsMakeJavaClasspath`$(PATH_SEP).";//g' %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/include/acsMakefileDefinitions.mk
#sed -i 's/export CLASSPATH;//g' %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/include/acsMakefileDefinitions.mk
#sed -i 's/export CLASSPATH=//g' %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/include/acsMakefileDefinitions.mk
# Dont Exit on false fail of libbaciErrTypePropertyStubs.a does not exist, it does
sed -i 's/@echo "ERROR: ----> $@  does not exist."; exit 1/@echo "ERROR: ----> $@  does not exist.";/g'  %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/include/acsMakefile

export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export ACS_CDB="$ALMASW_ROOTDIR/$ALMASW_RELEASE/config/defaultCDB"
export CLASSPATH="/usr/local/share/java/acscomponent.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/baciErrTypeProperty.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/baciErrTypeDevIO.jar:/usr/local/share/java/acserr.jar:/usr/local/share/java/acserrj.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/acscomponent.jar:/usr/local/share/java/acscommon.jar"

# Remove acsMakeJavaClasspath
echo '#!/usr/bin/env perl' > %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath
echo 'print $ENV{CLASSPATH}' >> %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath
chmod +x %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath

# omniorb acs_python lookup
sed -i 's|-bacs_python|-p %{_builddir}/%{name}-%{version}/LGPL/Tools/extpy/src/ -bacs_python |g' %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/include/acsMakefileDefinitions.mk


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
mkdir -p %{buildroot}%{_usr}/local/bin
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/bin/baciidlPy %{buildroot}%{_usr}/local/bin/

# ACS, ACSErr installed by other acs packages
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/baciErrTypeDevIO
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/baciErrTypeDevIO__POA/
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/baciErrTypeProperty
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/baciErrTypeProperty__POA/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/python/site-packages/baciErrTypeDevIO/__init__.py %{buildroot}%{_usr}/local/lib/python/site-packages/baciErrTypeDevIO/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/python/site-packages/baciErrTypeDevIO_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/python/site-packages/baciErrTypeDevIOImpl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/python/site-packages/baciErrTypeDevIO__POA/__init__.py %{buildroot}%{_usr}/local/lib/python/site-packages/baciErrTypeDevIO__POA/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/python/site-packages/baciErrTypeProperty/__init__.py %{buildroot}%{_usr}/local/lib/python/site-packages/baciErrTypeProperty/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/python/site-packages/baciErrTypeProperty_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/python/site-packages/baciErrTypePropertyImpl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/python/site-packages/baciErrTypeProperty__POA/__init__.py %{buildroot}%{_usr}/local/lib/python/site-packages/baciErrTypeProperty__POA/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/python/site-packages/baci_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/

mkdir -p %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/baciErrTypeDevIO.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/baciErrTypeProperty.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/baci.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/CosProperty.jar %{buildroot}%{_usr}/local/share/java/

mkdir -p %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/libbaciErrTypeDevIO.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/libbaciErrTypeDevIOStubs.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/libbaciErrTypeProperty.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/libbaciErrTypePropertyStubs.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/libbaciStubs.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/libbaciErrTypePropertyStubs.a %{buildroot}%{_usr}/local/%{_lib}/

chmod 755 %{buildroot}%{_usr}/local/%{_lib}/libbaciErrTypeDevIO.so
chmod 755 %{buildroot}%{_usr}/local/%{_lib}/libbaciErrTypeDevIOStubs.so
chmod 755 %{buildroot}%{_usr}/local/%{_lib}/libbaciErrTypeProperty.so
chmod 755 %{buildroot}%{_usr}/local/%{_lib}/libbaciErrTypePropertyStubs.so
chmod 755 %{buildroot}%{_usr}/local/%{_lib}/libbaciStubs.so
chmod 755 %{buildroot}%{_usr}/local/%{_lib}/libbaciErrTypePropertyStubs.a

# Clean
cd %{buildroot}%{_usr}/local/lib/python/site-packages/
find -name "*.pyo" | xargs rm -rf

# Devel Stuff
mkdir -p %{buildroot}%{_usr}/local/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/object/*.h %{buildroot}%{_usr}/local/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/object/*.cpp %{buildroot}%{_usr}/local/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/object/*.inl %{buildroot}%{_usr}/local/include/

%files
%{_usr}/local/lib/python/site-packages/baciErrTypeDevIO/__init__.py*
%{_usr}/local/lib/python/site-packages/baciErrTypeDevIO_idl.py*
%{_usr}/local/lib/python/site-packages/baciErrTypeDevIOImpl.py*
%{_usr}/local/lib/python/site-packages/baciErrTypeDevIO__POA/__init__.py*
%{_usr}/local/lib/python/site-packages/baciErrTypeProperty/__init__.py*
%{_usr}/local/lib/python/site-packages/baciErrTypeProperty_idl.py*
%{_usr}/local/lib/python/site-packages/baciErrTypePropertyImpl.py*
%{_usr}/local/lib/python/site-packages/baciErrTypeProperty__POA/__init__.py*
%{_usr}/local/lib/python/site-packages/baci_idl.py*

%{_usr}/local/share/java/baciErrTypeDevIO.jar
%{_usr}/local/share/java/baciErrTypeProperty.jar
%{_usr}/local/share/java/baci.jar
%{_usr}/local/share/java/CosProperty.jar

%{_usr}/local/%{_lib}/libbaciErrTypeDevIO.so
%{_usr}/local/%{_lib}/libbaciErrTypeDevIOStubs.so
%{_usr}/local/%{_lib}/libbaciErrTypeProperty.so
%{_usr}/local/%{_lib}/libbaciErrTypePropertyStubs.so
%{_usr}/local/%{_lib}/libbaciStubs.so

%{_usr}/local/bin/baciidlPy

%files devel
%{_usr}/local/include/baciC.cpp
%{_usr}/local/include/baciC.h
%{_usr}/local/include/baciC.inl
%{_usr}/local/include/baciErrTypeDevIOC.cpp
%{_usr}/local/include/baciErrTypeDevIOC.h
%{_usr}/local/include/baciErrTypeDevIOC.inl
%{_usr}/local/include/baciErrTypeDevIO.cpp
%{_usr}/local/include/baciErrTypeDevIO.h
%{_usr}/local/include/baciErrTypeDevIOS.cpp
%{_usr}/local/include/baciErrTypeDevIOS.h
%{_usr}/local/include/baciErrTypeDevIOS_T.cpp
%{_usr}/local/include/baciErrTypeDevIOS_T.h
%{_usr}/local/include/baciErrTypePropertyC.cpp
%{_usr}/local/include/baciErrTypePropertyC.h
%{_usr}/local/include/baciErrTypePropertyC.inl
%{_usr}/local/include/baciErrTypeProperty.cpp
%{_usr}/local/include/baciErrTypeProperty.h
%{_usr}/local/include/baciErrTypePropertyS.cpp
%{_usr}/local/include/baciErrTypePropertyS.h
%{_usr}/local/include/baciErrTypePropertyS_T.cpp
%{_usr}/local/include/baciErrTypePropertyS_T.h
%{_usr}/local/include/baciS.cpp
%{_usr}/local/include/baciS.h
%{_usr}/local/include/baciS_T.cpp
%{_usr}/local/include/baciS_T.h

%{_usr}/local/%{_lib}/libbaciErrTypePropertyStubs.a

%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
