Name:           doxygen
Version:        1.8.2
Release:        1
License:        GPL-2.0+
Summary:        Automated C, C++, and Java Documentation Generator
Url:            http://www.stack.nl/~dimitri/doxygen/
Group:          Development/Tools
Source:         http://ftp.stack.nl/pub/users/dimitri/doxygen-%{version}.src.tar.gz
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
%description
Doxygen is a documentation system for C, C++, Java, and IDL. It can
generate an online class browser (in HTML) and an offline reference
manual (in LaTeX) from a set of documented source files. The
documentation is extracted directly from the sources. Doxygen is
developed on a Linux platform, but it runs on most other UNIX flavors
as well. An executable for Windows 95/NT is also available.

%prep
%setup -q

%build
unset QTDIR
./configure \
   --prefix %{_prefix} \
   --shared \
   --release
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%attr(444,root,root) %doc %{_mandir}/man1/doxygen.1.*
%attr(444,root,root) %doc %{_mandir}/man1/doxytag.1.*
%attr(755,root,root) /usr/bin/*

