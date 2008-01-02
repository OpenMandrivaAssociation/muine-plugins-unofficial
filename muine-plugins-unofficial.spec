%define name muine-plugins-unofficial
%define version 0.0.1
%define release %mkrel 2

Summary: Collection of plugins for the Muine player
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch: muine-plugins-unofficial-0.0.1-dllmap.patch
License: GPL
Group: Sound
Url: http://www.public.asu.edu/~bnickel/MuinePluginsUnofficial/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel muine
BuildRequires: libalsa-devel
BuildRequires: libGConf2-devel
BuildArch: noarch
Requires: libalsa
%define _requires_exceptions ^lib.*

%description
This is a collection of plugins for the Muine audio player. It contains an
Alarm Clock and a Tray Icon plugin.

%prep
%setup -q
%patch -p1

%build
./configure --prefix=%_prefix --libdir=%_prefix/lib
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
mv %buildroot%buildroot/* %buildroot
%if %_lib != lib
mv %buildroot%_libdir %buildroot%_prefix/lib
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING AUTHORS ChangeLog NEWS
%_prefix/lib/muine/plugins/Muine.Plugins.AlarmClock.dll*
%_prefix/lib/muine/plugins/Muine.Plugins.TrayIcon.dll


