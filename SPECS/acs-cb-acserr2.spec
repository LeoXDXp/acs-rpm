Name:		ACS-acserr-2
Version:	2017.02
Release:	1%{?dist}
Summary:	ACS Error Core 2/2
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	ACS-acserr-%{version}.tar.gz
Source1:	Makefile-acserr
BuildRequires:	ACS-Tools-Kit-Benchmark-devel >= %{version} castor-ACS ACS-acserridl >= %{version} ACS-xmljbind >= %{version} ACS-jacsutil >= %{version} ACS-loggingidl >= %{version} ACS-logging >= %{version}
Requires:	ACS-Tools-Kit-Benchmark >= %{version}

%description
ACS Error Core 2/2. Provides libacserrHandlersErrStubs.so  libacserr.so  libErrorSystemErrTypeStubs.so, Python's ACSError, ACSErrorChecker.
acserrHandlersErr.jar, acserrj.jar, ACSError.jar, ErrorSystemErrType.jar, xmlvalidator.jar. Also, partial acserrHandlersErr and ErrorSystemErrType python products are in ACS-acserr-1
Package cut in half due to circular dependencies  (acserr->logging->acsutil->baciidl->acserr)

#%package devel
#Name: ACS-acserr-devel-2
#Summary: ACS Error Objects 2/2
#License: LGPL

#%description devel
#Object output: Stub and Skeleton .h, .cpp and .inl for 

%prep
%setup -q

%build
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/Makefile

# Basic path
mkdir -p  %{_builddir}/home/almamgr
# Symlink for build log
ln -s %{_builddir}/home/almamgr %{_builddir}/alma
# As acserr looks for internal acserrGen, fix them as they are fixed in Extprods
sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenIDL

sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenCpp

sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenJava

sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenPython

sed -i 's/`searchFile \/idl\/ACSError\.xsd`/\.\./g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenCheckXML
sed -i 's/$ACSROOT\/lib/\/usr\/local\/share\/java/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenCheckXML

# Hack to look inside the same folder. acserr cant be in a system path if its not yet installed
sed -i 's/&lt;acserr.idl&gt;/"acserr.idl"/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/config/AES2IDL.xslt
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserridl/ws/idl/acserr.idl %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/idl/
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/idl/commontypes.xml %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/idl/
# Changing and extending classpath
sed -i 's/$(ACSROOT)\/lib\/xalan\.jar$(PATH_SEP)$(ACSROOT)\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar:\/usr\/local\/share\/java\/castor-ACS\.jar/g' %{_builddir}/alma/ACS-%{version}/ACSSW/include/acsMakefileCore.mk 
# acserr.jar
mkdir -p %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/
ln -s %{_usr}/local/share/java/acserr.jar %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/
# Not nice stuff in acsMakefileDefinitions.mk
sed -i 's/`acsMakeJavaClasspath`:$(ACSROOT)\/lib\/endorsed\/xercesImpl.jar/\/usr\/share\/java\/xerces-j2.jar:\/usr\/local\/share\/java\/castor-ACS.jar:\/usr\/local\/share\/java\/xmljbind.jar:\/usr\/local\/share\/java\/jACSUtil.jar:\/usr\/share\/java\/apache-commons-logging.jar /g' %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/include/acsMakefileDefinitions.mk

# commontypes.xsd symlink
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/idl/commontypes.xsd %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/idl/
# acserrStubs
ln -s %{_usr}/local/%{_lib}/libacserrStubs.so %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/
# acsutilTimeStamp.h
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/include/acsutilTimeStamp.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# acsutilFindFile.h
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/include/acsutilFindFile.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# acsutil.h
ln -s  %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/include/acsutil.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/

# logging.h
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/logging.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# loggingGetLogger.h
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingGetLogger.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# loggingLogger.h
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingLogger.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# loggingBaseLog.h
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingBaseLog.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# loggingBaseExport.h
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingBaseExport.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# loggingStatistics.h 
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingStatistics.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# loggingHandler.h 
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingHandler.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# loggingACEMACROS.h 
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingACEMACROS.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# loggingMACROS.h
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingMACROS.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# loggingStopWatch.h
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingStopWatch.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# loggingLogTrace.h 
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingLogTrace.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# loggingLogSvcHandler.h
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingLogSvcHandler.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# loggingExport.h
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingExport.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# loggingLoggingProxy.h
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingLoggingProxy.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# loggingLoggingTSSStorage.h
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingLoggingTSSStorage.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# loggingLogThrottle.h
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingLogThrottle.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# loggingThrottleAlarmInterface.h
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingThrottleAlarmInterface.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# loggingACSLogger.h
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingACSLogger.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# loggingCacheLogger.h
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/include/loggingCacheLogger.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/ 
# liblogging.so
ln -s %{_usr}/local/%{_lib}/liblogging.so %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/

# lokiSmrtPnter
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiSmartPtr.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# lokiExport.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiExport.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# lokiSmallObj.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiSmallObj.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# lokiThreads.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiThreads.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# lokiSingleton.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiSingleton.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# lokiTypeManip.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiTypeManip.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# lokiStatic_check.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiStatic_check.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# lokiRefToValue.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiRefToValue.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# lokiConstPolicy.h
ln -s /home/almadevel/LGPL/Tools/loki/ws/include/lokiConstPolicy.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/

export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export ACS_CDB="$ALMASW_ROOTDIR/$ALMASW_RELEASE/config/defaultCDB"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:%{_usr}/local/%{_lib}/"
# Somehow, classpath breaks things, and still gets ignored

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
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/ACSErrorChecker/

cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSErrorChecker/ErrorChecker.py %{buildroot}%{_usr}/local/lib/python/site-packages/ACSErrorChecker/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSErrorChecker/ErrorDefinition.py %{buildroot}%{_usr}/local/lib/python/site-packages/ACSErrorChecker/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSErrorChecker/Subsystem.py %{buildroot}%{_usr}/local/lib/python/site-packages/ACSErrorChecker/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSErrorChecker/__init__.py %{buildroot}%{_usr}/local/lib/python/site-packages/ACSErrorChecker/

mkdir -p %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libacserrHandlersErrStubs.so
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libacserr.so
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libErrorSystemErrTypeStubs.so

chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libacserrHandlersErrStubs.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libacserr.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libErrorSystemErrTypeStubs.so

%files
%{_usr}/local/lib/python/site-packages/ACSErrorChecker/ErrorChecker.py
%{_usr}/local/lib/python/site-packages/ACSErrorChecker/ErrorDefinition.py
%{_usr}/local/lib/python/site-packages/ACSErrorChecker/Subsystem.py
%{_usr}/local/lib/python/site-packages/ACSErrorChecker/__init__.py

%{_usr}/local/%{_lib}/libacserrHandlersErrStubs.so
%{_usr}/local/%{_lib}/libacserr.so
%{_usr}/local/%{_lib}/libErrorSystemErrTypeStubs.so

%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
