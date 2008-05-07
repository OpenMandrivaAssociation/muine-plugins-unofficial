%define name muine-plugins-unofficial
%define version 1.0.0
%define release %mkrel 1

Summary: Collection of plugins for the Muine player
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
Patch: muine-plugins-unofficial-0.0.1-dllmap.patch
Patch1: muine-plugins-unofficial-1.0.0-gtk-sharp.patch
License: GPL
Group: Sound
Url: http://www.public.asu.edu/~bnickel/MuinePluginsUnofficial/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel muine
BuildRequires: libalsa-devel
BuildRequires: libGConf2-devel
BuildArch: noarch
Requires: libalsa
%define _requires_exceptions lib.*alsa2

%description
This is a collection of plugins for the Muine audio player. It contains an
Alarm Clock and a Tray Icon plugin.

%prep
%setup -q
%patch -p1
%patch1 -p1
autoconf

%build
./configure --prefix=%_prefix --libdir=%_prefix/lib
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std pkgconfigdir=%_datadir/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING AUTHORS ChangeLog NEWS
%_prefix/lib/muine/plugins/Muine.Plugins.Base.dll
%_prefix/lib/muine/plugins/Muine.Plugins.AlarmClock.dll*
%_prefix/lib/muine/plugins/Muine.Plugins.PluginManager.dll
%_prefix/lib/muine/plugins/Muine.Plugins.TrayIcon.dll
%_prefix/lib/muine/plugins/Muine.Plugins.Widgets.dll
%_datadir/pkgconfig/muine-plugins-unofficial.pc


