Name:      weechat
Summary:   Portable, fast, light and extensible IRC client
Version:   0.2.6.3
Release:   1%{?dist}
Source:    http://weechat.flashtux.org/download/%{name}-%{version}.tar.bz2
Patch0:    %{name}-%{version}-pie-rollup.patch.bz2
URL:       http://weechat.flashtux.org
Group:     Applications/Communications
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
License:   GPLv3
BuildRequires: ncurses-devel python-devel perl ruby-devel 
BuildRequires: gnutls-devel lua-devel aspell-devel
BuildRequires: docbook-style-xsl gettext ruby

%description
WeeChat (Wee Enhanced Environment for Chat) is a portable, fast, light and
extensible IRC client. Everything can be done with a keyboard.
It is customizable and extensible with scripts.

%prep
%setup -q
%patch0 -p1

%build
%configure \
  --disable-rpath \
  --enable-static=no \
  --with-doc-xsl-prefix=/usr/share/sgml/docbook/xsl-stylesheets

make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR="$RPM_BUILD_ROOT"

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

# This hardcoded docdir=... in Makefile.am is crap

mv $RPM_BUILD_ROOT%{_docdir}/%{name}/html .
mv $RPM_BUILD_ROOT%{_docdir}/%{name}/weechat_quickstart* .

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT 

%files -f %{name}.lang
%defattr(-,root,root,0755) 
%doc AUTHORS BUGS ChangeLog COPYING FAQ FAQ.fr NEWS README TODO html weechat_quickstart*
%{_mandir}/man1/%{name}-curses.1*
%{_bindir}/%{name}-curses
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/*

%changelog
* Thu Jun 25 2009 Paul P. Komkoff Jr <i@stingr.net> - 0.2.6.3-1
- gnutls detection bugfix

* Fri May  1 2009 Paul P. Komkoff Jr <i@stingr.net> - 0.2.6.2-1
- fix some charset decoding problems.

* Thu Mar 19 2009 Paul P. Komkoff Jr <i@stingr.net> - 0.2.6.1-1
- fix bz#490709

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.2.6-6
- Rebuild for Python 2.6

* Sun Sep 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.2.6-5
- Fix Patch0:/%%patch mismatch.

* Fri Jun 27 2008 Paul P. Komkoff Jr <i@stingr.net> - 0.2.6-4
- rebuild because of ssl/tls deps

* Sun Feb 24 2008 Paul P. Komkoff Jr <i@stingr.net> - 0.2.6-3
- make weechat-curses a PIE
- remove irrelevant INSTALL from docs
- remove *.la from plugins

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.6-2
- Autorebuild for GCC 4.3

* Fri Oct 19 2007 Paul P. Komkoff Jr <i@stingr.net> - 0.2.6-1
- new upstream version, new license
* Fri Jun  8 2007 Paul P. Komkoff Jr <i@stingr.net> - 0.2.5-1
- new upstream version
* Mon Apr  9 2007 Paul P. Komkoff Jr <i@stingr.net> - 0.2.4-2
- preparing for Fedora

* Thu Mar 29 2007 FlashCode <flashcode@flashtux.org> 0.2.4-1
- Released version 0.2.4
* Wed Jan 10 2007 FlashCode <flashcode@flashtux.org> 0.2.3-1
- Released version 0.2.3
* Sat Jan 06 2007 FlashCode <flashcode@flashtux.org> 0.2.2-1
- Released version 0.2.2
* Sun Oct 01 2006 FlashCode <flashcode@flashtux.org> 0.2.1-1
- Released version 0.2.1
* Sat Aug 19 2006 FlashCode <flashcode@flashtux.org> 0.2.0-1
- Released version 0.2.0
* Thu May 25 2006 FlashCode <flashcode@flashtux.org> 0.1.9-1
- Released version 0.1.9
* Sat Mar 18 2006 FlashCode <flashcode@flashtux.org> 0.1.8-1
- Released version 0.1.8
* Sat Jan 14 2006 FlashCode <flashcode@flashtux.org> 0.1.7-1
- Released version 0.1.7
* Fri Nov 11 2005 FlashCode <flashcode@flashtux.org> 0.1.6-1
- Released version 0.1.6
* Sat Sep 24 2005 FlashCode <flashcode@flashtux.org> 0.1.5-1
- Released version 0.1.5
* Sat Jul 30 2005 FlashCode <flashcode@flashtux.org> 0.1.4-1
- Released version 0.1.4
* Sat Jul 02 2005 FlashCode <flashcode@flashtux.org> 0.1.3-1
- Released version 0.1.3
* Sat May 21 2005 FlashCode <flashcode@flashtux.org> 0.1.2-1
- Released version 0.1.2
* Sat Mar 20 2005 FlashCode <flashcode@flashtux.org> 0.1.1-1
- Released version 0.1.1
* Sat Feb 12 2005 FlashCode <flashcode@flashtux.org> 0.1.0-1
- Released version 0.1.0
* Sat Jan 01 2005 FlashCode <flashcode@flashtux.org> 0.0.9-1
- Released version 0.0.9
* Sat Oct 30 2004 FlashCode <flashcode@flashtux.org> 0.0.8-1
- Released version 0.0.8
* Sat Aug 08 2004 FlashCode <flashcode@flashtux.org> 0.0.7-1
- Released version 0.0.7
* Sat Jun 05 2004 FlashCode <flashcode@flashtux.org> 0.0.6-1
- Released version 0.0.6
* Thu Feb 02 2004 FlashCode <flashcode@flashtux.org> 0.0.5-1
- Released version 0.0.5
* Thu Jan 01 2004 FlashCode <flashcode@flashtux.org> 0.0.4-1
- Released version 0.0.4
* Mon Nov 03 2003 FlashCode <flashcode@flashtux.org> 0.0.3-1
- Released version 0.0.3
* Sun Oct 05 2003 FlashCode <flashcode@flashtux.org> 0.0.2-1
- Released version 0.0.2
* Sat Sep 27 2003 FlashCode <flashcode@flashtux.org> 0.0.1-1
- Released version 0.0.1
