#
# spec file for package obs-service-container_checks
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           obs-service-container_checks
Version:        0
Release:        0
Summary:        Various checks for the services container
License:        GPL-3.0
Group:          Development/Tools/Building
Url:            http://github.com/openSUSE/obs-service-container_checks.git
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This service does various checks for the container (e.g. docker) it is running in. This service
is not for productive use.

%prep
%setup -q

%build

%install
%make_install

%post
%postun

%files
%defattr(-,root,root)
%doc README.md LICENSE
/usr/lib/obs/service/container_checks
/usr/lib/obs/service/container_checks.service

%changelog

