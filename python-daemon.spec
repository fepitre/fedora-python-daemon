%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-daemon
Version:        1.5.2
Release:        1%{?dist}
Summary:        Library to implement a well-behaved Unix daemon process

Group:          Development/Languages
License:        Python
URL:            http://pypi.python.org/pypi/python-daemon/
Source0:        http://pypi.python.org/packages/source/p/python-daemon/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel, python-setuptools
BuildRequires:  python-nose python-lockfile python-minimock
Requires:       python-lockfile

%description
This library implements the well-behaved daemon specification of PEP 3143,
"Standard daemon process library".

%prep
%setup -q

sed -i -e '/^#!\//, 1d' daemon/version/version_info.py


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%check
PYTHONPATH=$(pwd) nosetests


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE.PSF-2
%{python_sitelib}/*


%changelog
* Wed Dec 23 2009 Thomas Spura <tomspur@fedoraproject.org> - 1.5.2-1
- add missing BR: python-nose, minimock and lockfile
- also add lockfile as R (bug #513546)
- update to 1.5.2

* Wed Jun 24 2009 Kushal Das <kushal@fedoraproject.org> 1.4.6-1
- Initial release

