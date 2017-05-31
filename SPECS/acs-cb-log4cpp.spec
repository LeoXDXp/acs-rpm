Name:		log4cpp-ACS
Version:	1.0.2017.02
Release:	1%{?dist}
Summary:	Old version of log4cpp with ACS patches
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
Source1:	Makefile-log4cpp
Source2:	MakefileTools-log4cpp

%description
Log for C++ is a library of classes for flexible logging to files, syslog,
and other destinations. It is modeled after the Log for Java library and
stays as close to its API as is reasonable.
This package is patched for ACS. Patch modifies messages and levels.

%package devel
Summary: development tools for Log for C++ with ACS patch
Group: Development/Libraries
#Requires: %name = %version

%description devel
The %{name}-devel package contains the static libraries and header files
needed for development with %{name}.

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
#source %{_sysconfdir}/profile.d/acscb.sh
#source %{_sysconfdir}/profile.d/acscb-gnu.sh

export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export OSYSTEM="Linux"

# Compilation specific env vars
export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

cd %{_builddir}/%{name}-%{version}/
# mkdir of ACSSW
#mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/

make

# Clean symlink in builddir
unlink %{_builddir}/alma

%install
# Docs
#mkdir -p %{buildroot}/%{_usr}/local/share/doc/log4cpp-ACS/
#cp -f %{_builddir}/%{name}-%{version}/LGPL/Tools/log4cpp/src/log4cpp-1.0/{AUTHORS,COPYING,INSTALL,NEWS,README,THANKS,ChangeLog} %{buildroot}/%{_usr}/local/share/doc/log4cpp-ACS/

#
mkdir -p %{buildroot}/%{_usr}/local/%{_lib}/
cp -f %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/lib/liblog4cpp.a %{buildroot}/%{_usr}/local/%{_lib}/
cp -f %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/lib/liblog4cpp.la %{buildroot}/%{_usr}/local/%{_lib}/
cp -f %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/lib/liblog4cpp.so.4.0.6 %{buildroot}/%{_usr}/local/%{_lib}/
chmod 755 %{buildroot}/%{_usr}/local/%{_lib}/liblog4cpp.so.4.0.6
chmod 755 %{buildroot}/%{_usr}/local/%{_lib}/liblog4cpp.la

# Devel Stuff
mkdir -p %{buildroot}/%{_usr}/local/include/
cp -f %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/include/log4cpp/*.h* %{buildroot}/%{_usr}/local/include/
cp -rf %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/include/log4cpp/threading/ %{buildroot}/%{_usr}/local/include/

%post

ln -s %{_usr}/local/%{_lib}/liblog4cpp.so.4.0.6 %{_usr}/local/%{_lib}/liblog4cpp.so
ln -s %{_usr}/local/%{_lib}/liblog4cpp.so.4.0.6 %{_usr}/local/%{_lib}/liblog4cpp.so.4

%preun

unlink %{_usr}/local/%{_lib}/liblog4cpp.so
unlink %{_usr}/local/%{_lib}/liblog4cpp.so.4

%files
%attr(755,root,root) %{_usr}/local/%{_lib}/liblog4cpp.so.4.0.6
#%doc %{_usr}/local/share/doc/log4cpp-ACS/

%files devel
#%defattr(-,root,root,755)
#%attr(755,root,root) %prefix/bin/log4cpp-config
#%attr(755,root,root) %prefix/lib/lib*.so
%attr(755,root,root) %{_usr}/local/%{_lib}/liblog4cpp.la
%attr(644,root,root) %{_usr}/local/%{_lib}/liblog4cpp.a

%dir %{_usr}/local/include/log4cpp
%dir %{_usr}/local/include/log4cpp/threading
%{_usr}/local/include/log4cpp/threading/BoostThreads.hh
%{_usr}/local/include/log4cpp/threading/DummyThreads.hh
%{_usr}/local/include/log4cpp/threading/MSThreads.hh
%{_usr}/local/include/log4cpp/threading/OmniThreads.hh
%{_usr}/local/include/log4cpp/threading/PThreads.hh
%{_usr}/local/include/log4cpp/threading/Threading.hh
%{_usr}/local/include/log4cpp/AbortAppender.hh
%{_usr}/local/include/log4cpp/Appender.hh
%{_usr}/local/include/log4cpp/AppendersFactory.hh
%{_usr}/local/include/log4cpp/AppenderSkeleton.hh
%{_usr}/local/include/log4cpp/BasicConfigurator.hh
%{_usr}/local/include/log4cpp/BasicLayout.hh
%{_usr}/local/include/log4cpp/BufferingAppender.hh
%{_usr}/local/include/log4cpp/Category.hh
%{_usr}/local/include/log4cpp/CategoryStream.hh
%{_usr}/local/include/log4cpp/config.h
%{_usr}/local/include/log4cpp/config-openvms.h
%{_usr}/local/include/log4cpp/Configurator.hh
%{_usr}/local/include/log4cpp/config-win32.h
%{_usr}/local/include/log4cpp/convenience.h
%{_usr}/local/include/log4cpp/Export.hh
%{_usr}/local/include/log4cpp/FactoryParams.hh
%{_usr}/local/include/log4cpp/FileAppender.hh
%{_usr}/local/include/log4cpp/Filter.hh
%{_usr}/local/include/log4cpp/FixedContextCategory.hh
%{_usr}/local/include/log4cpp/HierarchyMaintainer.hh
%{_usr}/local/include/log4cpp/IdsaAppender.hh
%{_usr}/local/include/log4cpp/LayoutAppender.hh
%{_usr}/local/include/log4cpp/Layout.hh
%{_usr}/local/include/log4cpp/LayoutsFactory.hh
%{_usr}/local/include/log4cpp/LevelEvaluator.hh
%{_usr}/local/include/log4cpp/LoggingEvent.hh
%{_usr}/local/include/log4cpp/Manipulator.hh
%{_usr}/local/include/log4cpp/NDC.hh
%{_usr}/local/include/log4cpp/NTEventLogAppender.hh
%{_usr}/local/include/log4cpp/OstreamAppender.hh
%{_usr}/local/include/log4cpp/PassThroughLayout.hh
%{_usr}/local/include/log4cpp/PatternLayout.hh
%{_usr}/local/include/log4cpp/Portability.hh
%{_usr}/local/include/log4cpp/Priority.hh
%{_usr}/local/include/log4cpp/PropertyConfigurator.hh
%{_usr}/local/include/log4cpp/RemoteSyslogAppender.hh
%{_usr}/local/include/log4cpp/RollingFileAppender.hh
%{_usr}/local/include/log4cpp/SimpleConfigurator.hh
%{_usr}/local/include/log4cpp/SimpleLayout.hh
%{_usr}/local/include/log4cpp/StringQueueAppender.hh
%{_usr}/local/include/log4cpp/SyslogAppender.hh
%{_usr}/local/include/log4cpp/TimeStamp.hh
%{_usr}/local/include/log4cpp/TriggeringEventEvaluatorFactory.hh
%{_usr}/local/include/log4cpp/TriggeringEventEvaluator.hh
%{_usr}/local/include/log4cpp/Win32DebugAppender.hh

#%attr(644,root,root) %prefix/lib/pkgconfig/log4cpp.pc
#%attr(644,root,root) %prefix/share/aclocal/*.m4

%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 1.0-1
Initial Packaging
