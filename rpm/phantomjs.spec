%define    prefix  /usr/local
%define    debug_package %{nil}

Name:      phantomjs
Version:   %{version}
Release:   %{release}
Group:     Utilities/Misc
License:   BSD
URL:       https://github.com/ariya/phantomjs
Summary:   a headless WebKit with JavaScript API
BuildArch: x86_64
Source0:   phantomjs
# (only create temporary directory name, for RHEL5 compat environment)
# see : http://fedoraproject.org/wiki/Packaging:Guidelines#BuildRoot_tag
Prefix:    %{prefix}
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
PhantomJS is a headless WebKit with JavaScript API. It has fast and native
support for various web standards: DOM handling, CSS selector, JSON,
Canvas, and SVG. PhantomJS is created by Ariya Hidayat.

%prep

%build

%install

mkdir -p %{buildroot}/usr/share/phantomjs
mkdir -p %{buildroot}/usr/share/phantomjs/examples

#%{__install} -p -D -m 0644 phantomjs/CONTRIBUTING.md %{buildroot}/usr/share/phantomjs/CONTRIBUTING.md
%{__install} -p -D -m 0644 phantomjs/ChangeLog       %{buildroot}/usr/share/phantomjs/ChangeLog
%{__install} -p -D -m 0644 phantomjs/LICENSE.BSD     %{buildroot}/usr/share/phantomjs/LICENSE.BSD
%{__install} -p -D -m 0644 phantomjs/README.md       %{buildroot}/usr/share/phantomjs/README.md

%{__install} -Dp -m0755 phantomjs/bin/phantomjs %{buildroot}/%{prefix}/bin/%{name}

%{__install} -Dp -m0755 phantomjs/examples/*.js %{buildroot}/usr/share/phantomjs/examples/

# /usr/share/phantomjs
# /usr/share/phantomjs/CONTRIBUTING.md
# /usr/share/phantomjs/ChangeLog
# /usr/share/phantomjs/LICENSE.BSD
# /usr/share/phantomjs/README.md
# /usr/share/phantomjs/examples


%clean

%files
%defattr(0755,root,root)
%{prefix}/bin/phantomjs

%defattr(0644,root,root)
#/usr/share/phantomjs/CONTRIBUTING.md
/usr/share/phantomjs/ChangeLog
/usr/share/phantomjs/LICENSE.BSD
/usr/share/phantomjs/README.md
/usr/share/phantomjs/examples/*.js

%pre

%post

%changelog
* Sat Apr 08 2017 yuokada
- initial release
