Summary:	X based flight combat
Summary(de.UTF-8):	Flugkampfspiel unter X
Summary(fr.UTF-8):	Combat aérien sous X
Summary(pl.UTF-8):	Symulator lotu dla systemu X Window
Summary(tr.UTF-8):	X tabanlı uçuş ve savaş
Name:		acm
Version:	5.0
Release:	0.3
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://www.websimulations.com/download/%{name}-%{version}.tar.gz
# Source0-md5:	8d27051a3aa0d85b90f66a86f746e827
Patch0:		%{name}-ac_fix.patch
Patch1:		%{name}-sparc.patch
Patch2:		%{name}-general.patch
Patch3:		%{name}-DESTDIR.patch
Patch4:		%{name}-nolibs.patch
Patch5:		%{name}-malloc.patch
URL:		http://home.netcom.com/~rrainey/acm.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdbm-devel
BuildRequires:	nas-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ACM is an X based flight simulator. It also have network cabailities
for multiplayer games.

%description -l de.UTF-8
ACM ist ein Flugsimulator auf X-Basis, der netzwerkfähig ist und die
Teilnahme mehrerer Spieler gestattet.

%description -l fr.UTF-8
ACM est un simulateur de vol sous X. Il permet de jouer en réseau à
plusieurs joueurs.

%description -l pl.UTF-8
ACM to symulator lotu dla systemu X Window. Ma możliwość gry przez
sieć dla wielu graczy.

%description -l tr.UTF-8
ACM, X tabanlı bir uçuş simulatörüdür. Çok oyunculu oynayabilmek için
gerekli ağ yeteneklerine sahiptir.

%prep
%setup -q
chmod -R +rwX *
%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build
%{__aclocal}
%{__autoconf}
for dir in dis dis/disgen gedit; do
	olddir=$(pwd)
	cd $dir
	%{__autoconf}
	cd $olddir
done
%configure

# -j1 because of no rules to make dis/disp.h early enough
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/acm
%{_prefix}/lib/games/acm
%{_mandir}/man1/acm.1*
