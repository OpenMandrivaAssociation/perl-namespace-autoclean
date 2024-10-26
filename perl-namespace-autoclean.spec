%define upstream_name    namespace-autoclean

Name:       perl-%{upstream_name}
Version:    0.31
Release:    1

Summary:    Keep imports out of your namespace 
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/release/namespace-autoclean
Source0:    http://www.cpan.org/modules/by-module/namespace/namespace-autoclean-%{version}.tar.gz

BuildRequires: perl(B::Hooks::EndOfScope)
BuildRequires: perl(Class::MOP)
BuildRequires: perl(namespace::clean)
BuildRequires: perl-devel
BuildArch: noarch
Requires: perl(namespace::clean)
Requires:       perl(Sub::Identify)
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
%autosetup -p1 -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

# B::Hooks::EndOfScope >= 0.12 required for tests to pass...
# %check
# make test

%install
%make_install

%files
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/*
