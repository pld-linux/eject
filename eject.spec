Summary:	ejects ejectable media and controls auto ejection
Summary(de.UTF-8):	wirft austauschbare Datenträger aus und steuert Auswurf
Summary(es.UTF-8):	Expulsa medias expulsables y controla autoexpulsión
Summary(fr.UTF-8):	éjecte un support éjectable et commande l'éjection automatique
Summary(pl.UTF-8):	Eject otwieranie szuflad CDROM, Jaz, ZIP i innych
Summary(pt_BR.UTF-8):	Ejeta mídias ejetáveis e controla auto-ejeção
Summary(ru.UTF-8):	Программа, выталкивающая сменные носители из накопителей
Summary(tr.UTF-8):	Eject yeteneği olan aygıtları kontrol eder
Summary(uk.UTF-8):	Програма, що виштовхує змінні носії з накопичувачів
Name:		eject
Version:	2.1.5
Release:	4
License:	GPL
Group:		Applications/System
Source0:	http://ca.geocities.com/jefftranter@rogers.com/%{name}-%{version}.tar.gz
# Source0-md5:	b96a6d4263122f1711db12701d79f738
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	dd66d948c94fe0f0b4483c51873e6e20
Source2:	%{name}-pl.po
Patch0:		%{name}-gettext.patch
Patch1:		%{name}-po.patch
Patch2:		%{name}-symlink.patch
Patch3:		verbose.patch
Patch4:		lock.patch
Patch5:		opendevice.patch
Patch6:		spaces.patch
Patch7:		timeout.patch
Patch8:		umount.patch
URL:		http://sites.google.com/site/tranter/software
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.15
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program allows the user to eject media that is autoejecting like
CD-ROMs, Jaz and Zip drives, and floppy drives on SPARC machines.

%description -l de.UTF-8
Dieses Programm ermöglicht auf SPARC-Rechnern das Auswerfen von
Datenträgern wie CD-ROMs, Jaz-, Zip- und Floppy-Disketten, die
normalerweise automatisch ausgeworfen werden.

%description -l es.UTF-8
Este programa permite al usuario expulsar media que es autoexpulsable
como CD-ROMs, drives Jaz y Zip y floppy drives en máquinas SPARC.

%description -l fr.UTF-8
Ce programme permet à l'utilisateur d'éjecter un support autoéjectable
comme les CD-ROM, les lecteurs Zip et Jaz, et les disquettes sur les
SPARC.

%description -l pl.UTF-8
Program do automatycznego otwierania szuflad w urządzeniach CDROM,
Jaz, ZIP floppy (na maszynach SPARC) oraz innych.

%description -l pt_BR.UTF-8
Este programa permite ao usuário ejetar mídia que é auto-ejetável como
CD-ROMs, drives Jaz e Zip e floppy drives em máquinas SPARC.

%description -l ru.UTF-8
Эта программа позволяет пользователю выталкивать сменные носители из
накопителей, поддерживающих программный eject (такие как CD-ROMы,
Iomega Jaz или Zip диски, флоппи-диски на SPARC-машинах). Eject может
также управлять некоторыми CD ченджерами.

%description -l tr.UTF-8
Bu yazılım paketi ile kullanıcıya 'eject' yeteneği olan aygıtları
kontrol olanağı verilmektedir. Bu yeteneği olan aygıtlar arasında
CD-ROM'lar, Zip sürücüleri ve bazı disket sürücüleri yer alır.

%description -l uk.UTF-8
Ця програма дозволяє користувачеві виштовхувати змінні носії з
накопичувачів, що підтримують програмний eject (такі як CD-ROMи,
Iomega Jaz чи Zip диски, флопі-диски на SPARC-машинах). Eject може
також управляти деякими CD ченджерами

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

# standardize locale names
mv -f po/{cs_CZ,cs}.po
mv -f po/{de_DE,de}.po
mv -f po/{es_ES,es}.po
mv -f po/{fr_FR,fr}.po
mv -f po/{ja_JP.eucJP,ja}.po
mv -f po/{tr_TR,tr}.po
mv -f po/{zh_TW.UTF-8,zh_TW}.po

cp %{SOURCE2} po/pl.po

echo "cs de es fr ja pl pt_BR tr zh_TW" >> po/LINGUAS
printf "eject.c\ni18n.h\nvolname.c\n" >> po/POTFILES.in

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/README.eject-non-english-man-pages

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS PORTING PROBLEMS README TODO
%attr(755,root,root) %{_bindir}/eject
%attr(755,root,root) %{_bindir}/volname
%{_mandir}/man1/eject.1*
%{_mandir}/man1/volname.1*
%lang(fi) %{_mandir}/fi/man1/eject.1*
%lang(hu) %{_mandir}/hu/man1/eject.1*
%lang(ja) %{_mandir}/ja/man1/eject.1*
%lang(ja) %{_mandir}/ja/man1/volname.1*
%lang(pl) %{_mandir}/pl/man1/eject.1*
