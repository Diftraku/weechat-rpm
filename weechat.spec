%global _hardened_build 1
%global __provides_exclude_from ^%{_libdir}/weechat/plugins/.*$

Name:      weechat
Summary:   Portable, fast, light and extensible IRC client
Version:   0.4.1
Release:   1%{?dist}
Source:    http://weechat.org/files/src/%{name}-%{version}.tar.bz2
# Use Enchant when available.
Patch0:    weechat-0.4.1-enchant.patch
# Correctly determine the version of Ruby.
Patch1:    weechat-0.4.0-ruby-version.patch
URL:       http://weechat.org
Group:     Applications/Communications
License:   GPLv3
BuildRequires: ncurses-devel python-devel perl-devel ruby-devel
BuildRequires: gnutls-devel lua-devel enchant-devel
BuildRequires: docbook-style-xsl gettext ruby
BuildRequires: cmake perl-ExtUtils-Embed tcl-devel
BuildRequires: libcurl-devel zlib-devel pkgconfig

%description
WeeChat (Wee Enhanced Environment for Chat) is a portable, fast, light and
extensible IRC client. Everything can be done with a keyboard.
It is customizable and extensible with scripts.

%package devel
Summary: Development files for weechat
Group: Development/Libraries
Requires: %{name} = %{version}-%{release} pkgconfig

%description devel
WeeChat (Wee Enhanced Environment for Chat) is a portable, fast, light and
extensible IRC client. Everything can be done with a keyboard.
It is customizable and extensible with scripts.

This package contains include files and pc file for weechat.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%if 0%{?fedora} >= 19
%patch1 -p1
%endif

%build
mkdir build
pushd build
%cmake \
  -DPREFIX=%{_prefix} \
  -DLIBDIR=%{_libdir} \
  ..
make VERBOSE=1 %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
pushd build
make install DESTDIR="$RPM_BUILD_ROOT"
popd

%find_lang %name

%check
ctest

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc doc/en/weechat_faq.en.txt doc/en/weechat_quickstart.en.txt doc/en/weechat_scripting.en.txt
%doc doc/en/weechat_user.en.txt
%{_mandir}/man1/%{name}-curses.1*
%{_bindir}/%{name}-curses
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/*
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/weechat-plugin.h
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue May 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.1-1
- update to upstream release 0.4.1
- clean old changelog entries
- fix enchant patch set
- Ruby 2.0 crash now fixed upstream

* Tue Apr 02 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-7
- filter out automatically generated Provides that shouldn't be there (#947399)

* Sat Mar 30 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-6
- enable _hardened_build as weechat matches the "long running" criteria
- remove redundant PIE patch

* Fri Mar 29 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-5
- fix crash with Ruby 2.0

* Wed Mar 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-4
- rebuild with Ruby 2.0.0
- add patch to properly obtain the version of ruby
- fix bogus dates in older changelog entries

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-2
- reimplement enchant support as a separate patch
- implement additional enchant support for displaying spelling suggestions
  in weechat_aspell_get_suggestions(), which is a new function introduced by
  upstream in 0.4.0

* Mon Jan 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-1
- update to upstream release 0.4.0
- add CMAKE options (DPREFIX and DLIBDIR) which negate the need to patch
- remove enchant patches to keep close to upstream

* Sun Dec 02 2012 Paul Komkoff <i@stingr.net> - 0.3.9.2-2
- add zlib-devel dependency for epel6/ppc build

* Sat Dec  1 2012 Paul P. Komkoff Jr <i@stingr.net> - 0.3.9.2-1
- new upstream, long overdue

* Mon Nov 19 2012 Paul P. Komkoff Jr <i@stingr.net> - 0.3.8-4
- fix bz#878025

* Fri Nov 09 2012 Paul P. Komkoff Jr <i@stingr.net> - 0.3.8-3
- fix bz#875181

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Russell Golden <niveusluna@niveusluna.org> - 0.3.8-1
- New upstream version

* Fri Mar 16 2012 Paul P. Komkoff Jr <i@stingr.net> - 0.3.7-1
- new upstream version

* Wed Feb 08 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3.6-2
- Rebuilt for Ruby 1.9.3.

* Wed Jan 18 2012 Paul P. Komkoff Jr <i@stingr.net> - 0.3.6-1
- new upstream version

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Paul P. Komkoff Jr <i@stingr.net> - 0.3.5-2
- rebuilt

* Thu Jun  2 2011 Paul P. Komkoff Jr <i@stingr.net> - 0.3.5-1
- new upstream version

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug 28 2010 Paul P. Komkoff Jr <i@stingr.net> - 0.3.3-2
- fixed cmake config to accept python27

* Wed Aug 25 2010 Paul P. Komkoff Jr <i@stingr.net> - 0.3.3-1
- new upstream version

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri May  7 2010 Paul P. Komkoff Jr <i@stingr.net> - 0.3.2-2
- spec file fix

* Thu May  6 2010 Paul P. Komkoff Jr <i@stingr.net> - 0.3.2-1
- new upstream version
