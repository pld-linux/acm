Summary: X based flight combat
Name: acm
Version: 4.7
Release: 8TL
Copyright: MIT
Group: X11/Games
Source: ftp://ftp.x.org/contrib/games/multiplayer/acm-4.7.tar.gz
Patch: acm-4.7-linux.patch
Patch1: acm-4.7-glibc.patch
BuildRoot: /var/tmp/acm-root
Summary(de): Flugkampfspiel unter X
Summary(fr): Combat aérien sous X.
Summary(tr): X tabanlý uçuþ ve savaþ

%description
ACM is an X based flight simulator.  It also have network cabailities
for multiple player games.

%description -l de
ACM ist ein Flugsimulator auf X-Basis, der netzwerkfähig ist 
und die Teilnahme mehrerer Spieler gestattet. 

%description -l fr
ACM est un simulateur de vol sous X. Il permet de jouer en réseau à plusieurs
joueurs.

%description -l tr
ACM, X tabanlý bir uçuþ simulatörüdür. Çok oyunculu oynayabilmek için
gerekli að yeteneklerine sahiptir.

%prep
%setup -q
%patch -p1 -b .linux
%patch1 -p1 -b .noglibc

%build
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib/games,man/man1}

make prefix=$RPM_BUILD_ROOT/usr install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/acm
/usr/bin/acms
/usr/bin/kill-acms
/usr/man/man1/acm.1
/usr/lib/games/acm

%changelog
* Tue Oct 27 1998 Scott Stone <sstone@turbolinux.com>
- Built for TL 3.0

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
