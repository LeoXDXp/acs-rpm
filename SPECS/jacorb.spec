%define ALTVER 2016.10

Name:             jacorb
Version:          3.6.1.%{ALTVER}
Release:          1%{?dist}
Summary:          The Java implementation of the OMG's CORBA standard
Group:            Development/Libraries
License:          LGPLv2
URL:              http://www.jacorb.org/index.html

Source0:          http://www.jacorb.org/releases/%{version}/jacorb-%{version}-src.zip
Source1:          http://central.maven.org/maven2/org/jacorb/jacorb-parent/%{version}/jacorb-parent-%{version}.pom
Source2:          http://central.maven.org/maven2/org/jacorb/jacorb/%{version}/jacorb-%{version}.pom
Source3:          http://central.maven.org/maven2/org/jacorb/jacorb-idl-compiler/%{version}/jacorb-idl-compiler-%{version}.pom

# ACS Patch
Patch0:           JacORB-all-2015-02-26.patch

BuildArch:        noarch

BuildRequires:    javapackages-local
BuildRequires:    java-devel
BuildRequires:    ant
BuildRequires:    antlr-tool
BuildRequires:    avalon-logkit
BuildRequires:    bsh
BuildRequires:    slf4j

%description
This package contains the Java implementation of the OMG's CORBA standard, and

%package javadoc
Summary:          Javadocs for %{name}
Group:            Documentation
Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jacorb-%{version}

cp %{SOURCE1} jacorb-parent.pom
cp %{SOURCE2} jacorb.pom
cp %{SOURCE3} jacorb-idl-compiler.pom

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
find -name '*.zip' -exec rm -f '{}' \;

%patch0 -p1

# No xdoclet available
sed -i 's|,notification||' src/org/jacorb/build.xml

ln -s $(build-classpath antlr) lib/antlr-2.7.2.jar
ln -s $(build-classpath slf4j/api) lib/slf4j-api-1.5.6.jar

%mvn_alias "org.jacorb:" "jacorb:"

%build
export CLASSPATH=$(build-classpath avalon-logkit slf4j/api)

sed -i "s|>avalon<|>avalon-logkit<|g" jacorb-idl-compiler.pom

%pom_remove_dep "tanukisoft:wrapper" jacorb.pom
%pom_remove_dep "picocontainer:picocontainer" jacorb.pom
%pom_remove_dep "nanocontainer:nanocontainer" jacorb.pom
%pom_remove_dep "nanocontainer:nanocontainer-remoting" jacorb.pom

ant all doc

%install
%mvn_artifact jacorb-parent.pom
%mvn_artifact jacorb.pom lib/jacorb.jar
%mvn_artifact jacorb-idl-compiler.pom lib/idl.jar

%mvn_install -J doc/api

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc doc/LICENSE

%files javadoc -f .mfiles-javadoc
%doc doc/LICENSE

%changelog
* Tue Nov 22 2016 Leonardo Pizarro <lepizarr@inf.utfsm.cl>-3.6.1-1
Initial packaging based on 2.3.1 srpm
