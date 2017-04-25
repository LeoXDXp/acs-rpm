Name:	ACS-ExtJars
Version:	2017.02
Release:	2%{?dist}
Summary:	External Jar files for ACS CB

#Group:		
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz

#BuildRequires:	
Requires: ant devtoolset-4-eclipse-emf-core devtoolset-4-eclipse-emf-runtime

%description
The following Jar files for ACS: activation.jar, (apache-)common-math.jar, (apache-)common-xml-resolver, ehcache-core, jackarta-regexp (deprecated by apache), jchart2d, junit-dep, prevayler, sqltool.
They can be found at https://github.com/ACS-Community/ACS/tree/master/LGPL/Tools/extjars in the lib folder.
As a dependency needed by ACS-ToolsKit, org.eclipse.uml2.uml.ecore.importer_3.1.0.v20170227-0935.jar is added.

%prep
%setup -q

%install
#%make_install
mkdir -p %{buildroot}%{_prefix}/local/share/java/ 
mv %{_builddir}/%{name}-%{version}/* %{buildroot}%{_prefix}/local/share/java/

%files
%attr(645,-,-) %{_prefix}/local/share/java/


%changelog
* Tue Apr 25 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-2
Adding http://ftp.gnome.org/mirror/eclipse.org/modeling/mdt/uml2/updates/5.2/R201702270935/plugins/org.eclipse.uml2.uml.ecore.importer_3.1.0.v20170227-0935.jar
* Fri Mar 03 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
