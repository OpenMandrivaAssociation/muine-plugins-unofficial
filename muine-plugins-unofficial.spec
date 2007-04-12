%define name muine-plugins-unofficial
%define version 0.0.1
%define release %mkrel 1

Summary: Collection of plugins for the Muine player
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Sound
Url: http://www.public.asu.edu/~bnickel/MuinePluginsUnofficial/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel muine
BuildRequires: libalsa-devel
BuildRequires: libGConf2-devel
BuildArch: noarch
Requires: libalsa

%description
This is a collection of plugins for the Muine audio player. It contains an
Alarm Clock and a Tray Icon plugin.

%prep
%setup -q

%build
./configure --prefix=%_prefix --libdir=%_prefix/lib
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
mv %buildroot%buildroot/* %buildroot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING AUTHORS ChangeLog NEWS
%_prefix/lib/muine/plugins/Muine.Plugins.AlarmClock.dll*
%_prefix/lib/muine/plugins/Muine.Plugins.TrayIcon.dll


