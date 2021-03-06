%define		plugin	settings
%define		php_min_version 5.0.0
Summary:	Plugin for Cacti - Settings
Summary(pl.UTF-8):	Wtyczka do Cacti - Ustawienia
Name:		cacti-plugin-%{plugin}
Version:	0.71
Release:	8
License:	GPL v2
Group:		Applications/WWW
Source0:	http://docs.cacti.net/_media/plugin:settings-v%{version}-1.tgz
# Source0-md5:	f29150ecb1433f17d51fb3f54398fd3e
URL:		http://docs.cacti.net/plugin:settings
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	cacti
Requires:	cacti(pia) >= 2.0
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
Requires:	php(date)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
Provides common infrastrucutre plugin services for Cacti's Plugin
Architecture.

Features:
- Provides DNS Lookup API
- Provides a Mailer API

%description -l pl.UTF-8
Ta wtyczka Cacti zbiera wspólne ustawienia i funkcje używane przez
różne wtyczki.

%prep
%setup -qc
mv %{plugin}/{LICENSE,README} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{plugindir}
