Name:     patchage

Version:  1.0.0
Release:  1%{?dist}
Summary:  Patchage is a modular patch bay for Jack and ALSA based audio/MIDI systems.
License:  GPLv3+
URL:      http://drobilla.net/software/patchage
Source0:  http://download.drobilla.net/patchage-%{version}.tar.bz2

BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: jack-audio-connection-kit-dbus
BuildRequires: gtkmm24-devel
BuildRequires: dbus-glib-devel
BuildRequires: ganv-devel

%description
Patchage is a modular patch bay for Jack and ALSA based audio/MIDI systems.

%prep
%setup -q

%build
./waf --destdir=%{buildroot} --prefix=%{_prefix} configure
./waf

%install
./waf --destdir=%{buildroot} --prefix=%{_prefix} install

%files
%doc AUTHORS COPYING INSTALL NEWS README
%doc %{_exec_prefix}/share/man
%{_bindir}/patchage
%{_exec_prefix}/share/patchage/patchage.ui
%{_exec_prefix}/share/applications/patchage.desktop
%{_exec_prefix}/share/icons/hicolor
