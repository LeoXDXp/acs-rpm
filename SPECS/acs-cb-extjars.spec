Name:	ACS-ExtJars
Version:	2017.02
Release:	1%{?dist}
Summary:	External Jar files for ACS CB

#Group:		
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz

#BuildRequires:	
#Requires: ant devtoolset-4-eclipse-emf-core devtoolset-4-eclipse-emf-runtime

%description
The following Jar files for ACS: activation.jar, (apache-)common-math.jar, (apache-)common-xml-resolver, ehcache-core, jackarta-regexp (deprecated by apache), jchart2d, junit-dep, prevayler, sqltool.
They can be found at https://github.com/ACS-Community/ACS/tree/master/LGPL/Tools/extjars in the lib folder.

%prep
%setup -q

%install
#%make_install
mkdir -p %{buildroot}%{_prefix}/local/share/java/ 
mv %{_builddir}/%{name}-%{version}/* %{buildroot}%{_prefix}/local/share/java/

%files
%attr(645,-,-) %{_prefix}/local/share/java/


%changelog
* Fri Mar 03 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
