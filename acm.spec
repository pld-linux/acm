# ToDo:
# - make it install in a correct directory....
#
Summary:	X based flight combat
Summary(de):	Flugkampfspiel unter X
Summary(fr):	Combat aérien sous X
Summary(pl):	Symulator lotu dla systemu X Window
Summary(tr):	X tabanlý uçuþ ve savaþ
Name:		acm
Version:	5.0
Release:	0.2
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://www.websimulations.com/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_fix.patch
Patch1:		%{name}-sparc.patch
Patch2:		%{name}-general.patch
URL:		http://home.netcom.com/~rrainey/acm.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ACM is an X based flight simulator. It also have network cabailities
for multiplayer games.

%description -l de
ACM ist ein Flugsimulator auf X-Basis, der netzwerkfähig ist und die
Teilnahme mehrerer Spieler gestattet.

%description -l fr
ACM est un simulateur de vol sous X. Il permet de jouer en réseau à
plusieurs joueurs.

%description -l pl
ACM to symulator lotu dla systemu X Window. Ma mo¿liwo¶æ gry przez
sieæ dla wielu graczy.

%description -l tr
ACM, X tabanlý bir uçuþ simulatörüdür. Çok oyunculu oynayabilmek için
gerekli að yeteneklerine sahiptir.

%prep
%setup -q
chmod -R +rwX *
%patch0
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
#%{__autoheader}
for dir in dis dis/disgen gedit; do
	olddir=$(pwd)
	cd $dir
	%{__autoconf}
	cd $olddir
done
%configure --prefix=$RPM_BUILD_ROOT%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/games,%{_mandir}/man1}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/acm
%attr(755,root,root) %{_bindir}/acms
%attr(755,root,root) %{_bindir}/kill-acms
%{_libdir}/games/acm
%{_mandir}/man1/acm.1*
