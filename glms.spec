Summary:	A GNOME hardware monitoring applet
Summary(pl.UTF-8):   Aplet GNOME monitorujący sprzęt
Name:		glms
Version:	1.03
Release:	11
License:	GPL
Group:		X11/Applications
#Source0:	http://users.kiss.si/~k4fe0277/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	ec5c664b5fdc6cbbc2bd04414d85c82e
Source1:	%{name}_applet.desktop
Patch0:		%{name}-redhat.patch
Patch1:		%{name}-lm_sensors-2.5.5-patch
Patch2:		%{name}-configure.patch.gz
Patch3:		%{name}-ja.patch
Patch4:		%{name}-amfix.patch
#URL:		http://users.kiss.si/~k4fe0277/glms.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel
BuildRequires:	libtool
BuildRequires:	lm_sensors-devel
Requires:	lm_sensors
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

%description
The glms package contains a hardware monitoring applet for GNOME. The
applet displays the temperature of processors, the speed of cooling
fans, and power supply performance. You'll also need to have the
lm_sensors package installed.

%description -l pl.UTF-8
Pakiet glms zawiera aplet monitorujący sprzęt przeznaczony dla GNOME.
Aplet pokazuje temperaturę procesorów, obroty wiatraczków chłodzących
i osiągi źródła zasilania. Musisz mieć zainstalowany pakiet
lm_sensors.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

chmod u+x mkinstalldirs

cp -f %{SOURCE1} .

# "non-ascii character" - avoid rebuilding
touch po/glms.pot

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I /usr/share/aclocal/gnome
%{__automake}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# glms.mo but gnome/help/glms_applet
%find_lang %{name} --with-gnome --all-name

%clean
rm -fr $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/applets/Utility/*
%{_sysconfdir}/CORBA/servers/*
