Name:		ACS-otherjars
Version:	2017.02
Release:	1%{?dist}
Summary:	External Jar files for ACS CB

#Group:		
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz

#BuildRequires:	
#Requires:

%description
Handles requirements of ACS-Tools-Kit of java dependencies such as osgi(org.eclipse.uml2.uml.ecore.importer)

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
