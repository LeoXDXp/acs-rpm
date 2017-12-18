%define minVersion 2017.06

Name:		ACS-acserrTypes
Version:	2017.08
Release:	1%{?dist}
Summary:	ACS Error Core
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
Source1:	Makefile-acserrTypes
BuildRequires:	ACS-acserr >= %{version} ACS-acserridl >= %{version} ACS-Tools-Kit-Benchmark >= %{minVersion}
Requires:	ACS-Tools-Kit-Benchmark >= %{minVersion}

%description
ACS Error Types

%package devel
Summary: ACS Error Types
License: LGPL

%description devel
Object output: Stub and Skeleton .h, .cpp and .inl for ACS Error Types

%prep
%setup -q -n %{name}-%{version}

%build
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/Makefile

# Basic path
rm -rf %{_builddir}/home/almamgr/
mkdir -p  %{_builddir}/home/almamgr
# Symlink for build log
ln -s %{_builddir}/home/almamgr %{_builddir}/alma

cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/idl/ACSError.xsd %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/idl/

mkdir -p %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/config/

#cp -f %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/config/XSDIncludeDependencies.xml %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/config/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/config/AES2IDL.xslt %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/config/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/config/AES2CPP.xslt %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/config/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/config/AES2H.xslt %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/config/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/config/AES2Java.xslt %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/config/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/config/AES2Py.xslt %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/config/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/idl/ACSError.xsd %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/idl/

# As acserr looks for internal acserrGen, fix them as they are fixed in Extprods
sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenIDL
sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenCpp
sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar:\/usr\/local\/share\/java\/castor-ACS\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenJava
sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenPython

sed -i 's/`searchFile \/idl\/ACSError\.xsd`/\.\./g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenCheckXML
sed -i 's/$ACSROOT\/lib/\/usr\/local\/share\/java/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenCheckXML

# Hack to look inside the same folder. acserr cant be in a system path if its not yet installed
sed -i 's/&lt;acserr.idl&gt;/"acserr.idl"/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/config/AES2IDL.xslt
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserridl/ws/idl/acserr.idl %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/idl/
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/idl/commontypes.xml %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/idl/
# acserr Stuff
mkdir -p %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/
mkdir -p %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
ln -s %{_usr}/local/share/java/acserr.jar %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/
ln -s %{_usr}/local/%{_lib}/libacserr.so %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/acserrExceptionManager.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/acserrACSbaseExImpl.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/acserr.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/acserrLegacy.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/acserrGenExport.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/

# acserrStubs
ln -s %{_usr}/local/%{_lib}/libacserrStubs.so %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/

# Logging Stuff
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/logging.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingGetLogger.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingLogger.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingBaseLog.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingBaseExport.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingStatistics.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingHandler.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingACEMACROS.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingMACROS.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingStopWatch.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingLogTrace.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingLogSvcHandler.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingExport.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingLoggingProxy.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingLoggingTSSStorage.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingLogThrottle.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingThrottleAlarmInterface.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingACSLogger.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingCacheLogger.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
# ACSutil Stuff
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/include/acsutilTimeStamp.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
# Loki Stuff
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiSmartPtr.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
# lokiExport.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiExport.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
# lokiSmallObj.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiSmallObj.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
# lokiThreads.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiThreads.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
# lokiSingleton.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiSingleton.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
# lokiTypeManip.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiTypeManip.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
# lokiStatic_check.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiStatic_check.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
# lokiRefToValue.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiRefToValue.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
# lokiConstPolicy.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiConstPolicy.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/
# acsutil.h
ln -s  %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/include/acsutil.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/include/

export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export ACS_CDB="$ALMASW_ROOTDIR/$ALMASW_RELEASE/config/defaultCDB"
#export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:%{_usr}/local/%{_lib}/"
export CLASSPATH="%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTypeOK.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTypeMonitor.jar:%{_usr}/local/share/java/acserr.jar:%{_usr}/local/share/java/acserrj.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTypeAlarm.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTypeCommon.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTypePythonNative.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTypeCppNative.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTypeJavaNative.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTypeCORBA.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTypeDevIO.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTICS.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTicsTCorr.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/PatternAlarmCleared.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/PatternAlarmTriggered.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTypeOK.jar"
export PATH="$PATH:%{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src"

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

# Clean symlink in builddir
unlink %{_builddir}/alma

%install
# Instalation on usr local, if python, then python/site-packages, if C/C++, then include, if Java, then share/java 
# ACSErr and ACSErr__POA folders, and acserr_idl.py
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/
#ACSErr and ACSErr__POA provided by ACS-acserridl

# Remove objects
cd %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/
find -name "*.pyc" | xargs rm -rf

cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTICS %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTICS__POA %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTicsTCorr %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTicsTCorr__POA %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeAlarm %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeAlarm__POA %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeCommon %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeCommon__POA %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeCORBA %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeCORBA__POA %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeCppNative %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeCppNative__POA %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeDevIO %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeDevIO__POA %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeJavaNative %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeJavaNative__POA %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeMonitor %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeMonitor__POA %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeOK %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeOK__POA %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypePythonNative %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypePythonNative__POA %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/PatternAlarmCleared %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/PatternAlarmCleared__POA %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/PatternAlarmTriggered %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/PatternAlarmTriggered__POA %{buildroot}%{_usr}/local/lib/python/site-packages/

cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTICS_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTICSImpl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTicsTCorr_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTicsTCorrImpl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeAlarm_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeAlarmImpl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeCommon_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeCommonImpl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeCORBA_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeCORBAImpl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeCppNative_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeCppNativeImpl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeDevIO_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeDevIOImpl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeJavaNative_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeJavaNativeImpl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeMonitor_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeMonitorImpl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeOK_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypeOKImpl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypePythonNative_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/ACSErrTypePythonNativeImpl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/PatternAlarmCleared_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/PatternAlarmClearedImpl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/PatternAlarmTriggered_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/python/site-packages/PatternAlarmTriggeredImpl.py %{buildroot}%{_usr}/local/lib/python/site-packages/

# Remove objects
cd %{buildroot}%{_usr}/local/lib/python/site-packages/
find -name "*.pyo" | xargs rm -rf

mkdir -p %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTICS.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTicsTCorr.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTypeAlarm.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTypeCommon.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTypeCORBA.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTypeCppNative.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTypeDevIO.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTypeJavaNative.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTypeMonitor.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTypeOK.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/ACSErrTypePythonNative.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/PatternAlarmCleared.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/PatternAlarmTriggered.jar %{buildroot}%{_usr}/local/share/java/

# Shared Objects
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTICS.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTICSStubs.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTicsTCorr.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTicsTCorrStubs.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeAlarm.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeAlarmStubs.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeCommon.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeCommonStubs.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeCORBA.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeCORBAStubs.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeCppNative.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeCppNativeStubs.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeDevIO.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeDevIOStubs.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeJavaNative.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeJavaNativeStubs.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeMonitor.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeMonitorStubs.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeOK.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeOKStubs.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypePythonNative.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypePythonNativeStubs.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libPatternAlarmCleared.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libPatternAlarmClearedStubs.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libPatternAlarmTriggered.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libPatternAlarmTriggeredStubs.so

mkdir -p %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTICS.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTICSStubs.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTicsTCorr.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTicsTCorrStubs.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeAlarm.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeAlarmStubs.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeCommon.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeCommonStubs.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeCORBA.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeCORBAStubs.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeCppNative.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeCppNativeStubs.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeDevIO.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeDevIOStubs.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeJavaNative.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeJavaNativeStubs.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeMonitor.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeMonitorStubs.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeOK.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeOKStubs.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypePythonNative.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypePythonNativeStubs.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libPatternAlarmCleared.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libPatternAlarmClearedStubs.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libPatternAlarmTriggered.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libPatternAlarmTriggeredStubs.so %{buildroot}%{_usr}/local/%{_lib}/


# Devel Stuff
mkdir -p %{buildroot}%{_usr}/local/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/object/*.h %{buildroot}%{_usr}/local/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/object/*.cpp %{buildroot}%{_usr}/local/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/object/*.inl %{buildroot}%{_usr}/local/include/

%files
%{_usr}/local/lib/python/site-packages/ACSErrTICS/
%{_usr}/local/lib/python/site-packages/ACSErrTICS__POA/
%{_usr}/local/lib/python/site-packages/ACSErrTicsTCorr/
%{_usr}/local/lib/python/site-packages/ACSErrTicsTCorr__POA/
%{_usr}/local/lib/python/site-packages/ACSErrTypeAlarm/
%{_usr}/local/lib/python/site-packages/ACSErrTypeAlarm__POA/
%{_usr}/local/lib/python/site-packages/ACSErrTypeCommon/
%{_usr}/local/lib/python/site-packages/ACSErrTypeCommon__POA/
%{_usr}/local/lib/python/site-packages/ACSErrTypeCORBA/
%{_usr}/local/lib/python/site-packages/ACSErrTypeCORBA__POA/
%{_usr}/local/lib/python/site-packages/ACSErrTypeCppNative/
%{_usr}/local/lib/python/site-packages/ACSErrTypeCppNative__POA/
%{_usr}/local/lib/python/site-packages/ACSErrTypeDevIO/
%{_usr}/local/lib/python/site-packages/ACSErrTypeDevIO__POA/
%{_usr}/local/lib/python/site-packages/ACSErrTypeJavaNative/
%{_usr}/local/lib/python/site-packages/ACSErrTypeJavaNative__POA/
%{_usr}/local/lib/python/site-packages/ACSErrTypeMonitor/
%{_usr}/local/lib/python/site-packages/ACSErrTypeMonitor__POA/
%{_usr}/local/lib/python/site-packages/ACSErrTypeOK/
%{_usr}/local/lib/python/site-packages/ACSErrTypeOK__POA/
%{_usr}/local/lib/python/site-packages/ACSErrTypePythonNative/
%{_usr}/local/lib/python/site-packages/ACSErrTypePythonNative__POA/
%{_usr}/local/lib/python/site-packages/PatternAlarmCleared/
%{_usr}/local/lib/python/site-packages/PatternAlarmCleared__POA/
%{_usr}/local/lib/python/site-packages/PatternAlarmTriggered/
%{_usr}/local/lib/python/site-packages/PatternAlarmTriggered__POA/

%{_usr}/local/lib/python/site-packages/ACSErrTICS_idl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTICSImpl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTicsTCorr_idl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTicsTCorrImpl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypeAlarm_idl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypeAlarmImpl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypeCommon_idl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypeCommonImpl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypeCORBA_idl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypeCORBAImpl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypeCppNative_idl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypeCppNativeImpl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypeDevIO_idl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypeDevIOImpl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypeJavaNative_idl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypeJavaNativeImpl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypeMonitor_idl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypeMonitorImpl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypeOK_idl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypeOKImpl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypePythonNative_idl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypePythonNativeImpl.py*
%{_usr}/local/lib/python/site-packages/PatternAlarmCleared_idl.py*
%{_usr}/local/lib/python/site-packages/PatternAlarmClearedImpl.py*
%{_usr}/local/lib/python/site-packages/PatternAlarmTriggered_idl.py*
%{_usr}/local/lib/python/site-packages/PatternAlarmTriggeredImpl.py*

%{_usr}/local/share/java/ACSErrTICS.jar
%{_usr}/local/share/java/ACSErrTicsTCorr.jar
%{_usr}/local/share/java/ACSErrTypeAlarm.jar
%{_usr}/local/share/java/ACSErrTypeCommon.jar
%{_usr}/local/share/java/ACSErrTypeCORBA.jar
%{_usr}/local/share/java/ACSErrTypeCppNative.jar
%{_usr}/local/share/java/ACSErrTypeDevIO.jar
%{_usr}/local/share/java/ACSErrTypeJavaNative.jar
%{_usr}/local/share/java/ACSErrTypeMonitor.jar
%{_usr}/local/share/java/ACSErrTypeOK.jar
%{_usr}/local/share/java/ACSErrTypePythonNative.jar
%{_usr}/local/share/java/PatternAlarmCleared.jar
%{_usr}/local/share/java/PatternAlarmTriggered.jar

%{_usr}/local/%{_lib}/libACSErrTICS.so
%{_usr}/local/%{_lib}/libACSErrTICSStubs.so
%{_usr}/local/%{_lib}/libACSErrTicsTCorr.so
%{_usr}/local/%{_lib}/libACSErrTicsTCorrStubs.so
%{_usr}/local/%{_lib}/libACSErrTypeAlarm.so
%{_usr}/local/%{_lib}/libACSErrTypeAlarmStubs.so
%{_usr}/local/%{_lib}/libACSErrTypeCommon.so
%{_usr}/local/%{_lib}/libACSErrTypeCommonStubs.so
%{_usr}/local/%{_lib}/libACSErrTypeCORBA.so
%{_usr}/local/%{_lib}/libACSErrTypeCORBAStubs.so
%{_usr}/local/%{_lib}/libACSErrTypeCppNative.so
%{_usr}/local/%{_lib}/libACSErrTypeCppNativeStubs.so
%{_usr}/local/%{_lib}/libACSErrTypeDevIO.so
%{_usr}/local/%{_lib}/libACSErrTypeDevIOStubs.so
%{_usr}/local/%{_lib}/libACSErrTypeJavaNative.so
%{_usr}/local/%{_lib}/libACSErrTypeJavaNativeStubs.so
%{_usr}/local/%{_lib}/libACSErrTypeMonitor.so
%{_usr}/local/%{_lib}/libACSErrTypeMonitorStubs.so
%{_usr}/local/%{_lib}/libACSErrTypeOK.so
%{_usr}/local/%{_lib}/libACSErrTypeOKStubs.so
%{_usr}/local/%{_lib}/libACSErrTypePythonNative.so
%{_usr}/local/%{_lib}/libACSErrTypePythonNativeStubs.so
%{_usr}/local/%{_lib}/libPatternAlarmCleared.so
%{_usr}/local/%{_lib}/libPatternAlarmClearedStubs.so
%{_usr}/local/%{_lib}/libPatternAlarmTriggered.so
%{_usr}/local/%{_lib}/libPatternAlarmTriggeredStubs.so

%files devel
%{_usr}/local/include/ACSErrTICSC.cpp
%{_usr}/local/include/ACSErrTICSC.h
%{_usr}/local/include/ACSErrTICSC.inl
%{_usr}/local/include/ACSErrTICS.cpp
%{_usr}/local/include/ACSErrTICS.h
%{_usr}/local/include/ACSErrTICSS.cpp
%{_usr}/local/include/ACSErrTICSS.h
%{_usr}/local/include/ACSErrTicsTCorrC.cpp
%{_usr}/local/include/ACSErrTicsTCorrC.h
%{_usr}/local/include/ACSErrTicsTCorrC.inl
%{_usr}/local/include/ACSErrTicsTCorr.cpp
%{_usr}/local/include/ACSErrTicsTCorr.h
%{_usr}/local/include/ACSErrTicsTCorrS.cpp
%{_usr}/local/include/ACSErrTicsTCorrS.h
%{_usr}/local/include/ACSErrTypeAlarmC.cpp
%{_usr}/local/include/ACSErrTypeAlarmC.h
%{_usr}/local/include/ACSErrTypeAlarmC.inl
%{_usr}/local/include/ACSErrTypeAlarm.cpp
%{_usr}/local/include/ACSErrTypeAlarm.h
%{_usr}/local/include/ACSErrTypeAlarmS.cpp
%{_usr}/local/include/ACSErrTypeAlarmS.h
%{_usr}/local/include/ACSErrTypeCommonC.cpp
%{_usr}/local/include/ACSErrTypeCommonC.h
%{_usr}/local/include/ACSErrTypeCommonC.inl
%{_usr}/local/include/ACSErrTypeCommon.cpp
%{_usr}/local/include/ACSErrTypeCommon.h
%{_usr}/local/include/ACSErrTypeCommonS.cpp
%{_usr}/local/include/ACSErrTypeCommonS.h
%{_usr}/local/include/ACSErrTypeCORBAC.cpp
%{_usr}/local/include/ACSErrTypeCORBAC.h
%{_usr}/local/include/ACSErrTypeCORBAC.inl
%{_usr}/local/include/ACSErrTypeCORBA.cpp
%{_usr}/local/include/ACSErrTypeCORBA.h
%{_usr}/local/include/ACSErrTypeCORBAS.cpp
%{_usr}/local/include/ACSErrTypeCORBAS.h
%{_usr}/local/include/ACSErrTypeCppNativeC.cpp
%{_usr}/local/include/ACSErrTypeCppNativeC.h
%{_usr}/local/include/ACSErrTypeCppNativeC.inl
%{_usr}/local/include/ACSErrTypeCppNative.cpp
%{_usr}/local/include/ACSErrTypeCppNative.h
%{_usr}/local/include/ACSErrTypeCppNativeS.cpp
%{_usr}/local/include/ACSErrTypeCppNativeS.h
%{_usr}/local/include/ACSErrTypeDevIOC.cpp
%{_usr}/local/include/ACSErrTypeDevIOC.h
%{_usr}/local/include/ACSErrTypeDevIOC.inl
%{_usr}/local/include/ACSErrTypeDevIO.cpp
%{_usr}/local/include/ACSErrTypeDevIO.h
%{_usr}/local/include/ACSErrTypeDevIOS.cpp
%{_usr}/local/include/ACSErrTypeDevIOS.h
%{_usr}/local/include/ACSErrTypeJavaNativeC.cpp
%{_usr}/local/include/ACSErrTypeJavaNativeC.h
%{_usr}/local/include/ACSErrTypeJavaNativeC.inl
%{_usr}/local/include/ACSErrTypeJavaNative.cpp
%{_usr}/local/include/ACSErrTypeJavaNative.h
%{_usr}/local/include/ACSErrTypeJavaNativeS.cpp
%{_usr}/local/include/ACSErrTypeJavaNativeS.h
%{_usr}/local/include/ACSErrTypeMonitorC.cpp
%{_usr}/local/include/ACSErrTypeMonitorC.h
%{_usr}/local/include/ACSErrTypeMonitorC.inl
%{_usr}/local/include/ACSErrTypeMonitor.cpp
%{_usr}/local/include/ACSErrTypeMonitor.h
%{_usr}/local/include/ACSErrTypeMonitorS.cpp
%{_usr}/local/include/ACSErrTypeMonitorS.h
%{_usr}/local/include/ACSErrTypeOKC.cpp
%{_usr}/local/include/ACSErrTypeOKC.h
%{_usr}/local/include/ACSErrTypeOKC.inl
%{_usr}/local/include/ACSErrTypeOK.cpp
%{_usr}/local/include/ACSErrTypeOK.h
%{_usr}/local/include/ACSErrTypeOKS.cpp
%{_usr}/local/include/ACSErrTypeOKS.h
%{_usr}/local/include/ACSErrTypePythonNativeC.cpp
%{_usr}/local/include/ACSErrTypePythonNativeC.h
%{_usr}/local/include/ACSErrTypePythonNativeC.inl
%{_usr}/local/include/ACSErrTypePythonNative.cpp
%{_usr}/local/include/ACSErrTypePythonNative.h
%{_usr}/local/include/ACSErrTypePythonNativeS.cpp
%{_usr}/local/include/ACSErrTypePythonNativeS.h
%{_usr}/local/include/PatternAlarmClearedC.cpp
%{_usr}/local/include/PatternAlarmClearedC.h
%{_usr}/local/include/PatternAlarmClearedC.inl
%{_usr}/local/include/PatternAlarmCleared.cpp
%{_usr}/local/include/PatternAlarmCleared.h
%{_usr}/local/include/PatternAlarmClearedS.cpp
%{_usr}/local/include/PatternAlarmClearedS.h
%{_usr}/local/include/PatternAlarmTriggeredC.cpp
%{_usr}/local/include/PatternAlarmTriggeredC.h
%{_usr}/local/include/PatternAlarmTriggeredC.inl
%{_usr}/local/include/PatternAlarmTriggered.cpp
%{_usr}/local/include/PatternAlarmTriggered.h
%{_usr}/local/include/PatternAlarmTriggeredS.cpp
%{_usr}/local/include/PatternAlarmTriggeredS.h


%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
