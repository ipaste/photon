Summary:	Google Startup Scripts
Name:		google-startup-scripts
Version:	1.3.1
Release:	1%{?dist}
License:	Apache License
Group:		System Environment/Base
URL:		https://github.com/GoogleCloudPlatform/compute-image-packages/
Source0:	google-startup-scripts-%{version}.tar.gz
%define sha1 google-startup-scripts=e96f19d98fd43856e1a40622b32c61284c77b2b6
Vendor:		VMware, Inc.
Distribution:	Photon
Provides:	google-startup-scripts
BuildArch:	noarch
Requires:  	python2

%description
Google provides a set of startup scripts that interact with the virtual machine environment.
On boot, the startup script /usr/share/google/onboot queries the instance metadata
for a user-provided startup script to run. User-provided startup scripts can be specified
in the instance metadata under startup-script or, if the metadata is in a small script
or a downloadable file, it can be specified via startup-script-url.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
cp -rpf * $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mv $RPM_BUILD_ROOT/etc/init.d/* $RPM_BUILD_ROOT/etc/rc.d/init.d/
rm -rf $RPM_BUILD_ROOT/etc/init.d/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/*
/lib/*
/etc/*
%exclude /README.md
%exclude /LICENSE

%changelog
*   Thu Jan 28 2016 Anish Swaminathan <anishs@vmware.com> 1.3.1-1
-   Upgrade version
*   Mon Aug 10 2015 Anish Swaminathan <anishs@vmware.com> 1.2.7-1
-   Updated version.
