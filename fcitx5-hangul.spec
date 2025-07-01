Summary:	Hangul (Korean IM) plugin for fcitx5
Name:		fcitx5-hangul
Version:	5.1.6
Release:	1
Source0:    https://github.com/fcitx/fcitx5-hangul/archive/refs/tags/%{version}.tar.gz
URL:		https://github.com/fcitx/fcitx5-hangul
License:	LGPLv2
Group:		System/Internationalization
BuildRequires:	cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  lib64hangul-devel

%description
Hangul (Korean IM) plugin for fcitx5.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %name

%files -f %name.lang
%{_libdir}/fcitx5/libhangul.so
%{_datadir}/fcitx5/addon/hangul.conf
%{_datadir}/fcitx5/hangul/*
%{_datadir}/fcitx5/inputmethod/hangul.conf
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Hangul.metainfo.xml
