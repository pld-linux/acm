# ToDo:
# - make it build,
# - make it work :>
#
Summary:	X based flight combat.
Summary(de):	Flugkampfspiel unter X.
Summary(fr):	Combat aérien sous X.
Summary(tr):	X tabanlý uçuþ ve savaþ.
Summary(pl):	Symulator lotu dla X Windows.
Name:		acm
Version:	5.0
Release:	0.1
Copyright:	MIT
Group:		X11/Applications/Games
Source0:	http://www.websimulations.com/download/%{name}-%{version}.tar.gz
#Patch0:		%{name}-4.7-linux.patch
#Patch1:		%{name}-4.7-glibc.patch
URL:		http://home.netcom.com/~rrainey/acm.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ACM is an X based flight simulator. It also have network cabailities
for multiple player games.

%description -l de
ACM ist ein Flugsimulator auf X-Basis, der netzwerkfähig ist und die
Teilnahme mehrerer Spieler gestattet.

%description -l fr
ACM est un simulateur de vol sous X. Il permet de jouer en réseau à
plusieurs joueurs.

%description -l tr
ACM, X tabanlý bir uçuþ simulatörüdür. Çok oyunculu oynayabilmek için
gerekli að yeteneklerine sahiptir.

%prep
%setup -q
chmod -R +rwX *
#%patch -p1 -b .linux
#%patch1 -p1 -b .noglibc

%build
rm -f missing
%{__aclocal}
%{__autoconf}
#%{__autoheader}
#%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{bin,lib/games,man/man1}

%{__make} prefix=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/acm
%attr(755,root,root) %{_bindir}/acms
%attr(755,root,root) %{_bindir}/kill-acms
%{_prefix}/man/man1/acm.1
%{_libdir}/games/acm
