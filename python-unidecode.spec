%global debug_package %{nil}

Name: python-unidecode
Epoch: 100
Version: 1.3.3
Release: 1%{?dist}
BuildArch: noarch
Summary: US-ASCII transliterations of Unicode text
License: GPL-2.0-only
URL: https://github.com/avian2/unidecode/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This is a python port of Text::Unidecode Perl module. It provides a
function, 'unidecode(...)' that takes Unicode data and tries to
represent it in ASCII characters.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-unidecode
Summary: US-ASCII transliterations of Unicode text
Requires: python3
Provides: python3-unidecode = %{epoch}:%{version}-%{release}
Provides: python3dist(unidecode) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-unidecode = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(unidecode) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-unidecode = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(unidecode) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-unidecode
This is a python port of Text::Unidecode Perl module. It provides a
function, 'unidecode(...)' that takes Unicode data and tries to
represent it in ASCII characters.

%files -n python%{python3_version_nodots}-unidecode
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-unidecode
Summary: US-ASCII transliterations of Unicode text
Requires: python3
Provides: python3-unidecode = %{epoch}:%{version}-%{release}
Provides: python3dist(unidecode) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-unidecode = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(unidecode) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-unidecode = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(unidecode) = %{epoch}:%{version}-%{release}

%description -n python3-unidecode
This is a python port of Text::Unidecode Perl module. It provides a
function, 'unidecode(...)' that takes Unicode data and tries to
represent it in ASCII characters.

%files -n python3-unidecode
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
