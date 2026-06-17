Name:           phidget22networkserver
Version:        1.25.20260512
Release:        %autorelease
Summary:        Drivers and API for Phidget devices
License:        LGPL-3.0-or-later and BSD-2-Clause and BSD-3-Clause
URL:            https://www.phidgets.com
Source0:        https://www.phidgets.com/downloads/phidget22/servers/linux/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  libphidget22-devel
BuildRequires:  libphidget22extra-devel
BuildRequires:  autoconf
BuildRequires:  avahi-compat-libdns_sd-devel
BuildRequires:  avahi-devel
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libusb1-devel
BuildRequires:  make
BuildRequires:  udev

Requires:       libphidget22
Requires:       libphidget22extra
Requires:       avahi-compat-libdns_sd
Requires:       udev

%description
Phidgets are a set of "plug and play" building blocks for low cost USB
sensing and control from your PC.  All the USB complexity is taken care
of by the robust libphidget API.

%prep
%autosetup

%build
%configure --disable-silent-rules --disable-static --enable-zeroconf=avahi --disable-ldconfig --enable-jni
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
mkdir -p -m 0755 %{buildroot}%{_sysconfdir}/phidgets/
install -p -m 0644 files/etc/phidgets/* %{buildroot}%{_sysconfdir}/phidgets/

%ldconfig_scriptlets

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/%{name}
%{_sysconfdir}/phidgets/

%changelog
%autochangelog