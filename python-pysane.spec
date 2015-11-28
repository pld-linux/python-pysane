Summary:	Python SANE module
Summary(pl.UTF-8):	Moduł SANE dla Pythona
Name:		python-pysane
Version:	2.0.1
Release:	2
License:	MIT-like
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/p/pysane/pysane-%{version}.tar.gz
# Source0-md5:	8964574c06ab6ee7b782429386e887ac
URL:		https://pypi.python.org/pypi/pysane/
BuildRequires:	python-PIL-devel
BuildRequires:	python-devel >= 2
BuildRequires:	python-numpy-numarray-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sane-backends-devel
Requires:	python-PIL
Requires:	python-numpy-numarray
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SANE module provides an interface to the SANE scanner and frame
grabber interface for Linux.

%description -l pl.UTF-8
Moduł SANE udostępnia interfejs do biblioteki SANE będącej interfejsem
do skanerów i urządzeń przechwytujących ramki obrazu dla Linuksa.

%prep
%setup -q -n pysane-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{py_sitedir}/_sane.so
%{py_sitedir}/sane.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/pysane-%{version}-py*.egg-info
%endif
