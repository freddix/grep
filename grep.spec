Summary:	GNU grep Utilities
Name:		grep
Version:	2.17
Release:	1
Epoch:		2
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/grep/%{name}-%{version}.tar.xz
# Source0-md5:	3b1f0cbf1139e76171f790665b1b41cf
URL:		http://www.gnu.org/software/grep/grep.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GNU versions of commonly used grep utilities. Grep searches one or
more input files for lines which contain a match to a specified
pattern and then prints the matching lines. GNU's grep utilities
include grep, egrep and fgrep.

%prep
%setup -q

rm -f po/no.po

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--disable-perl-regexp		\
	--without-included-regex	\
	--enable-nls
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo .so grep.1 > $RPM_BUILD_ROOT%{_mandir}/man1/egrep.1
echo .so grep.1 > $RPM_BUILD_ROOT%{_mandir}/man1/fgrep.1

%find_lang %{name}

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_mandir}/ja-grep-nozgrep.diff

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*info*

