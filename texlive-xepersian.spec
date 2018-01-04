Name:		texlive-xepersian
Version:	20.0
Release:	1
Summary:	Persian for LaTeX, using XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/xepersian
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xepersian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xepersian.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xepersian.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports Persian typesetting, using the Persian
Modern fonts, by default.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xepersian
%{_texmfdistdir}/tex/xelatex/xepersian
%doc %{_texmfdistdir}/doc/xelatex/xepersian
#- source
%doc %{_texmfdistdir}/source/xelatex/xepersian

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
