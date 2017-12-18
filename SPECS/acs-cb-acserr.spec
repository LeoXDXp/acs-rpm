%define minVersion 2017.06

Name:		ACS-acserr
Version:	2017.08
Release:	1%{?dist}
Summary:	ACS Error Core
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
Source1:	Makefile-acserr
#Source2:	liblogging.so
BuildRequires:	ACS-Tools-Kit-Benchmark-devel >= %{minVersion} castor-ACS ACS-acserridl >= %{version} ACS-xmljbind >= %{version} ACS-jacsutil >= %{version} ACS-loggingidl >= %{version} ACS-acsutil >= %{version} ACS-logging >= %{version}
Requires:	ACS-Tools-Kit-Benchmark >= %{minVersion}
Obsoletes:	acserr

%description
ACS Error Core. Provides acserrHandlersErr.jar, acserrj.jar, ACSError.jar, ErrorSystemErrType.jar, xmlvalidator.jar. Pythons acserrHandlersErr and ErrorSystemErrType ACSError, ACSErrorChecker. Shared objects: libacserrHandlersErrStubs.so  libacserr.so  libErrorSystemErrTypeStubs.so

%package devel
Summary: ACS Error Objects
License: LGPL

%description devel
Object output: Stub and Skeleton .h, .cpp and .inl for acserrHandlersErr and ErrorSystemErrType

%prep
%setup -q -n %{name}-%{version}

%build
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/Makefile

# Basic path
rm -rf %{_builddir}/home/almamgr/
mkdir -p  %{_builddir}/home/almamgr
# Symlink for build log
ln -s %{_builddir}/home/almamgr %{_builddir}/alma
# As acserr looks for internal acserrGen, fix them as they are fixed in Extprods
sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenIDL

sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenCpp

sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar:\/usr\/local\/share\/java\/castor-ACS\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenJava

sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenPython

sed -i 's/`searchFile \/idl\/ACSError\.xsd`/\.\./g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenCheckXML
sed -i 's/$ACSROOT\/lib/\/usr\/local\/share\/java/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenCheckXML

# Hack to look inside the same folder. acserr cant be in a system path if its not yet installed
sed -i 's/&lt;acserr.idl&gt;/"acserr.idl"/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/config/AES2IDL.xslt
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserridl/ws/idl/acserr.idl %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/idl/
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/idl/commontypes.xml %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/idl/
# Changing and extending classpath
sed -i 's/$(ACSROOT)\/lib\/xalan\.jar$(PATH_SEP)$(ACSROOT)\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar:\/usr\/local\/share\/java\/castor-ACS\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/include/acsMakefileCore.mk 
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
#ln -s %{_usr}/local/%{_lib}/liblogging_idlStubs.so %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/
ln -s %{_usr}/local/%{_lib}/liblogging.so %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/
#cp -f %{SOURCE2} %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/
# 
ln -s /usr/%{_lib}/libloki.so.0 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libloki.so

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

# acsutil.h
ln -s  %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/include/acsutil.h %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/include/
# acsutil.so
ln -s %{_usr}/local/%{_lib}/libacsutil.so %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/

#Pyxbgen
mkdir -p %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSError/
pyxbgen -u %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/idl/ACSError.xsd -m ACSError --archive-to-file %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSError.wxs
#cp %{_builddir}/%{name}-%{version}/ACSError.py %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSError/ACSError.py

source %{_sysconfdir}/profile.d/tcltk-acs.sh
source %{_sysconfdir}/profile.d/jacorb-acs.sh

export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export ACS_CDB="$ALMASW_ROOTDIR/$ALMASW_RELEASE/config/defaultCDB"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:%{_usr}/local/%{_lib}/"
#export CLASSPATH="$CLASSPATH:/usr/share/java/castor/castor-xml.jar:/usr/share/java/castor/castor-core.jar:/usr/local/share/java/commontypes.jar:/usr/local/share/java/acserr.jar:/usr/local/share/java/jACSUtil.jar:"
export CLASSPATH="$CLASSPATH:/usr/local/share/java/castor-ACS.jar:/usr/local/share/java/commontypes.jar:/usr/local/share/java/acserr.jar:/usr/local/share/java/jACSUtil.jar:"
export PYTHON_ROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/Python"
export PATH="$PATH:%{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src"

# Symlink of Python's compilelall for hardcoded path in make files
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/Python/lib/python2.7/
ln -s %{_usr}/%{_lib}/python2.7/compileall.py %{_builddir}/home/almamgr/ACS-%{version}/Python/lib/python2.7/compileall.py

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
mkdir -p %{_builddir}/home/almamgr/ACS-%{minVersion}/ACSSW/
# Add debug to vpath in acsMakefile line 1810+
sed -i 's/@echo "ERROR: ----> $@  does not exist."; exit 1/@echo "ERROR: ----> $@  does not exist.";/g'  %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/include/acsMakefile

make

# TAT Stuff. Symlink to libtatlib.tcl/ folder
ln -s /home/almamgr/ACS-%{minVersion}/ACSSW/lib/libtatlib.tcl/ %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/
ln -s /home/almamgr/ACS-%{minVersion}/ACSSW/lib/libtatlib.tcl/ %{_builddir}/%{name}-%{version}/LGPL/acsBUILD/lib/
export HOST="$HOSTNAME"
export VLTDATA=""
export OSYSTEM="Linux"
export CYGWIN_VER=""
# Classpath: makes ACSErrTypeTest.jar available
export CLASSPATH="$CLASSPATH:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/ACSErrTypeTest.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/ExmplErrType.jar:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/acserrj.jar:/usr/share/java/junit.jar:"

make test

# Clean symlink in builddir
unlink %{_builddir}/alma

%install
# Instalation on usr local, if python, then python/site-packages, if C/C++, then include, if Java, then share/java 
# ACSErr and ACSErr__POA folders, and acserr_idl.py
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/ACSErrorChecker
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/ACSError
#ACSErr and ACSErr__POA provided by ACS-acserridl
#cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSErr/ %{buildroot}%{_usr}/local/lib/python/site-packages/
#cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSErr__POA/ %{buildroot}%{_usr}/local/lib/python/site-packages/

# Remove objects
cd %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/
find -name "*.pyo" | xargs rm -rf

cp %{_builddir}/%{name}-%{version}/ACSError.py %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSError/ACSError.py
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSError/ %{buildroot}%{_usr}/local/lib/python/site-packages/
touch %{buildroot}%{_usr}/local/lib/python/site-packages/ACSError/__init__.py
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/acserrHandlersErr/ %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/acserrHandlersErr_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/acserrHandlersErr__POA/ %{buildroot}%{_usr}/local/lib/python/site-packages/

cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ErrorSystemErrType_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ErrorSystemErrType/ %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ErrorSystemErrType__POA/ %{buildroot}%{_usr}/local/lib/python/site-packages/

cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSErrorChecker/ErrorChecker.py %{buildroot}%{_usr}/local/lib/python/site-packages/ACSErrorChecker/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSErrorChecker/ErrorDefinition.py %{buildroot}%{_usr}/local/lib/python/site-packages/ACSErrorChecker/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSErrorChecker/Subsystem.py %{buildroot}%{_usr}/local/lib/python/site-packages/ACSErrorChecker/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSErrorChecker/__init__.py %{buildroot}%{_usr}/local/lib/python/site-packages/ACSErrorChecker/

cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ExmplErrType/ %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ExmplErrType_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ExmplErrTypeImpl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ExmplErrType__POA/ %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/_GlobalIDL/ %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/_GlobalIDL__POA/ %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/test_AES2Py.py %{buildroot}%{_usr}/local/lib/python/site-packages/

# Old 
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/acserrOldTest_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSErrOldTypeTest_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
# Test
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/acserrTest_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSErrTypeTest/ %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSErrTypeTest_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSErrTypeTestImpl.py %{buildroot}%{_usr}/local/lib/python/site-packages/

cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/python/site-packages/ACSErrTypeTest__POA/ %{buildroot}%{_usr}/local/lib/python/site-packages/

# Remove objects
cd %{buildroot}%{_usr}/local/lib/python/site-packages/
find -name "*.pyo" | xargs rm -rf

mkdir -p %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/acserrHandlersErr.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/acserrj.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/ACSError.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/ErrorSystemErrType.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/xmlvalidator.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/ExmplErrType.jar %{buildroot}%{_usr}/local/share/java/
# UnitTest jar files
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/acserrjTest.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/acserrOldTest.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/ACSErrOldTypeTest.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/acserrTest.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/ACSErrTypeTest.jar %{buildroot}%{_usr}/local/share/java/

# acserrGen Scripts not installed by ACS-Tools
mkdir -p %{buildroot}%{_usr}/local/bin

cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenCheckXML %{buildroot}%{_usr}/local/bin/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenCpp %{buildroot}%{_usr}/local/bin/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenIDL %{buildroot}%{_usr}/local/bin/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenJava %{buildroot}%{_usr}/local/bin/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenPython %{buildroot}%{_usr}/local/bin/

cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/updateErrDefs.sh %{buildroot}%{_usr}/local/bin/

chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libacserrHandlersErrStubs.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libacserr.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libErrorSystemErrTypeStubs.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libExmplErrType.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libExmplErrTypeStubs.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libacserrOldTestStubs.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libACSErrOldTypeTestStubs.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libacserrTestStubs.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libACSErrTypeTest.so
chmod 755 %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libACSErrTypeTestStubs.so

mkdir -p %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libacserrHandlersErrStubs.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libacserr.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libErrorSystemErrTypeStubs.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libExmplErrType.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libExmplErrTypeStubs.so %{buildroot}%{_usr}/local/%{_lib}/

# Old stuff
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libacserrOldTestStubs.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libACSErrOldTypeTestStubs.so %{buildroot}%{_usr}/local/%{_lib}/
# Test stuff
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libacserrTestStubs.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libACSErrTypeTest.so %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libACSErrTypeTestStubs.so %{buildroot}%{_usr}/local/%{_lib}/

#.a 
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libacserrHandlersErrStubs.a %{buildroot}%{_usr}/local/%{_lib}/
# Old .a
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libacserrOldTestStubs.a %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libACSErrOldTypeTestStubs.a %{buildroot}%{_usr}/local/%{_lib}/
# Test .a
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libacserrTestStubs.a %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libACSErrTypeTest.a %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libACSErrTypeTestStubs.a %{buildroot}%{_usr}/local/%{_lib}/

# Devel Stuff
mkdir -p %{buildroot}%{_usr}/local/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/object/*.h %{buildroot}%{_usr}/local/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/object/*.cpp %{buildroot}%{_usr}/local/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/object/*.inl %{buildroot}%{_usr}/local/include/

%files
%{_usr}/local/lib/python/site-packages/acserrHandlersErr_idl.py*
%{_usr}/local/lib/python/site-packages/acserrHandlersErr/
%{_usr}/local/lib/python/site-packages/acserrHandlersErr__POA/
%{_usr}/local/lib/python/site-packages/ErrorSystemErrType_idl.py*
%{_usr}/local/lib/python/site-packages/ErrorSystemErrType/
%{_usr}/local/lib/python/site-packages/ErrorSystemErrType__POA/
%{_usr}/local/lib/python/site-packages/ACSErrorChecker/ErrorChecker.py*
%{_usr}/local/lib/python/site-packages/ACSErrorChecker/ErrorDefinition.py*
%{_usr}/local/lib/python/site-packages/ACSErrorChecker/Subsystem.py*
%{_usr}/local/lib/python/site-packages/ACSErrorChecker/__init__.py*
%{_usr}/local/lib/python/site-packages/ExmplErrType/
%{_usr}/local/lib/python/site-packages/ExmplErrType_idl.py*
%{_usr}/local/lib/python/site-packages/ExmplErrTypeImpl.py*
%{_usr}/local/lib/python/site-packages/ExmplErrType__POA/
%{_usr}/local/lib/python/site-packages/_GlobalIDL/
%{_usr}/local/lib/python/site-packages/_GlobalIDL__POA/
%{_usr}/local/lib/python/site-packages/test_AES2Py.py*

%{_usr}/local/lib/python/site-packages/acserrOldTest_idl.py*
%{_usr}/local/lib/python/site-packages/ACSErrOldTypeTest_idl.py*
%{_usr}/local/lib/python/site-packages/ACSError/

%{_usr}/local/lib/python/site-packages/acserrTest_idl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypeTest/
%{_usr}/local/lib/python/site-packages/ACSErrTypeTest_idl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypeTestImpl.py*
%{_usr}/local/lib/python/site-packages/ACSErrTypeTest__POA/

%{_usr}/local/share/java/acserrHandlersErr.jar
%{_usr}/local/share/java/acserrj.jar
%{_usr}/local/share/java/ACSError.jar
%{_usr}/local/share/java/ErrorSystemErrType.jar
%{_usr}/local/share/java/xmlvalidator.jar
%{_usr}/local/share/java/ACSErrOldTypeTest.jar
%{_usr}/local/share/java/ACSErrTypeTest.jar
%{_usr}/local/share/java/ExmplErrType.jar
%{_usr}/local/share/java/acserrOldTest.jar
%{_usr}/local/share/java/acserrTest.jar
%{_usr}/local/share/java/acserrjTest.jar

%{_usr}/local/%{_lib}/libacserrHandlersErrStubs.so
%{_usr}/local/%{_lib}/libacserr.so
%{_usr}/local/%{_lib}/libErrorSystemErrTypeStubs.so
%{_usr}/local/%{_lib}/libACSErrOldTypeTestStubs.so
%{_usr}/local/%{_lib}/libACSErrTypeTest.so
%{_usr}/local/%{_lib}/libACSErrTypeTestStubs.so
%{_usr}/local/%{_lib}/libExmplErrType.so
%{_usr}/local/%{_lib}/libExmplErrTypeStubs.so
%{_usr}/local/%{_lib}/libacserrOldTestStubs.so
%{_usr}/local/%{_lib}/libacserrTestStubs.so

%attr(645,-,-) %{_usr}/local/bin/acserrGenCheckXML
%attr(645,-,-) %{_usr}/local/bin/acserrGenCpp
%attr(645,-,-) %{_usr}/local/bin/acserrGenIDL
%attr(645,-,-) %{_usr}/local/bin/acserrGenJava
%attr(645,-,-) %{_usr}/local/bin/acserrGenPython

%files devel
%{_usr}/local/include/acserrHandlersErrC.cpp
%{_usr}/local/include/acserrHandlersErrC.h
%{_usr}/local/include/acserrHandlersErrC.inl
%{_usr}/local/include/acserrHandlersErrS.cpp
%{_usr}/local/include/acserrHandlersErrS.h
%{_usr}/local/include/ErrorSystemErrTypeC.cpp
%{_usr}/local/include/ErrorSystemErrTypeC.h
%{_usr}/local/include/ErrorSystemErrTypeC.inl
%{_usr}/local/include/ErrorSystemErrTypeS.cpp
%{_usr}/local/include/ErrorSystemErrTypeS.h
%{_usr}/local/include/ACSErrOldTypeTestC.cpp
%{_usr}/local/include/ACSErrOldTypeTestC.h
%{_usr}/local/include/ACSErrOldTypeTestC.inl
%{_usr}/local/include/ACSErrOldTypeTestS.cpp
%{_usr}/local/include/ACSErrOldTypeTestS.h
%{_usr}/local/include/ACSErrTypeTest.cpp
%{_usr}/local/include/ACSErrTypeTest.h
%{_usr}/local/include/ACSErrTypeTestC.cpp
%{_usr}/local/include/ACSErrTypeTestC.h
%{_usr}/local/include/ACSErrTypeTestC.inl
%{_usr}/local/include/ACSErrTypeTestS.cpp
%{_usr}/local/include/ACSErrTypeTestS.h
%{_usr}/local/include/ExmplErrType.cpp
%{_usr}/local/include/ExmplErrType.h
%{_usr}/local/include/ExmplErrTypeC.cpp
%{_usr}/local/include/ExmplErrTypeC.h
%{_usr}/local/include/ExmplErrTypeC.inl
%{_usr}/local/include/ExmplErrTypeS.cpp
%{_usr}/local/include/ExmplErrTypeS.h
%{_usr}/local/include/acserrOldTestC.cpp
%{_usr}/local/include/acserrOldTestC.h
%{_usr}/local/include/acserrOldTestC.inl
%{_usr}/local/include/acserrOldTestS.cpp
%{_usr}/local/include/acserrOldTestS.h
%{_usr}/local/include/acserrTestC.cpp
%{_usr}/local/include/acserrTestC.h
%{_usr}/local/include/acserrTestC.inl
%{_usr}/local/include/acserrTestS.cpp
%{_usr}/local/include/acserrTestS.h

%attr(645,-,-) %{_usr}/local/bin/updateErrDefs.sh

%{_usr}/local/%{_lib}/libacserrHandlersErrStubs.a
%{_usr}/local/%{_lib}/libacserrOldTestStubs.a
%{_usr}/local/%{_lib}/libACSErrOldTypeTestStubs.a
%{_usr}/local/%{_lib}/libacserrTestStubs.a
%{_usr}/local/%{_lib}/libACSErrTypeTest.a
%{_usr}/local/%{_lib}/libACSErrTypeTestStubs.a

%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
