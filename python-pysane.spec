Summary:	Python SANE module
Summary(pl.UTF-8):	Moduł SANE dla Pythona
Name:		python-pysane
Version:	2.0.1
Release:	2
License:	MIT-like
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pysane/
Source0:	https://files.pythonhosted.org/packages/source/p/pysane/pysane-%{version}.tar.gz
# Source0-md5:	8964574c06ab6ee7b782429386e887ac
URL:		https://pypi.org/project/pysane/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-numpy-numarray-devel
BuildRequires:	python-pillow-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
BuildRequires:	sane-backends-devel
Requires:	python-numpy-numarray
Requires:	python-pillow
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SANE module provides an interface to the SANE scanner and frame
grabber interface for Linux.

%description -l pl.UTF-8
Moduł SANE udostępnia interfejs do biblioteki SANE będącej interfejsem
do skanerów i urządzeń przechwytujących ramki obrazu dla Linuksa.

%prep
%setup -q -n pysane-%{version}

%{__sed} -i -e "s,^PIL_IMAGING_DIR.*,import sysconfig\nPIL_IMAGING_DIR = sysconfig.get_path('include') + '/Imaging'," setup.py

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
%{py_sitedir}/pysane-%{version}-py*.egg-info
