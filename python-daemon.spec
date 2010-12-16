%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}

Name:           python-daemon
Version:        1.5.2
Release:        4%{?dist}
Summary:        Library to implement a well-behaved Unix daemon process

Group:          Development/Languages
License:        Python
URL:            http://pypi.python.org/pypi/python-daemon/
Source0:        http://pypi.python.org/packages/source/p/python-daemon/%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}-import.patch
Patch1:         %{name}-%{version}-py24-exc.patch
Patch2:         %{name}-%{version}-lockfile.patch
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
%patch0 -p0 -b .import
%patch1 -p0 -b .py24-exc
%patch2 -b .lockfile

sed -i -e '/^#!\//, 1d' daemon/version/version_info.py


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm -fr %{buildroot}%{python_sitelib}/tests

%clean
rm -rf %{buildroot}

# Test suite requires minimock and lockfile
%check
PYTHONPATH=$(pwd) nosetests

%files
%defattr(-,root,root,-)
%doc LICENSE.PSF-2
%{python_sitelib}/daemon/
%{python_sitelib}/python_daemon-%{version}-py%{pyver}.egg-info/

%changelog
* Thu Dec 16 2010 Luke Macken <lmacken@redhat.com> - 1.5.2-4
- Remove the setuptools dependency on lockfile, since the EL5 package does not
  contain the proper egg-info metadata

* Fri Jan 08 2010 Luke Macken <lmacken@redhat.com> - 1.5.2-3
- Add python-daemon-1.5.2-py24-exc.patch to fix a few
  unit tests on python 2.4

* Fri Jan 08 2010 Luke Macken <lmacken@redhat.com> - 1.5.2-2
- Add python-daemon-1.5.2-import.patch, which fixes the use of
  __import__ to work on Python 2.4

* Wed Dec 23 2009 Thomas Spura <tomspur@fedoraproject.org> - 1.5.2-1
- add missing BR: python-nose
- also add lockfile as R (bug #513546)
- update to 1.5.2

* Wed Dec 23 2009 Thomas Spura <tomspur@fedoraproject.org> - 1.5.1-2
- add missing BR: minimock and lockfile -> testsuite works again
- remove patch, use sed instead

* Wed Oct 07 2009 Luke Macken <lmacken@redhat.com> - 1.5.1-1
- Update to 1.5.1
- Remove conflicting files (#512760)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 24 2009 Kushal Das <kushal@fedoraproject.org> 1.4.6-1
- Initial release

