#
%define		module	cfgparse
%define		_ver	v01_02
%define		ver	%(echo %{_ver} | sed -e 's@^v0@@' -e 's@_@.@g')
#
Summary:	Python configuration file parser module
Summary(pl.UTF-8):	Moduł Pythona do parsowania plików konfiguracyjnych
Name:		python-cfgparse
Version:	%{ver}
Release:	4
License:	distrubutable	
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/cfgparse/%{module}-%{_ver}.tar.gz
# Source0-md5:	9add1b0bbf828f7c7383407cdeefea94
URL:		http://cfgparse.sourceforge.net/
BuildRequires:	python >= 2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python configuration file parser module.

%description -l pl.UTF-8
Moduł Pythona do parsowania plików konfiguracyjnych.

%prep
%setup -q -n %{module}-%{_ver}

%install
rm -rf $RPM_BUILD_ROOT

%py_install

# make python *.pyo files
%{py_ocomp} $RPM_BUILD_ROOT%{py_sitescriptdir}

# remove .py files, leave just compiled ones.
%{py_postclean}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt docs/cfgparse.pdf docs/cfgparse/* 
%{py_sitescriptdir}/*.py[co]
