Name:		ACS-uml2-emf
Version:	2017.02
Release:	1%{?dist}
Summary:	Eclipse's MDT-UML2 and EMF Jar files for ACS-Tools-Kit Package

#Group:		
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz

#BuildRequires:	
Requires: ant-antunit

%description
Packaging runtime (jars) of eclipse mdt-uml2, emf and emf-validation. Also ant-core jar is provided.

%prep
%setup -q

%install
#%make_install
mkdir -p %{buildroot}%{_prefix}/local/share/eclipse/
mv %{_builddir}/%{name}-%{version}/eclipse/* %{buildroot}%{_prefix}/local/share/eclipse/

mkdir -p %{buildroot}%{_prefix}/local/share/java
mv %{_builddir}/%{name}-%{version}/ant-*.jar %{buildroot}%{_prefix}/local/share/java/

%files
%attr(645,-,-) %{_prefix}/local/share/eclipse
%{_prefix}/local/share/java


%changelog
* Fri Mar 03 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
