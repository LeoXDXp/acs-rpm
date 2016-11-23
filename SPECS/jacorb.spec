%define ALTVER 2016.10

Name:             jacorb-ACS-%{ALTVER}
Version:          3.6.1
Release:          1%{?dist}
Summary:          The Java implementation of the OMG's CORBA standard
Group:            Development/Libraries
License:          LGPLv2
URL:              http://www.jacorb.org/index.html

Source0:          http://www.jacorb.org/releases/%{version}/jacorb-%{version}-source.zip
Source1:          http://central.maven.org/maven2/org/jacorb/jacorb-parent/%{version}/jacorb-parent-%{version}.pom
Source2:          http://central.maven.org/maven2/org/jacorb/jacorb/%{version}/jacorb-%{version}.pom
Source3:          http://central.maven.org/maven2/org/jacorb/jacorb-idl-compiler/%{version}/jacorb-idl-compiler-%{version}.pom

# ACS Patch
Patch0:           JacORB-all-2015-02-26.patch

BuildArch:        noarch
# javapackages-local in Centos7 comes thru SCL repo as rh-java-common-javapackages-local
BuildRequires:    rh-java-common-javapackages-local java-devel ant antlr-tool avalon-logkit bsh slf4j

%description
This package contains the Java implementation of the OMG's CORBA standard, and

%package javadoc
Summary:          Javadocs for %{name}
Group:            Documentation
# jpackage-utils is provided by javapackages-tools
Requires:         rh-java-common-javapackages-local

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
# Version patching
cp %{buildroot}/core/src/main/java-templates/org/jacorb/util/Version.java %{buildroot}/core/src/main/java-templates/org/jacorb/util/Version.java.bak
BUILD_TS=$(date "+%d %B %Y %H:%M")
sed -e "s/@releaseYear@/2015/;s/@timestamp@/$BUILD_TS/;s/@buildNumber@/ACS build based on 150a4c9/;s/@project.version@/%{version}/" < %{buildroot}/core/src/main/java-templates/org/jacorb/util/Version.java.bak > %{buildroot}/core/src/main/java-templates/org/jacorb/util/Version.java


# Need Revision
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
Initial packaging based on 2.3.1 srpm. Building for CentOS 7 mainly
