Name:		ACS
Version:	2015.4
Release:	1%{?dist}
Summary:	ACS CB for CentOS 7	

Group:		
License:	
URL:		
#Source0:	http://acs-community.github.io/
Source0:	%{name}-%{version}.tar.gz
#Source1:	http://archive.eclipse.org/eclipse/downloads/drops/R-3.6.1-201009090800/eclipse-3.6.1-delta-pack.zip
#Source2:	http://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/R-4.2.2-201302041200/eclipse-4.2.2-delta-pack.zip	
#Source3:	http://archive.eclipse.org/eclipse/downloads/drops/R-3.6.1-201009090800/eclipse-SDK-3.6.1-linux-gtk-x86_64.tar.gz
#Source4:	http://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/R-4.2.2-201302041200/eclipse-SDK-4.2.2-linux-gtk-x86_64.tar.gz
#Source5:	http://www.jacorb.org/releases/3.6/jacorb-3.6-source.zip

BuildArch: x86_64
BuildRequires:	java-1.8.0-openjdk java-1.8.0-openjdk-devel java-1.8.0-openjdk-demo ksh blas-devel gcc expat-devel gcc gcc-c++ gcc-gfortran make byacc patch vim subversion libX11-devel ncurses-devel readline gdbm gdbm-devel bzip2-devel zlib-devel sqlite-devel sqlite2-devel openssl-devel openldap-devel freetype-devel libpng-devel libpng10-devel libxml2-devel libxslt-devel gsl-devel flex xemacs xemacs-packages-extra doxygen autoconf213 autoconf util-linux-ng unzip time log4cpp expat expat21 cppunit cppunit-devel swig castor castor-xml castor-demo shunit2 lockfile-progs xterm lpr ant centos-release
Requires: python procmail lockfile-progs "X Window System" gnome-classic-session gnome-terminal nautilus-open-terminal control-center liberation-mono-fonts setroubleshoot-server 

%description
RPM Installer of ACS-CB 2015.4. It takes the compiled files and installs it on /home/almamgr/ (symlink to /alma). 

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
#%make_install
mkdir -p  %{buildroot}/home/almamgr
mkdir -p %{_usr}/local/bin/
#mkdir -p %{_usr}/local/lib/
mkdir -p %{_usr}/lib64/python2.7/site-packages/
ln -s %{buildroot}/home/almamgr %{buildroot}/alma
cp -r %{_builddir}/%{name}-%{version}/    %{buildroot}/home/almamgr/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/ %{buildroot}/home/almamgr/%{name}-current/
#Binaries ln
# for i in $( find /home/almamgr/ACS-current/LGPL/CommonSoftware/ -type d -name "bin" ); do ln -s $i/* /usr/local/bin/ ;done
# for i in $( find /home/almamgr/ACS-current/LGPL/Kit/ -type d -name "bin" ); do ln -s $i/* /usr/local/bin/ ;done
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsstartup/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdb/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsalarmidl/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acscommandcenter/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftwareacscourse/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsdaemon/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/acsEclipseUtils/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/acssampGUI/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/alarmPanel/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/alarmSourcePanel/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/cdbBrowser/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/errorBrowser/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/eventGUI/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/jlog/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/logLevelGUI/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/logTools/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/objexp/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/ACSLaser/alarm-clients/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acslog/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsncdds/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acspy/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acspyexmpl/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acssim/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsstartup/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsutilpy/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdb/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdbChecker/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdb_rdb/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/codegen/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/containerTests/contNcTest/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jacsutil/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jcont/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jmanager/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/loggingts/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/maci/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/nsStatisticsService/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/task/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/xmlpybind/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/Kit/acs/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/Kit/acstempl/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/Kit/doc/bin/* /usr/local/bin/
#Python Libs 
# A macro must be used so to make this noarch
# for i in $( find /home/almamgr/ACS-current/LGPL/CommonSoftware/ -type d -name "" ); do ln -s $i/* /usr/lib64/python2.7/site-packages/ ;done
# for i in $( find /home/almamgr/ACS-current/LGPL/CommonSoftware/ -type d -name "site-packages" -exec ls  {} \;); do echo unlink /usr/lib64/python2.7/site-packages/$i; done
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/Kit/acs/lib/python/site-packages/* /usr/lib64/python2.7/site-packages/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/acsBUILD/lib/python/site-packages/* /usr/lib64/python2.7/site-packages/
# Shared Objects
# for i in $( find /home/almamgr/ACS-current/LGPL/CommonSoftware/ -type f -name "*.so" ) ; do  ln -s $i /usr/local/lib64/ ; done
# for i in $( find /home/almamgr/ACS-current/LGPL/CommonSoftware/ -type f -name "*.jar" ) ; do  ln -s $i /usr/local/lib64/ ; done -> Needed ?
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/ACSLaser/acs-jms/lib/libACSJMSMessageEntityStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/ACSLaser/alarmCommon/lib/liberrTypeAlarmService.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/ACSLaser/alarmCommon/lib/liberrTypeAlarmServiceStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/ACSLaser/baciPropsTest/lib/libtestComponentStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/ACSLaser/demo/lib/libalsysMountImpl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/ACSLaser/demo/lib/libdemoComponentsStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/ACSLaser/laser-core/lib/libAlarmSystemStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/ACSLaser/laser-source-cpp/lib/liblaserSourceAcsSpecific.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsContainerServices/ws/lib/libJavaContainerError.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsContainerServices/ws/lib/libJavaContainerErrorStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsContainerServices/ws/lib/libacsComponentListener.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsContainerServices/ws/lib/libacsContainerServices.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsContainerServices/ws/lib/libacsErrTypeContainerServices.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsContainerServices/ws/lib/libacsErrTypeContainerServicesStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsContainerServices/ws/lib/libacsErrTypeLifeCycle.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsContainerServices/ws/lib/libacsErrTypeLifeCycleStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/objexp/lib/libobjexpErrType.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/objexp/lib/libobjexpErrTypeStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsQoS/ws/lib/libacsQoS.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsQoS/ws/lib/libacsQoSErrType.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsQoS/ws/lib/libacsQoSErrTypeStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsalarm/lib/libacsAlSysSource.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsalarm/lib/libalSysSource.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsalarm/lib/libalarmSource.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsalarmidl/ws/lib/libAcsAlarmSystemStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsalarmidl/ws/lib/libacsErrTypeAlarmSourceFactory.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsalarmidl/ws/lib/libacsErrTypeAlarmSourceFactoryStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acscomponent/ws/lib/libacsErrTypeComponent.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acscomponent/ws/lib/libacsErrTypeComponentStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acscomponent/ws/lib/libacscomponent.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acscomponentidl/ws/lib/libacscomponentStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acscourse/ws/lib/libACSErrTypeACSCourse.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acscourse/ws/lib/libACSErrTypeACSCourseStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acscourse/ws/lib/libacscourseMount1Impl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acscourse/ws/lib/libacscourseMount2Impl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acscourse/ws/lib/libacscourseMount2LoopImpl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acscourse/ws/lib/libacscourseMount3Impl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acscourse/ws/lib/libacscourseMount4Impl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acscourse/ws/lib/libacscourseMount5Impl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acscourse/ws/lib/libacscourseMountStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsdaemonidl/ws/lib/libacsdaemonErrType.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsdaemonidl/ws/lib/libacsdaemonErrTypeStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsdaemonidl/ws/lib/libacsdaemonStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libErrorSystemErrTypeStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libacserr.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/libacserrHandlersErrStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTICS.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTICSStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTicsTCorr.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTicsTCorrStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeAlarm.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeAlarmStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeCORBA.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeCORBAStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeCommon.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeCommonStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeCppNative.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeCppNativeStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeDevIO.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeDevIOStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeJavaNative.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeJavaNativeStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeMonitor.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeMonitorStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeOK.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypeOKStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypePythonNative.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libACSErrTypePythonNativeStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libPatternAlarmCleared.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libPatternAlarmClearedStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libPatternAlarmTriggered.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserrTypes/ws/lib/libPatternAlarmTriggeredStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserridl/ws/lib/libacserrStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplAmsSeqImpl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplAmsSeqStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplBuildingImpl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplBuildingStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplCalendarImpl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplCalendarStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplCallbacksImpl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplConstrErrorHelloWorld.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplDoorImpl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplErrTest.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplErrTestStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplErrorComponentImpl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplErrorComponentStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplFilterWheelImpl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplFilterWheelStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplFridgeImpl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplFridgeStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplHelloWorldImpl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplHelloWorldStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplInitErrorHelloWorld.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplLampImpl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplLampStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplLampWheelImpl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplLampWheelStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplMountImpl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplMountStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplPowerSupplyImpl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplPowerSupplyStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplRampedPowerSupplyImpl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplRampedPowerSupplyStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/lib/libacsexmplSlowMountImpl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/libacscommonStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acslog/ws/lib/libacslogStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsnc/ws/lib/libacsnc.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsncdds/lib/libacsddsnc.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsncidl/ws/lib/libacsncErrType.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsncidl/ws/lib/libacsncErrTypeStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsncidl/ws/lib/libacsncStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acspy/lib/libacspytestStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acssamp/ws/lib/libacssamp.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acssamp/ws/lib/libacssampStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acssim/lib/libSimulatorStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsstartup/lib/libACSIRSentinelStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acstestcompcpp/lib/libacstestcompErrorExplorer.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acstestcompcpp/lib/libacstestcompStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acstestcompcpp/lib/libacstestcompTimingExplorer.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsthread/ws/lib/libacsThread.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsthread/ws/lib/libacsthreadErrType.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsthread/ws/lib/libacsthreadErrTypeStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acstime/ws/lib/libACSTimeError.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acstime/ws/lib/libACSTimeErrorStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acstime/ws/lib/lib_acstimeSWIG.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acstime/ws/lib/libacsclock.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acstime/ws/lib/libacstime.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acstime/ws/lib/libacstimeStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acstime/ws/lib/libacstimer.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/lib/libacsutil.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/archiveevents/ws/lib/libarchiveevents.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/baci/ws/lib/libbaci.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/libbaciErrTypeDevIO.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/libbaciErrTypeDevIOStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/libbaciErrTypeProperty.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/libbaciErrTypePropertyStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/baciidl/ws/lib/libbaciStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/basenc/ws/lib/libbasenc.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkData/lib/libACSBulkDataError.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkData/lib/libACSBulkDataErrorStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkData/lib/libACSBulkDataStatus.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkData/lib/libACSBulkDataStatusStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkData/lib/libACS_BD_Errors.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkData/lib/libACS_BD_ErrorsStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkData/lib/libbulkDataCallback.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkData/lib/libbulkDataDistributerLib.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkData/lib/libbulkDataDistributerStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkData/lib/libbulkDataReceiverStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkData/lib/libbulkDataSenderStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkData/lib/libbulkDataStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkDataNT/lib/libACSBulkDataError.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkDataNT/lib/libACSBulkDataErrorStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkDataNT/lib/libACSBulkDataStatus.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkDataNT/lib/libACSBulkDataStatusStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkDataNT/lib/libACS_BD_Errors.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkDataNT/lib/libACS_BD_ErrorsStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkDataNT/lib/libACS_DDS_Errors.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkDataNT/lib/libACS_DDS_ErrorsStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkDataNT/lib/libbulkDataDistributerStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkDataNT/lib/libbulkDataReceiverStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkDataNT/lib/libbulkDataSenderStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/bulkDataNT/lib/libbulkDataStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdb/ws/lib/libcdb.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdbidl/ws/lib/libcdbDALStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdbidl/ws/lib/libcdbErrType.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdbidl/ws/lib/libcdbErrTypeStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdbidl/ws/lib/libcdbjDALStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/containerTests/contLogTest/lib/libcontLogTestImpl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/containerTests/contLogTest/lib/libcontLogTest_IFStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/containerTests/contLogTest/lib/libtypeSafeLogsLTS.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/containerTests/contNcTest/lib/libCounterConsumerImpl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/containerTests/contNcTest/lib/libCounterSupplierImpl.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/containerTests/contNcTest/lib/libcontNcTest_IFStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/containerTests/corbaRefPersistenceTest/lib/libHelloWorldStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/containerTests/corbaRefPersistenceTest/lib/libcomponentGetterStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/define/ws/lib/libArchiveIdentifierError.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/define/ws/lib/libArchiveIdentifierErrorStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/define/ws/lib/libarchive_xmlstore_if.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/define/ws/lib/libarchive_xmlstore_ifStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/define/ws/lib/libxmlentity.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/define/ws/lib/libxmlentityStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/enumprop/ws/lib/libenumpropMACROStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/enumprop/ws/lib/libenumpropMACRO_includedStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/enumprop/ws/lib/libenumpropStdStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jcontexmpl/lib/libErrorSystemComponentStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jcontexmpl/lib/libErrorSystemExample.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jcontexmpl/lib/libErrorSystemExampleStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jcontexmpl/lib/libEventComponentStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jcontexmpl/lib/libHelloDemoStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jcontexmpl/lib/libJContExmplErrTypeTest.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jcontexmpl/lib/libJContExmplErrTypeTestStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jcontexmpl/lib/libLampAccessStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jcontexmpl/lib/libLampCallbackStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jcontexmpl/lib/libXmlComponentStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jmanager/lib/libjmanagerErrType.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jmanager/lib/libjmanagerErrTypeStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/lib/libbaselogging.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/lib/liblogging.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/loggingidl/ws/lib/liblogging_idlStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/loggingtsTypes/ws/lib/libAcsContainerLogLTS.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/loggingtsTypes/ws/lib/libAcsNCTraceLogLTS.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/maci/ws/lib/libmaci.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/maci/ws/lib/libmaciClient.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/maciidl/ws/lib/libmaciErrType.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/maciidl/ws/lib/libmaciErrTypeStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/maciidl/ws/lib/libmaciStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/mastercomp/lib/libmastercomp_ifStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/monitoring/moncollect/ws/lib/libMonitorCollector.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/monitoring/monicd/ws/lib/libCollectorListStatusStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/monitoring/monicd/ws/lib/libDAOErrType.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/monitoring/monicd/ws/lib/libDAOErrTypeStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/monitoring/monicd/ws/lib/libMCtestComponentStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/monitoring/monicd/ws/lib/libMonitorArchiverIFStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/monitoring/monicd/ws/lib/libMonitorCollectorStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/monitoring/monicd/ws/lib/libMonitorErr.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/monitoring/monicd/ws/lib/libMonitorErrStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/monitoring/monicd/ws/lib/libTMCDBCOMMON_IDLStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/parameter/lib/libacsXercesUtilities.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/parameter/lib/libparameter.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/recovery/ws/lib/librecovery.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/repeatGuard/ws/lib/libRepeatGuard.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/repeatGuard/ws/lib/libRepeatGuardLogger.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/task/lib/libcharacteristicTask.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/task/lib/libcharacteristicTaskStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/task/lib/libparameterTask.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/task/lib/libstaticContainer.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/task/lib/libtaskComponent.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/task/lib/libtaskComponentStubs.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/task/lib/libtaskErrType.so /usr/local/lib64/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/task/lib/libtaskErrTypeStubs.so /usr/local/lib64/

mkdir -p  %{buildroot}/home/almaproc/introot
%clean


%pre
# Install epel-maven repo
curl https://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -o /etc/yum.repos.d/epel-apache-maven.repo

# ACE-TAO RPM from OpenSUSE
echo "
[ace-tao_opensuse]
name=Latest ACE micro release (CentOS_7)
type=rpm-md
baseurl=http://download.opensuse.org/repositories/devel:/libraries:/ACE:/micro/CentOS_7/
gpgcheck=1
gpgkey=http://download.opensuse.org/repositories/devel:/libraries:/ACE:/micro/CentOS_7//repodata/repomd.xml.key
enabled=0
" > /etc/yum.repos.d/ace-tao.repo

#Local users
useradd -U almamgr
useradd -U almaproc
echo new2me | echo new2me | passwd --stdin almaproc

%post
# Permissions
chown -R almamgr:almamgr /home/almamgr/
chown almaproc:almaproc /home/almaproc/introot/

# Create systemd service
echo "
[Unit]
Description=Alma Common Software CB Service
#Documentation=man:sshd(8) man:sshd_config(5)
After=multi-user.target

[Service]
Type=forking
Environment=INTROOT='/home/almaproc/introot/'
EnvironmentFile=-/home/almamgr/ACS-current/LGPL/acsBUILD/config/.acs/.bash_profile.acs
User=almamgr
ExecPreStart=killACS -q
ExecStart=acsStart
ExecStop=acsStop && acsdataClean --all
ExecReload=cdbjDALClearCache
KillMode=process
#Restart=on-failure
#RestartSec=10s

[Install]
WantedBy=multi-user.target

" > %{_sysconfdir}/systemd/system/acscb.service
systemctl enable acscb.service
systemctl daemon-reload

# Set SELinux PERMISSIVE (Audit mode)
sed -i 's/SELINUX=disabled/SELINUX=permissive/g' %{_sysconfdir}/sysconfig/selinux
sed -i 's/SELINUX=enforcing/SELINUX=permissive/g' %{_sysconfdir}/sysconfig/selinux
setenforce 0

# /etc/hosts
#echo "" >> /etc/hosts

%preun
systemctl stop acscb.service
systemctl disable acscb.service
 
%postun
systemctl daemon-reload
# Al user processes must be killed before userdel
pkill -u almaproc
pkill -u almamgr
userdel -r almamgr
userdel -r almaproc


%files
# find CommonSoftware/ -type d -name "bin" -exec chmod -R +x {} \;
# find Kit/ -type d -name "bin" -exec chmod -R +x {} \;
%doc
%config %{_sysconfdir}/systemd/system/acscb.service
%attr(0705,almagr,almamgr) /home/almamgr/ 
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsstartup/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdb/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsalarmidl/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acscommandcenter/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftwareacscourse/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsdaemon/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/acsEclipseUtils/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/acssampGUI/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/alarmPanel/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/alarmSourcePanel/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/cdbBrowser/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/errorBrowser/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/eventGUI/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/jlog/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/logLevelGUI/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/logTools/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/objexp/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/ACSLaser/alarm-clients/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acslog/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsncdds/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acspy/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acspyexmpl/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acssim/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsstartup/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsutilpy/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdb/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdbChecker/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdb_rdb/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/codegen/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/containerTests/contNcTest/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jacsutil/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jcont/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jmanager/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/loggingts/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/maci/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/nsStatisticsService/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/task/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/xmlpybind/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/Kit/acs/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/Kit/acstempl/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/Kit/doc/bin/*
%attr(-,almaproc,almaproc)/home/almaproc/introot/
%{_usr}/local/bin/*
#%{_usr}/local/lib/*
%{_usr}/lib64/python2.7/site-packages/

%changelog
* Mon Aug 19 2016 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
