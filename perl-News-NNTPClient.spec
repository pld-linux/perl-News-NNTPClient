%include	/usr/lib/rpm/macros.perl
Summary:	News-NNTPClient perl module
Summary(pl):	Modu³ perla News-NNTPClient
Name:		perl-News-NNTPClient
Version:	0.28
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/News/NNTPClient-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
Obsoletes:	perl-NNTPClient
BuildRoot:	/tmp/%{name}-%{version}-root

%description
News-NNTPClient - a client interface to NNTP. 

%description -l pl
News-NNTPClient - interfejs klienta NNTP.

%prep
%setup -q -n NNTPClient-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/News/NNTPClient
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/News/NNTPClient.pm
%{perl_sitelib}/News/NNTPFetchProgress.pm
%{perl_sitearch}/auto/News/NNTPClient

%{_mandir}/man3/*
