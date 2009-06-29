%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-daemon
Version:        1.4.6
Release:        1%{?dist}
Summary:        Library to implement a well-behaved Unix daemon process

Group:          Development/Languages
License:        Python
URL:            http://pypi.python.org/pypi/python-daemon/
Source0:        http://pypi.python.org/packages/source/p/python-daemon/%{name}-%{version}.tar.gz
Patch0:         version_info_fix.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel, python-setuptools

%description
This library implements the well-behaved daemon specification of PEP 3143,
"Standard daemon process library".

%prep
%setup -q

%patch0 -p1



%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc TODO LICENSE.PSF-2
%{python_sitelib}/*


%changelog
* Wed Jun 24 2009 Kushal Das <kushal@fedoraproject.org> 1.4.6-1
- Initial release

