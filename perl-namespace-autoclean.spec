%define upstream_name    namespace-autoclean
%define upstream_version 0.13

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Keep imports out of your namespace 
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/namespace/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(B::Hooks::EndOfScope)
BuildRequires: perl(Class::MOP)
BuildRequires: perl(namespace::clean)
BuildRequires: perl-devel
BuildArch: noarch
Requires: perl(namespace::clean)
Provides: perl(namespace::autoclean)

%description
When you import a function into a Perl package, it will naturally also be
available as a method.

The 'namespace::autoclean' pragma will remove all imported symbols at the
end of the current package's compile cycle. Functions called in the package
itself will still be bound by their name, but they won't show up as methods
on your class or instances.

This module is very similar to namespace::clean, except it will clean all
imported functions, no matter if you imported them before or after you
'use'd the pagma. It will also not touch anything that looks like a method,
according to 'Class::MOP::Class::get_method_list'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.120.0-2mdv2011.0
+ Revision: 657863
- rebuild for updated spec-helper

* Mon Feb 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.120.0-1
+ Revision: 636615
- update to new version 0.12

* Tue Jul 27 2010 Funda Wang <fwang@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 561096
- rebuild for perl 5.12

* Mon Jul 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 551216
- update to 0.11

* Wed Sep 16 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 443469
- update to 0.09

* Wed Jul 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 393404
- update to 0.08
- fixed summary field

* Sun Jun 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.70.0-3mdv2010.0
+ Revision: 387862
- fix dependencies

* Sat Jun 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-2mdv2010.0
+ Revision: 383240
- adding manual provides:

* Thu May 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 380351
- update to 0.07
- using %%perl_convert_version
- fix license

* Thu May 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2010.0
+ Revision: 378234
- update to new version 0.06

* Thu May 14 2009 Jérôme Quelin <jquelin@mandriva.org> 0.05-2mdv2010.0
+ Revision: 375698
- rebuild

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2010.0
+ Revision: 371859
- import perl-namespace-autoclean


* Mon May 04 2009 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist

