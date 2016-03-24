Name: scx-postinstall
Version: 1.0
Release: alt1
Summary: Script 'post' for install agent for SCOM
License:  Public Domain
Group: Monitoring
Packager: Korneechev Evgeniy <ek@myconnector.ru>
BuildArch: noarch

Source0: %name-%version.tar.gz

%description
%summary

%prep
%setup

%install
mkdir -p %buildroot%_sysconfdir/pam.d
install -p omi %buildroot%_sysconfdir/pam.d/

%files
%_sysconfdir/pam.d/omi

%changelog
* Wed Mar 23 2016 Evgeniy Korneechev <ek@myconnector.ru> 1.0-alt1
- Initial build

