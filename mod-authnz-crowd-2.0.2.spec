%define name mod_crowd 
%define version 2.0.2 
%define release skybet.0.1

Summary: mod_crowd
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: Apache 2.0 
Group: System Environment/Libraries
Obsoletes: mod_crowd 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64
Vendor: Atlassian
Url: https://confluence.atlassian.com/display/CROWD021/
Requires(pre): httpd libxml2 curl

%description
Crowd is designed to help you manage users and groups across multiple applications. 

%clean

%prep
%setup -q -n %{name}-%{version}
rm -Rf %{buildroot}

%pre

%build
autoreconf --install
./configure --exec-prefix=%{buildroot}/usr
make
%__mkdir %{buildroot}
%__mkdir %{buildroot}/etc
%__mkdir %{buildroot}/etc/httpd
%__mkdir %{buildroot}/etc/httpd/conf.d
%__mkdir %{buildroot}/usr
%__mkdir %{buildroot}/usr/lib64
%__mkdir %{buildroot}/usr/lib64/httpd
%__mkdir %{buildroot}/usr/lib64/httpd/modules

%install
%__make install
cp /usr/lib64/httpd/modules/mod_authnz_crowd.so.0.0.0 %{buildroot}/usr/lib64/httpd/modules/
cp etc/mod_crowd.conf %{buildroot}/etc/httpd/conf.d/

%post
rm /usr/lib64/httpd/modules/mod_authnz_crowd.so
ln -s /usr/lib64/httpd/modules/mod_authnz_crowd.so.0.0.0 /usr/lib64/httpd/modules/mod_authnz_crowd.so

%files
%defattr(-,root,root)
/usr/lib64/httpd/modules/mod_authnz_crowd.so.0.0.0
/etc/httpd/conf.d/mod_crowd.conf

