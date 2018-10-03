%define upstream_name    namespace-autoclean
%define upstream_version 0.28

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2

Summary:    Keep imports out of your namespace 
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/namespace/namespace-autoclean-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

# B::Hooks::EndOfScope >= 0.12 required for tests to pass...
# %check
# make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*
