Summary:	A GNOME hardware monitoring applet
Summary(pl):	Aplet GNOME monitoruj±cy sprzêt
Name:		glms
Version:	1.03
Release:	11
License:	GPL
Group:		X11/Applications
#Source0:	http://users.kiss.si/~k4fe0277/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	ec5c664b5fdc6cbbc2bd04414d85c82e
Source1:	%{name}_applet.desktop
Patch1:		%{name}-redhat.patch
Patch2:		%{name}-lm_sensors-2.5.5-patch
Patch3:		%{name}-configure.patch.gz
Patch4:		%{name}-ja.patch
#URL:		http://users.kiss.si/~k4fe0277/glms.html
ExclusiveArch:	%{ix86}
Requires:	lm_sensors
BuildRequires:	lm_sensors-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

%description
The glms package contains a hardware monitoring applet for GNOME. The
applet displays the temperature of processors, the speed of cooling
fans, and power supply performance. You'll also need to have the
lm_sensors package installed.

%description -l pl
Pakiet glms zawiera aplet monitoruj±cy sprzêt przeznaczony dla GNOME.
Aplet pokazuje temperaturê procesorów, obroty wiatraczków ch³odz±cych
i osi±gi ¼ród³a zasilania. Musisz mieæ zainstalowany pakiet
lm_sensors.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

chmod u+x mkinstalldirs

cp -f %{SOURCE1} .

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I /usr/share/aclocal/gnome
%{__automake}
%{__autoconf}
CFLAGS="%{rpmcflags} -I/usr/X11R6/include/gnome-1.0" ; export CFLAGS
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -fr $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/applets/Utility/*
%{_datadir}/gnome/help/*
%{_sysconfdir}/CORBA/servers/*
