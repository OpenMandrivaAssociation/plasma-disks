%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Hard disk health monitoring for KDE Plasma
Name:		plasma-disks
Version:	5.21.1
Release:	1
License:	GPL
Group:		Graphical desktop/KDE
URL:		https://kde.org
Source0:	http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	smartmontools
Requires:	smartmontools

%description
Plasma Disks monitors S.M.A.R.T. data of disks and alerts the user when
signs of imminent failure appear.

%prep
%autosetup -n %{name}-%{version} -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name

%files -f %{name}.lang
%license LICENSES/*.txt
%{_libexecdir}/kf5/kauth/kded-smart-helper
%{_libdir}/qt5/plugins/plasma/kcms/smart.so
%{_libdir}/qt5/plugins/kf5/kded/smart.so
%{_datadir}/dbus-1/system-services/org.kde.kded.smart.service
%{_datadir}/dbus-1/system.d/org.kde.kded.smart.conf
%{_datadir}/knotifications5/org.kde.kded.smart.notifyrc
%{_datadir}/kpackage/kcms/plasma_disks/*
%{_datadir}/kservices5/smart.desktop
%{_datadir}/metainfo/org.kde.plasma.disks.metainfo.xml
%{_datadir}/polkit-1/actions/org.kde.kded.smart.policy
