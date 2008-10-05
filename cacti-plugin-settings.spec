%define		plugin	settings
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Settings
Summary(pl.UTF-8):	Wtyczka do Cacti - Ustawienia
Name:		cacti-plugin-settings
Version:	0.5
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://mirror.cactiusers.org/downloads/plugins/%{plugin}-%{version}.zip
# Source0-md5:	a23406021b9e1c3a23d2ff61fec6de49
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
This Cacti plugin houses common settings and functions used by
different plugins.

%description -l pl.UTF-8
Ta wtyczka Cacti zbiera wspólne ustawienia i funkcje używane przez
różne wtyczki.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{plugindir}
